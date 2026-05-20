from datetime import datetime

from agents.content_agent import content_agent
from agents.insight_agent import insight_agent
from agents.impact_agent import impact_agent
from agents.action_agent import action_agent
from agents.simulation_agent import simulation_agent
from agents.visualization_agent import visualization_agent
from agents.mega_agent import mega_agent
from tool_registry import ToolRegistry
from state_manager import StateManager


class AntigravityRuntime:
    def __init__(self):
        self.logs = []
        self.state_manager = StateManager()
        self.tools = ToolRegistry()

    def trace(self, agent, task, status, details=None):
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent,
            "task": task,
            "status": status,
            "details": details or ""
        }
        self.logs.append(log)

    def execute(self, content):
        self.trace("PlannerAgent", "workflow_planning", "started")

        workflow = [
            ("ContentAgent", "extract_content", content_agent),
            ("InsightAgent", "generate_insights", insight_agent),
            ("ImpactAgent", "analyze_business_impact", impact_agent),
            ("DecisionAgent", "recommend_actions", action_agent),
            ("SimulationAgent", "simulate_execution", simulation_agent),
            ("VisualizationAgent", "visualize_outcome", visualization_agent),
        ]

        self.trace("PlannerAgent", "workflow_planning", "completed", "6-stage workflow generated")

        context = content
        outputs = {}

        import time
        import time
        try:
            for agent, task, handler in workflow:
                self.trace(agent, task, "started")
                result = handler(context)
                outputs[agent] = result
                self.trace(agent, task, "completed")
                context = result

            # Dynamic tool execution based on DecisionAgent's recommendation
            decision = outputs.get("DecisionAgent", {})
            target_system = decision.get("target_system", "generic_api")
            
            tool_execution = self.tools.execute(target_system, decision)
            self.trace("ToolExecutionAgent", target_system, "completed", tool_execution["message"])

            self.state_manager.update("workflow_status", "completed")
            self.state_manager.update("recommended_action", decision.get("recommended_action", "Unknown Action"))

        except Exception as e:
            self.trace("System", "error", "failed", str(e))
            self.state_manager.update("workflow_status", "failed")
            return {
                "workflow_trace": self.logs,
                "workflow_state": self.state_manager.get_state(),
                "tool_execution": {"status": "failed", "error": str(e)},
                "results": outputs
            }

        return {
            "workflow_trace": self.logs,
            "workflow_state": self.state_manager.get_state(),
            "tool_execution": tool_execution,
            "results": outputs
        }
