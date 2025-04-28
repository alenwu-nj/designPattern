class DataValidator:

    def validate(self, data):
        if isinstance(data, dict) and "type" in data:
            return True
        return False


class RiskAnalyzer:

    def analyze(self, data):
        data_type = data["type"]
        if data_type == "financial":
            return self.analyze_financial(data)
        elif data_type == "health":
            return self.analyze_health(data)
        elif data_type == "personal":
            return self.analyze_personal(data)
        else:
            return "Unknown data type"

    def analyze_financial(self, data):
        if data["value"] > 100000:
            return "High Financial Risk"
        return "Low Financial Risk"

    def analyze_health(self, data):
        if data["value"] < 50:
            return "High Health Risk"
        return "Low Health Risk"

    def analyze_personal(self, data):
        if data["value"] == "sensitive":
            return "High Personal Risk"
        return "Low Personal Risk"


class ReportGenerator:

    def generate_report(self, risk):
        return f"Risk assessment report: {risk}"


class RiskAssessmentFacade:

    def __init__(self):
        self.validator = DataValidator()
        self.analyzer = RiskAnalyzer()
        self.report_generator = ReportGenerator()

    def assess_risk(self, data):
        if not self.validator.validate(data):
            return "Invalid data format."

        risk_level = self.analyzer.analyze(data)

        report = self.report_generator.generate_report(risk_level)
        return report


def client_code(facade: RiskAssessmentFacade, data):
    result = facade.assess_risk(data)
    print(result)


if __name__ == "__main__":
    facade = RiskAssessmentFacade()

    financial_data = {"type": "financial", "value": 150000}
    client_code(facade, financial_data)

    health_data = {"type": "health", "value": 30}
    client_code(facade, health_data)

    personal_data = {"type": "personal", "value": "sensitive"}
    client_code(facade, personal_data)

    invalid_data = {"invalid_key": 150}
    client_code(facade, invalid_data)
