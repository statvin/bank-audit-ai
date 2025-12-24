# BankAudit AI 🛡️

> **Auditor de Conformidade Bancária Automatizado**  
> RAG + Llama 3.3 + Análise Heurística

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/LLM-Llama%203.3-orange)
![Status](https://img.shields.io/badge/Status-MVP%20Funcional-green)

---

## 💼 O Problema de Negócio

A auditoria de contratos bancários e normativos (BACEN, CVM) é um processo
denso, manual e sujeito a erro humano. Profissionais perdem horas buscando
cláusulas específicas de penalidade, prazos e conformidade em documentos que
frequentemente ultrapassam 50 páginas.

---

## 💡 A Solução

O **BankAudit AI** é um sistema modular de auditoria técnica que:

1. **Ingere** documentos complexos (PDFs de contratos, editais, resoluções).
2. **Recupera** informações precisas com rastreabilidade (RAG – Retrieval-Augmented Generation).
3. **Classifica o Risco** automaticamente (Alto / Médio / Baixo) utilizando um motor híbrido
   de IA e regras determinísticas de compliance.
4. **Gera Relatórios** formais em PDF prontos para análise gerencial.

---

## 📸 Prova de Conceito (POC)

*Teste real realizado com o Contrato de Cartão de Crédito PF da Caixa Econômica Federal.*

**Entrada (Pergunta):**
> Quais são os encargos e penalidades cobrados em caso de atraso no pagamento da fatura?

**Saída do Sistema (Relatório Gerado):**
> 🔴 **Risco Identificado: ALTO**
>
> De acordo com o contrato, serão cobrados:
> - Juros sobre o valor mínimo (**Cláusula 11.2**)
> - Encargos contratuais sobre saque emergencial (**Cláusula 11.3**)
> - Penalidades contratuais previstas na **Cláusula 11.4**
>
> *Fontes: Página 6, Página 2*

---

## 🛠️ Arquitetura do Sistema

O projeto foi desenvolvido seguindo princípios de **Clean Code** e
**Modularidade**, com responsabilidades bem definidas:

```text
bank-audit-ai/
├── src/
│   ├── retrieval.py   # Ingestão e vetorização (FAISS + embeddings locais)
│   ├── risk.py        # Regras determinísticas de compliance
│   ├── auditor.py     # Orquestração de IA (Groq / Llama 3.3)
│   └── report.py      # Geração de relatórios PDF
├── main.py            # Entry point da aplicação
├── requirements.txt   # Dependências
└── .env               # Credenciais (não versionado)
```

---

## 🚀 Stack Tecnológica

- **LLM Orchestration:** LangChain
- **Model:** Llama 3.3-70B (via Groq API — baixa latência)
- **Vector Database:** FAISS (in-memory)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
- **Reporting:** FPDF
- **Language:** Python 3.10+

---

## ⚙️ Instalação e Uso

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/statvin/bank-audit-ai.git
cd bank-audit-ai
```

### 2️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure a API Key
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Groq:

```ini
GROQ_API_KEY=gsk_sua_chave_aqui
```

### 4️⃣ Execute a auditoria
```bash
python main.py
```

O sistema solicitará:
- o caminho do PDF
- a pergunta de auditoria no terminal

---

## 🔒 Privacidade e Segurança

Este projeto foi desenhado considerando a sensibilidade de dados bancários
(**Bank-grade Security principles**):

- **Embeddings locais:** a vetorização ocorre localmente, reduzindo exposição de dados.
- **Zero retention:** o modelo Llama 3 via Groq é usado apenas para inferência.

---

## 👤 Autor

**Vinícius Ramos**  
Analista de Sistemas
