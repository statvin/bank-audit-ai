import sys
from google.colab import userdata
from src.retrieval import VectorEngine
from src.auditor import BankAuditor
from src.report import generate_pdf

# 1. Recupera a chave segura pelo NOME que demos no menu da esquerda
try:
    api_key = userdata.get('GROQ_API_KEY')
except Exception as e:
    print(f"❌ Erro ao buscar a chave: {e}")
    api_key = None

if not api_key:
    print("❌ Erro: Chave não encontrada. Verifique se o nome no menu Secrets é exatamente 'GROQ_API_KEY'")
else:
    # 2. Inicializa os módulos
    print("🚀 Iniciando BankAudit AI...")
    try:
        # Se der erro de importação, recarregamos para garantir
        if 'src.auditor' not in sys.modules:
            import src.auditor
        
        engine = VectorEngine()
        auditor = BankAuditor(api_key) # Passamos a chave aqui

        # 3. Cria a base de conhecimento
        # Verifica se a variável pdf_filename existe (da célula anterior)
        if 'pdf_filename' not in globals():
            print("⚠️ Erro: Você precisa rodar a célula de UPLOAD do PDF antes desta!")
        else:
            vector_store = engine.create_vector_store(pdf_filename)

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
            print("\n✅ Processo finalizado. Baixe o PDF na aba de arquivos à esquerda.")

    except Exception as e:
        print(f"❌ Ocorreu um erro durante a execução: {e}")