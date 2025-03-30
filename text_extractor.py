import pdfplumber
import docx

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def extract_text_from_docx(docx_path):
    """Extracts text from a DOCX file."""
    doc = docx.Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(txt_path):
    """Extracts text from a TXT file."""
    with open(txt_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

# Test the functions
if __name__ == "__main__":
    pdf_text = extract_text_from_pdf("D:\ML projects\AI resume matcher\PRASAD CV.pdf")  # Replace with an actual file
    # docx_text = extract_text_from_docx("sample_resume.docx")
    # txt_text = extract_text_from_txt("sample_resume.txt")

    print("PDF Text:\n", pdf_text[:500])  # Print first 500 characters
    # print("\nDOCX Text:\n", docx_text[:500])
    # print("\nTXT Text:\n", txt_text[:500])
