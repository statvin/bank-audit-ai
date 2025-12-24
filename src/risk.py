class RiskAnalyzer:
    """
    Motor de análise heurística para classificação de risco bancário.
    """

    def __init__(self):
        # Termos críticos
        self.high_risk_terms = [
            "penalidade", "multa", "sanção", "fraude", "crime",
            "rescisão", "processo administrativo", "ilícito", "grave"
        ]
        self.medium_risk_terms = [
            "prazo", "obrigação", "dever", "monitoramento",
            "alerta", "revisão", "condicionante", "reporte", "advertência"
        ]

    def calculate_risk(self, text: str) -> str:
        text_lower = text.lower()

        if any(term in text_lower for term in self.high_risk_terms):
            return "ALTO"
        elif any(term in text_lower for term in self.medium_risk_terms):
            return "MÉDIO"

        return "BAIXO"