import sys
import os
import json

def insight_agent(content_result):
    import time
    time.sleep(0.1)
    
    # Extract the user's snippet from the content result
    try:
        snippet_text = content_result.get('key_findings', ['User report'])[0]
        issue = snippet_text.replace("User reported: '", "").replace("'", "")
    except:
        issue = "the reported issue"
        
    return {
        "primary_insight": f"A critical situation has developed regarding {issue}. This requires immediate attention to prevent further escalation and user impact.",
        "root_cause": f"Underlying system failure related to: {issue}",
        "insight_category": "Operations/Customer Relations",
        "confidence_score": 95
    }