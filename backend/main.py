# backend/main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS

# Your Google API key
GOOGLE_API_KEY = "AIzaSyA2u0pTSGMRwSq0MgfMduhiat-DN_eXaBU"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_pdf_and_search(pdf_path, query):
    try:
        # Set Google API key
        os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

        # Load PDF and split into pages
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()

        # Extract embeddings from pages
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        # Create vector store
        db = FAISS.from_documents(pages, embeddings)

        # Perform similarity search based on query
        docs = db.similarity_search(query)

        # Construct context for generating response
        content = "\n".join([x.page_content for x in docs])
        qa_prompt = "Use the following pieces of context to answer the user's question. If you don't know the answer, just say that you don't know, don't try to make up an answer.----------------"
        input_text = qa_prompt + "\nContext:" + content + "\nUser question:\n" + query

        # Generate response using Google's Generative AI
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        result = llm.invoke(input_text)

        # Return generated response
        return result.content
    except Exception as e:
        return str(e)

@app.post("/submit")
async def submit_form(pdf: UploadFile = File(...), query: str = Form(...)):
    pdf_path = f"./{pdf.filename}"
    with open(pdf_path, "wb") as f:
        f.write(pdf.file.read())
    result = load_pdf_and_search(pdf_path, query)
    os.remove(pdf_path)  # Clean up the uploaded file
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
