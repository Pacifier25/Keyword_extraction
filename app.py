import streamlit as st
import joblib
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Keyword Extraction App", page_icon="🔑", layout="wide")

# Load the vectorizer and transformer
vectorizer = joblib.load('vectorizer.pkl')
tfidf_transformer = joblib.load('tfidf_transformer.pkl')

# Helper functions
def sort_coo(coo_matrix):
    """Sort a sparse matrix by descending order of its values."""
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: x[1], reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """Extract the top N items from a sorted vector."""
    sorted_items = sorted_items[:topn]
    results = {}
    for idx, score in sorted_items:
        results[feature_names[idx]] = score
    return results

def get_keywords_with_confidence(text, vectorizer, tfidf_transformer, topn=10):
    """Get keywords with their confidence scores."""
    # Generate TF-IDF vector
    tf_idf_vector = tfidf_transformer.transform(vectorizer.transform([text]))
    sorted_items = sort_coo(tf_idf_vector.tocoo())
    feature_names = vectorizer.get_feature_names_out()

    # Extract raw scores for the top keywords
    keywords = extract_topn_from_vector(feature_names, sorted_items, topn)

    # Normalize scores to calculate percentages
    total_score = sum(keywords.values())
    keywords_with_confidence = {k: round((v / total_score) * 100, 2) for k, v in keywords.items()}

    return keywords_with_confidence

def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file."""
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f7f9fc;
    }
    section[data-testid="stSidebar"] {
        background-color: #dff6ff;
    }
    h1 {
        color: #1a73e8;
    }
    h4 {
        color: #333333;
    }
    .stTextArea, .stFileUploader {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("<h1 style='text-align: center;'>🔑 Keyword Extraction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Upload your PDF or enter text, and we'll extract the top keywords for you!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar settings
st.sidebar.header("Settings")
num_keywords = st.sidebar.slider("Select the number of keywords to extract", min_value=1, max_value=20, value=10)
st.sidebar.markdown("### How it works:")
st.sidebar.info(
    """
    1. Upload a PDF file or paste text into the text area.
    2. Choose the number of keywords you want to extract.
    3. Click the **Extract Keywords** button.
    """
)

# File uploader
uploaded_file = st.file_uploader("📄 Upload a PDF file", type=["pdf"])
text_input = ""

# Extract text from the uploaded PDF
if uploaded_file is not None:
    try:
        text_input = extract_text_from_pdf(uploaded_file)
        st.success("✅ PDF uploaded and text extracted successfully!")
        with st.expander("🔍 View extracted text from PDF"):
            st.write(text_input)
    except Exception as e:
        st.error(f"❌ Error reading the PDF: {e}")

# Manual text input
text_input = st.text_area("✍️ Or, enter your text here:", text_input, height=200, help="You can paste text here for keyword extraction.")

# Extract keywords when button is clicked
if st.button("🔑 Extract Keywords"):
    if text_input.strip():
        # Get keywords with confidence scores
        keywords_with_confidence = get_keywords_with_confidence(text_input, vectorizer, tfidf_transformer, num_keywords)
        
        # Display keywords
        st.markdown("### 🎯 Extracted Keywords with Confidence Scores")
        st.write("Here are the top keywords extracted from your text along with their confidence scores:")
        
        keyword_df = pd.DataFrame(list(keywords_with_confidence.items()), columns=["Keyword", "Confidence (%)"])
        keyword_df["Confidence (%)"] = keyword_df["Confidence (%)"].map(lambda x: f"{x:.2f}%")
        st.table(keyword_df)

        # Provide a download button for the keywords
        csv = keyword_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Keywords as CSV",
            data=csv,
            file_name="keywords_with_confidence.csv",
            mime="text/csv",
        )
    else:
        st.warning("⚠️ Please upload a PDF or enter some text to extract keywords.")

