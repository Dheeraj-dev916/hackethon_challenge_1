import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_model, parse_json_response

def mega_agent(content):
    prompt = f"""
You are the master autonomous orchestrator. You must analyze the following unstructured content and process it through 5 stages of reasoning: Content Understanding, Insight Extraction, Impact Analysis, Decision Making, and Simulation.

Return ONLY a JSON object with exactly this schema:
{{
    "ContentAgent": {{
        "key_findings": ["list of facts"],
        "metrics": ["list of data points"],
        "anomalies": ["list of unusual patterns"],
        "regions_affected": ["list of locations"],
        "risk_signals": ["list of potential risks"]
    }},
    "InsightAgent": {{
        "primary_insight": "The core problem or opportunity identified",
        "root_cause": "The underlying reason for this situation",
        "insight_category": "Operational, Financial, Strategic, etc.",
        "confidence_score": 95
    }},
    "ImpactAgent": {{
        "business_impact": "How this affects the business",
        "financial_risk": "High, Medium, or Low",
        "affected_stakeholders": ["list of stakeholders"],
        "urgency": "Immediate, Short-term, or Long-term"
    }},
    "DecisionAgent": {{
        "recommended_action": "The single best action to mitigate the risk",
        "execution_steps": ["list of 3-5 concrete steps"],
        "priority_level": "Urgent, High, Medium, or Low",
        "target_system": "Name of the system to execute this action (e.g. 'crm_api', 'billing_system', 'fleet_manager')"
    }},
    "SimulationAgent": {{
        "simulation_status": "SUCCESS",
        "actions_executed": ["list of mocked actions performed"],
        "system_state_before": "Description of the broken or original state",
        "system_state_after": "Description of the fixed or new state",
        "risk_mitigated": "Yes"
    }}
}}

Content to analyze:
{content}
"""
    try:
        model = get_model()
        response = model.generate_content(prompt)
        return parse_json_response(response)
    except Exception as e:
        print(f"Error in mega_agent: {e}")
        return {
            "ContentAgent": {
                "key_findings": [f"ERROR: {str(e)}"],
                "metrics": ["N/A"],
                "anomalies": ["N/A"],
                "regions_affected": ["N/A"],
                "risk_signals": ["N/A"]
            },
            "InsightAgent": {
                "primary_insight": "Failed to extract insight",
                "root_cause": "Unknown",
                "insight_category": "Error",
                "confidence_score": 0
            },
            "ImpactAgent": {
                "business_impact": "Unknown impact",
                "financial_risk": "Unknown",
                "affected_stakeholders": ["None"],
                "urgency": "Low"
            },
            "DecisionAgent": {
                "recommended_action": "No action recommended",
                "execution_steps": ["System error occurred"],
                "priority_level": "Low",
                "target_system": "generic_api"
            },
            "SimulationAgent": {
                "simulation_status": "FAILED",
                "actions_executed": ["None"],
                "system_state_before": "Unknown",
                "system_state_after": "Unknown",
                "risk_mitigated": "No"
            }
        }
