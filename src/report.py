from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Relatorio de Auditoria - BankAudit AI', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

def generate_pdf(data: dict, filename="parecer_final.pdf"):
    pdf = PDFReport()
    pdf.add_page()

    # Seção de Risco
    pdf.set_font("Arial", 'B', 12)
    cor = (200, 0, 0) if data['risk'] == "ALTO" else (0, 0, 0)
    pdf.set_text_color(*cor)
    pdf.cell(0, 10, f"NIVEL DE RISCO IDENTIFICADO: {data['risk']}", ln=True)
    pdf.set_text_color(0, 0, 0) # Volta para preto
    pdf.ln(5)

    # Pergunta
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 10, "Questao Analisada:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 7, data['question'])
    pdf.ln(5)

    # Resposta
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 10, "Parecer Tecnico:", ln=True)
    pdf.set_font("Arial", size=10)
    # Tratamento simples para caracteres
    texto = data['answer'].encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 7, texto)
    pdf.ln(5)

    # Fontes
    pdf.set_font("Arial", 'I', 9)
    pdf.cell(0, 10, "Fontes de Referencia:", ln=True)
    for source in data['sources']:
        pdf.cell(0, 7, f"- {source}", ln=True)

    pdf.output(filename)
    print(f"📄 Relatório PDF gerado: {filename}")