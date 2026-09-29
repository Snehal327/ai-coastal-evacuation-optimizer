def generate_alert(risk_level):

    if risk_level == "HIGH":
        return "CRITICAL ALERT: Evacuate immediately using the recommended safe route."

    elif risk_level == "MEDIUM":
        return "WARNING: Cyclone risk is increasing. Stay prepared for evacuation."

    else:
        return "INFO: Continue monitoring official cyclone updates."


if __name__ == "__main__":
    print(generate_alert("HIGH"))
