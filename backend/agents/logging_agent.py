from datetime import datetime

def logging_agent(logs):

    final_logs = []

    for log in logs:
        final_logs.append({
            "timestamp": str(datetime.now()),
            "message": log
        })

    return final_logs