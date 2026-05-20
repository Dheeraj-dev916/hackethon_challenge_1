from antigravity_runtime import AntigravityRuntime
from agents.planner_agent import PlannerAgent


class AntigravityWorkflowEngine:

    def __init__(self):
        self.runtime = AntigravityRuntime()
        self.planner = PlannerAgent()

    def orchestrate(self, content):
        plan = self.planner.create_execution_plan(content)
        execution = self.runtime.execute(content)

        return {
            "antigravity_workflow_plan": plan,
            "antigravity_execution": execution,
            "orchestration_status": "completed"
        }
