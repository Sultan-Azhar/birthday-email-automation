import fitz
from langchain_core.documents import Document

def load_pdf_documents(pdf_bytes: bytes) -> list[Document]:
    """PDF bytes se har page ka readable text nikalta hai."""
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
    documents = []
    try:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text().strip()
            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={"page": page_number}
                    )
                )
    finally:
        pdf.close()
    return documents
