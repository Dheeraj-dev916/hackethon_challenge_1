
class DecisionAgent:
    def decide_action(self, insights, impact):
        severity = impact.get("severity", "medium")

        if severity == "high":
            return {
                "recommended_action": "Launch retention campaign and notify operations",
                "priority": "critical",
                "confidence": 0.94,
                "reasoning": [
                    "Revenue impact projected to increase",
                    "Customer churn probability rising",
                    "Immediate intervention recommended"
                ]
            }

        return {
            "recommended_action": "Monitor trends and optimize pricing",
            "priority": "medium",
            "confidence": 0.81,
            "reasoning": [
                "Moderate decline detected",
                "Controlled intervention sufficient"
            ]
        }
