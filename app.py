import streamlit as st
import pdfplumber
import docx
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to process uploaded file
def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file)
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return None

# Function to compute similarity using BERT
def compute_similarity_bert(resume, job_desc):
    resume_embedding = model.encode(resume, convert_to_tensor=True)
    job_desc_embedding = model.encode(job_desc, convert_to_tensor=True)
    
    # Compute cosine similarity
    similarity_score = cosine_similarity(resume_embedding.cpu().numpy().reshape(1, -1),
                                         job_desc_embedding.cpu().numpy().reshape(1, -1))
    return similarity_score[0][0]  # Return the match score

# Streamlit UI
st.title("AI-Powered Resume-to-Job Matcher")
st.write("Upload a Resume and Job Description to check their match score.")

resume_file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
job_desc_file = st.file_uploader("Upload Job Description (TXT, DOCX)", type=["txt", "docx"])

if st.button("Match Resume"):
    if resume_file and job_desc_file:
        resume_text = extract_text(resume_file)
        job_desc_text = extract_text(job_desc_file)

        if resume_text and job_desc_text:
            score = compute_similarity_bert(resume_text, job_desc_text)
            st.subheader(f"Resume Match Score: {score:.2f}")
        else:
            st.error("Could not extract text from one of the files. Please try again.")
    else:
        st.warning("Please upload both files before clicking Match.")
