from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from src.risk import RiskAnalyzer

class BankAuditor:
    def __init__(self, api_key):
        # ATUALIZAÇÃO: Usando o novo modelo Llama 3.3 (mais potente e atual)
        self.llm = ChatGroq(
            api_key=api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )

        self.risk_engine = RiskAnalyzer()

        self.prompt_template = PromptTemplate(
            template="""
            VOCÊ É UM AUDITOR SÊNIOR DE CONFORMIDADE BANCÁRIA (CAIXA ECONÔMICA FEDERAL).

            DIRETRIZES:
            1. Responda APENAS com base no contexto abaixo.
            2. Se a informação não estiver no texto, diga: "Informação não localizada no documento."
            3. Cite a página da informação se possível.

            CONTEXTO:
            {context}

            PERGUNTA:
            {question}

            PARECER TÉCNICO:
            """,
            input_variables=["context", "question"]
        )

    def analyze(self, vector_store, question: str) -> dict:
        # Busca os 4 trechos mais relevantes
        retriever = vector_store.as_retriever(search_kwargs={"k": 4})
        docs = retriever.invoke(question)

        if not docs:
            return {"error": "Sem contexto."}

        # Monta o contexto
        context_text = "\n\n".join([d.page_content for d in docs])

        # Pergunta à IA
        response = self.llm.invoke(
            self.prompt_template.format(context=context_text, question=question)
        )

        # Calcula Risco
        risk_level = self.risk_engine.calculate_risk(context_text)

        return {
            "question": question,
            "answer": response.content,
            "risk": risk_level,
            "sources": [f"Pág {d.metadata.get('page', 0) + 1}" for d in docs]
        }