import streamlit as st
from app.config import PAGE_TITLE, PAGE_ICON
from app.embedding import load_embeddings
from app.pdf_loader import load_pdf_documents
from app.text_splitter import split_documents
from app.vector_store import create_vector_store
from app.rag_pipeline import answer_question

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title(f"{PAGE_ICON} My Private CV AI Agent")
st.write("Upload your CV, process it, and ask questions using only its contents.")

@st.cache_resource
def get_embeddings():
    return load_embeddings()

embeddings = get_embeddings()

uploaded_file = st.file_uploader("Upload your CV PDF", type=["pdf"])

if uploaded_file is not None and st.button("Process My CV"):
    with st.spinner("Reading and processing your CV..."):
        try:
            documents = load_pdf_documents(uploaded_file.getvalue())
            if not documents:
                st.error("PDF se readable text nahi mila. Check karein ke PDF scanned image na ho.")
            else:
                chunks = split_documents(documents)
                vectorstore = create_vector_store(chunks, embeddings)
                st.session_state["vectorstore"] = vectorstore
                st.success(f"CV processed successfully! Total chunks: {len(chunks)}")
        except Exception as exc:
            st.error(f"CV process nahi ho saki: {exc}")

if "vectorstore" in st.session_state:
    st.subheader("Ask questions about your CV")
    question = st.chat_input("Example: What is my education?")
    if question:
        with st.spinner("Searching your CV and preparing an answer..."):
            try:
                answer, pages = answer_question(
                    st.session_state["vectorstore"], question
                )
                st.chat_message("user").write(question)
                st.chat_message("assistant").write(answer)
                st.caption(f"CV source page(s): {pages if pages else 'Not identified'}")
            except Exception as exc:
                st.error(f"Answer generate nahi ho saka: {exc}")
else:
    st.info("Pehle CV upload karein aur 'Process My CV' par click karein.")
