import sys
import os
from dotenv import load_dotenv
from src.retrieval import VectorEngine
from src.auditor import BankAuditor
from src.report import generate_pdf

# 1. Carrega variáveis de ambiente (.env)
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

if not api_key:
    print("❌ Erro: GROQ_API_KEY não encontrada no arquivo .env")
else:
    # 2. Inicializa os módulos
    print("🚀 Iniciando BankAudit AI...")
    try:
        engine = VectorEngine()
        auditor = BankAuditor(api_key)  # Passamos a chave aqui

        # 3. Cria a base de conhecimento
        pdf_path = input("📄 Digite o caminho do arquivo PDF: ")

        vector_store = engine.create_vector_store(pdf_path)

        # 4. Loop de interação
        print("\n" + "="*50)
        pergunta = input("🔎 Digite sua pergunta para a auditoria: ")
        print("🤖 Analisando documento... aguarde.")

        resultado = auditor.analyze(vector_store, pergunta)

        # 5. Exibe Resultado
        print("\n" + "="*50)
        print(f"RISCO: {resultado['risk']}")
        print("="*50)
        print(resultado['answer'])
        print("\nFontes:", resultado['sources'])

        # 6. Gera PDF
        generate_pdf(resultado)
        print("\n✅ Processo finalizado. Relatório gerado com sucesso.")

    except Exception as e:
        print(f"❌ Ocorreu um erro durante a execução: {e}")
