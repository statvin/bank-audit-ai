import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorEngine:
    """Gerencia a ingestão do PDF e a criação da memória vetorial."""

    def __init__(self):
        # Embeddings leves para rodar rápido
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

    def create_vector_store(self, pdf_path: str):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

        print(f"🔄 Processando documento...")
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()

        chunks = self.text_splitter.split_documents(docs)

        # Cria o índice FAISS
        vector_store = FAISS.from_documents(chunks, self.embeddings)
        print(f"✅ Indexação concluída: {len(chunks)} fragmentos criados.")

        return vector_store