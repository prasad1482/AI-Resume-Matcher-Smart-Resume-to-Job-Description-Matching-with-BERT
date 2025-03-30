import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample resume and job description (Replace with real data)
resume_text = "Experienced Software Engineer with expertise in Python and Machine Learning. Worked at Google."
job_desc_text = "Looking for a Software Engineer with strong Python skills and experience in Machine Learning."

def compute_similarity(resume, job_desc):
    """Computes similarity score between resume and job description."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume, job_desc])
    
    # Compute Cosine Similarity
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    
    return similarity_score[0][0]  # Return the similarity score

# Test the function
if __name__ == "__main__":
    score = compute_similarity(resume_text, job_desc_text)
    print(f"Resume Match Score: {score:.2f}")
