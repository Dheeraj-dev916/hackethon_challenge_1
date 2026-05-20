import sys
import os
import json
import uuid
from datetime import datetime

class PlannerAgent:
    def create_execution_plan(self, content):
        workflow_id = str(uuid.uuid4())
        
        import time
        time.sleep(0.1)
        snippet = content[:40] + "..." if len(content) > 40 else content
        dynamic_objectives = {
            "ContentUnderstandingAgent": f"Extract details from user input: '{snippet}'",
            "InsightExtractionAgent": f"Determine the root cause regarding: '{snippet}'",
            "ImpactAnalysisAgent": f"Analyze the financial and reputational impact of: '{snippet}'",
            "DecisionAgent": "Recommend steps to resolve the issue and prevent churn",
            "ToolExecutionAgent": "Execute automated resolution systems",
            "SimulationAgent": "Simulate the resolution of the incident"
        }

        return {
            "workflow_id": workflow_id,
            "created_at": datetime.utcnow().isoformat(),
            "execution_plan": [
                {
                    "step": 1,
                    "agent": "ContentUnderstandingAgent",
                    "objective": dynamic_objectives.get("ContentUnderstandingAgent", "Extract core facts"),
                    "status": "planned"
                },
                {
                    "step": 2,
                    "agent": "InsightExtractionAgent",
                    "objective": dynamic_objectives.get("InsightExtractionAgent", "Determine primary insight"),
                    "status": "planned"
                },
                {
                    "step": 3,
                    "agent": "ImpactAnalysisAgent",
                    "objective": dynamic_objectives.get("ImpactAnalysisAgent", "Analyze impact"),
                    "status": "planned"
                },
                {
                    "step": 4,
                    "agent": "DecisionAgent",
                    "objective": dynamic_objectives.get("DecisionAgent", "Recommend an action"),
                    "status": "planned"
                },
                {
                    "step": 5,
                    "agent": "ToolExecutionAgent",
                    "objective": dynamic_objectives.get("ToolExecutionAgent", "Simulate API tool execution"),
                    "status": "planned"
                },
                {
                    "step": 6,
                    "agent": "SimulationAgent",
                    "objective": dynamic_objectives.get("SimulationAgent", "Project before and after states"),
                    "status": "planned"
                }
            ]
        }
