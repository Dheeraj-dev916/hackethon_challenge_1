import sys
import os
import json
import time

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')

sys.path.append('backend')
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__))))

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from workflow_engine import AntigravityWorkflowEngine

CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"
PURPLE = "\033[95m"
WHITE  = "\033[97m"

SAMPLE_INPUT = """Over the last 24 hours, our customer support team has received 3,500 identical
tickets. Our automated billing system erroneously charged all premium tier subscribers
twice for their monthly renewal. Customers are threatening to cancel, and our social
media mentions are overwhelmingly negative (down 45% in sentiment). We need to
immediately reverse the duplicate charges and send out an apology email with a 10%
discount code for next month to prevent massive subscriber churn."""

def divider(char="─", color=CYAN):
    print(f"{color}" + char * 70 + f"{RESET}")

def print_header():
    print()
    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║         🧠  GOOGLE ANTIGRAVITY — AGENT TRACE LOGS                   ║{RESET}")
    print(f"{BOLD}{CYAN}║         Autonomous Content-to-Action Intelligence System             ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def section(title, color=YELLOW):
    print()
    divider("═", color)
    print(f"{BOLD}{color}  {title}{RESET}")
    divider("═", color)

def step(num, agent, task, status="✅ COMPLETED", color=GREEN):
    print(f"  {BOLD}{color}[STEP {num}]{RESET}  {WHITE}{agent}{RESET}  →  {DIM}{task}{RESET}  {color}{status}{RESET}")
    time.sleep(0.4)

def print_json_block(label, data, color=GREEN):
    print(f"\n  {BOLD}{color}{label}:{RESET}")
    lines = json.dumps(data, indent=4).splitlines()
    for line in lines:
        print(f"    {DIM}{line}{RESET}")
    time.sleep(0.2)

def run_trace():
    print_header()
    time.sleep(0.5)

    # ── SECTION 1: INPUT ────────────────────────────────────────────────────
    section("PHASE 1 │ UNSTRUCTURED INPUT INGESTION", CYAN)
    time.sleep(0.3)
    print(f"\n  {BOLD}Input Content:{RESET}")
    for line in SAMPLE_INPUT.strip().splitlines():
        print(f"  {DIM}{line.strip()}{RESET}")
        time.sleep(0.05)

    # ── SECTION 2: WORKPLAN ─────────────────────────────────────────────────
    section("PHASE 2 │ ANTIGRAVITY WORKPLAN (Master Planner Agent)", YELLOW)
    time.sleep(0.3)
    print(f"\n  {BOLD}Antigravity is generating the multi-agent execution plan...{RESET}")
    time.sleep(0.8)

    agents = [
        ("ContentUnderstandingAgent",  "Extract key facts, signals and anomalies from input"),
        ("InsightExtractionAgent",     "Identify root cause and primary insight pattern"),
        ("ImpactAnalysisAgent",        "Evaluate business impact and financial risk"),
        ("DecisionAgent",              "Generate concrete, domain-specific recommended action"),
        ("ToolExecutionAgent",         "Simulate API/system tool execution"),
        ("SimulationAgent",            "Simulate before/after system state change"),
    ]

    print()
    for i, (agent, objective) in enumerate(agents, 1):
        print(f"  {BOLD}{CYAN}[PLANNED TASK {i}]{RESET}  {PURPLE}{agent}{RESET}")
        print(f"              └─ Objective: {DIM}{objective}{RESET}")
        time.sleep(0.3)

    # ── SECTION 3: EXECUTION ────────────────────────────────────────────────
    section("PHASE 3 │ AGENTIC WORKFLOW EXECUTION (Reasoning Steps)", GREEN)
    time.sleep(0.3)

    print(f"\n  {BOLD}Initializing AntigravityRuntime...{RESET}")
    time.sleep(0.5)
    engine = AntigravityWorkflowEngine()
    print(f"  {GREEN}✅ Runtime initialized. Dispatching agents...{RESET}\n")
    time.sleep(0.5)

    result = engine.orchestrate(SAMPLE_INPUT)

    trace = result['antigravity_execution']['workflow_trace']
    plan  = result['antigravity_workflow_plan']['execution_plan']

    print(f"  {BOLD}Reasoning Steps:{RESET}")
    for t in trace:
        icon = "🔄" if t['status'] == 'started' else "✅"
        color = CYAN if t['status'] == 'started' else GREEN
        print(f"  {icon}  {color}[{t['agent']}]{RESET}  {t['task']}  →  {BOLD}{t['status'].upper()}{RESET}")
        time.sleep(0.25)

    # ── SECTION 4: DECISION FLOW ────────────────────────────────────────────
    section("PHASE 4 │ DECISION FLOW & REASONING CHAIN", PURPLE)
    time.sleep(0.3)

    results = result['antigravity_execution']['results']

    print_json_block("🔍 ContentUnderstandingAgent Output", results.get('ContentAgent', {}), CYAN)
    time.sleep(0.3)
    print_json_block("💡 InsightExtractionAgent Output", results.get('InsightAgent', {}), YELLOW)
    time.sleep(0.3)
    print_json_block("⚠️  ImpactAnalysisAgent Output", results.get('ImpactAgent', {}), RED)
    time.sleep(0.3)
    print_json_block("⚡ DecisionAgent Output", results.get('DecisionAgent', {}), GREEN)

    # ── SECTION 5: ACTION EXECUTION ─────────────────────────────────────────
    section("PHASE 5 │ ACTION SIMULATION & EXECUTION LOGS", GREEN)
    time.sleep(0.3)

    sim = results.get('SimulationAgent', {})
    tool = result['antigravity_execution'].get('tool_execution', {})

    print(f"\n  {BOLD}Tool Execution:{RESET}")
    print(f"  {GREEN}  Target System  :{RESET} {tool.get('tool', 'N/A')}")
    print(f"  {GREEN}  Status         :{RESET} {BOLD}{tool.get('status', 'N/A').upper()}{RESET}")
    print(f"  {GREEN}  Timestamp      :{RESET} {tool.get('timestamp', 'N/A')}")
    time.sleep(0.4)

    print(f"\n  {BOLD}Execution Logs:{RESET}")
    for log in sim.get('execution_logs', []):
        color = GREEN if "SUCCESS" in log else CYAN
        print(f"  {color}  {log}{RESET}")
        time.sleep(0.3)

    print(f"\n  {BOLD}Actions Executed:{RESET}")
    for action in sim.get('actions_executed', []):
        print(f"  {GREEN}  ✅ {action}{RESET}")
        time.sleep(0.2)

    # ── SECTION 6: OUTCOME ───────────────────────────────────────────────────
    section("PHASE 6 │ OUTCOME — SYSTEM STATE BEFORE vs AFTER", YELLOW)
    time.sleep(0.3)

    before = sim.get('system_state_before', {})
    after  = sim.get('system_state_after',  {})

    print(f"\n  {BOLD}{RED}  ◀ BEFORE STATE:{RESET}")
    for k, v in before.items():
        print(f"      {k:20s}: {RED}{v}{RESET}")
        time.sleep(0.15)

    print(f"\n  {BOLD}{GREEN}  ▶ AFTER STATE:{RESET}")
    for k, v in after.items():
        print(f"      {k:20s}: {GREEN}{v}{RESET}")
        time.sleep(0.15)

    print(f"\n  {BOLD}{GREEN}  Risk Mitigated: {sim.get('risk_mitigated', 'N/A')}{RESET}")
    time.sleep(0.3)

    # ── FINAL ────────────────────────────────────────────────────────────────
    section("✅  ANTIGRAVITY WORKFLOW COMPLETE", CYAN)
    print(f"\n  {BOLD}{GREEN}All agents executed successfully.{RESET}")
    print(f"  {BOLD}{CYAN}Orchestration Status: {result.get('orchestration_status', 'completed').upper()}{RESET}")
    print()
    divider("═", CYAN)
    print()

if __name__ == '__main__':
    run_trace()
