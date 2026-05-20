def visualization_agent(simulation_result):

    return {
        "before_state": simulation_result["system_state_before"],
        "after_state": simulation_result["system_state_after"],
        "summary": "System state improved successfully"
    }