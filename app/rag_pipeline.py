from langchain_ollama import ChatOllama
from app.config import OLLAMA_MODEL_NAME, RETRIEVAL_K

def answer_question(vectorstore, question: str) -> tuple[str, list[int]]:
    """CV se relevant chunks retrieve karke local Ollama model se jawab leta hai."""
    results = vectorstore.similarity_search(question, k=RETRIEVAL_K)

    if not results:
        return "This information is not available in your CV.", []

    context = "\n\n".join(doc.page_content for doc in results)
    pages = sorted({
        doc.metadata["page"]
        for doc in results
        if "page" in doc.metadata
    })

    llm = ChatOllama(model=OLLAMA_MODEL_NAME, temperature=0, num_predict = 400)
    prompt = f"""
IMPORTANT INSTRUCTIONS:
- Give detailed and long answers.
- Explain the answer step by step.
- Use headings and bullet points where useful.
- Include relevant details from the CV.
- Do not give unnecessarily short answers.
- Never invent information that is not present in the CV.
- If information is missing, clearly mention that.

CV INFORMATION:
{context}

USER QUESTION:
{question}

Give a simple, clear answer.
"""
    response = llm.invoke(prompt)
    return response.content, pages
