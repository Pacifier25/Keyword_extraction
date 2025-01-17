# 🔑 Keyword Extraction App

The **Keyword Extraction App** is a web-based tool built using **Streamlit** that enables users to extract the most relevant keywords from text or PDF files. Designed with simplicity and functionality in mind, the app caters to professionals, researchers, and students who need to identify key topics or terms quickly and efficiently.

## 💡 How It Works

The application uses a **pre-trained TF-IDF vectorizer** and **transformer** to analyze input text. TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical method that evaluates the importance of words in a document relative to a collection of documents. The app calculates confidence scores for each keyword, reflecting its relative importance in the input text.

## 🛠️ Features

- **PDF File Support**: Upload PDF documents for automated text extraction.
- **Text Input**: Manually paste text for quick keyword extraction.
- **Confidence Scores**: Each keyword is assigned a relevance percentage.
- **Minimalist Interface**: A clean, easy-to-use design for maximum productivity.
- **Versatile Use Cases**: Ideal for academic, professional, and creative applications.

## ✨ Who Can Benefit?

This app is suitable for a wide range of users, including:
- **Researchers**: Summarize key points from large academic papers or studies.
- **Marketers**: Identify trends or critical insights in textual data.
- **Content Creators**: Optimize written material with relevant keywords for SEO.
- **Educators**: Extract essential terms and topics from teaching materials.

## 🎯 Why Use This App?

Whether you're working on academic research, business reports, or casual content, the **Keyword Extraction App** provides a fast, reliable, and user-friendly way to identify the most important terms in your text. Its intuitive interface and customizable features make it accessible for both technical and non-technical users.

---

## Installation 🚀

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   .\env\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place the pre-trained vectorizer (`vectorizer.pkl`) and transformer (`tfidf_transformer.pkl`) files in the project directory.

5. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## File Structure 📂

```
.
├── app.py                  # Main Streamlit application
├── vectorizer.pkl          # Pre-trained TF-IDF vectorizer
├── tfidf_transformer.pkl   # Pre-trained TF-IDF transformer
├── keyword_extraction.ipynb # Jupyter Notebook for model training
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## Requirements 📦

- Python 3.7 or later
- Required libraries:
  - Streamlit
  - scikit-learn
  - pandas
  - PyPDF2
  - joblib

Install the required libraries using:
```bash
pip install -r requirements.txt
```

---

## Screenshots 📸

### Main Page
![image](https://github.com/user-attachments/assets/106e4e5a-9713-4bc9-aa85-157a287b8d25)


### Extracted Keywords
![image](https://github.com/user-attachments/assets/72dba38d-bed0-4781-ae2f-9cb99a07309c)


---

## License 📜

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as per the terms of the license.

---

## Acknowledgments 🙌

- Built with ❤️ using [Streamlit](https://streamlit.io/).
- Inspired by the need for easy and efficient keyword extraction for text analysis.

---

## Contributions 🤝

Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.
