import sys
import traceback
sys.path.append('backend')
from backend.workflow_engine import AntigravityWorkflowEngine

print("Starting engine test...")
try:
    engine = AntigravityWorkflowEngine()
    result = engine.orchestrate("Testing the custom input for our system.")
    print("SUCCESS!")
    print(result)
except Exception as e:
    print("ERROR:")
    traceback.print_exc()
