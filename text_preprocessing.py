import spacy
import string
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords (only needed once)
nltk.download("stopwords")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Cleans and preprocesses text for NLP."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization using spaCy
    doc = nlp(text)
    
    # Remove stopwords and lemmatize
    processed_text = " ".join([token.lemma_ for token in doc if token.text not in stopwords.words("english")])
    
    return processed_text

# Test the function
if __name__ == "__main__":
    sample_text = """Experienced Software Engineer with 5+ years in Python and Machine Learning.
    Worked at Google as a Data Scientist."""
    
    cleaned_text = preprocess_text(sample_text)
    print("Processed Text:\n", cleaned_text)
