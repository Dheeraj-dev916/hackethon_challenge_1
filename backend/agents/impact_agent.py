import sys
import os
import json

def impact_agent(insight_result):
    import time
    time.sleep(0.1)
    
    try:
        issue = insight_result.get('root_cause', '').replace("Underlying system failure related to: ", "")
    except:
        issue = "the issue"
        
    return {
        "business_impact": f"High risk of workflow disruption and brand damage if '{issue}' is not immediately resolved.",
        "financial_risk": "Moderate to High (Depends on resolution time)",
        "affected_stakeholders": ["End Users", "Support Team", "Operations"],
        "urgency": "CRITICAL"
    }