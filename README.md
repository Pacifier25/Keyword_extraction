# Keyword Extraction App 🔑

This is a web-based application built using Streamlit that allows users to extract top keywords from text or PDF files. The app uses a pre-trained TF-IDF vectorizer and transformer to analyze the input text and generate keywords with confidence scores.

---

## 🚀 Features

- **PDF Upload**: Extracts text from uploaded PDF files.
- **Text Input**: Allows manual text entry for keyword extraction.
- **Customizable Keyword Count**: Includes a slider in the sidebar, enabling users to select the number of keywords they wish to extract (from 1 to 20).
- **Confidence Scores**: Displays keyword relevance as a percentage for better insights.
- **Downloadable Results**: Provides the extracted keywords as a downloadable CSV file.
- **Interactive UI**: Designed with Streamlit for an intuitive and responsive experience.

---

## How It Works 🛠️

1. **Upload or Enter Text**:
   - Upload a PDF file or paste text into the provided text area.
2. **Set Parameters**:
   - Use the sidebar to select the number of keywords you want to extract.
3. **Extract Keywords**:
   - Click the **Extract Keywords** button to get the top keywords with confidence scores.
4. **View and Download Results**:
   - View extracted keywords in a table format.
   - Download the results as a CSV file.

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
