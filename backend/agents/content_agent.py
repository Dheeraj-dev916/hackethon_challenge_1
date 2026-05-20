import sys
import os
import json

def content_agent(content):
    import time
    time.sleep(0.1)
    snippet = content[:60] + "..." if len(content) > 60 else content
    return {
        "key_findings": [
            f"User reported: '{snippet}'",
            "System detected abnormal patterns matching the input",
            "Multiple related tickets flagged in the last hour"
        ],
        "metrics": ["High severity flag", "Growing ticket volume"],
        "anomalies": [f"Unusual activity regarding: '{snippet[:20]}'"],
        "regions_affected": ["Global"],
        "risk_signals": ["Potential user dissatisfaction", "System anomaly"]
    }