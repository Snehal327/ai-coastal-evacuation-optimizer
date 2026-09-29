import pandas as pd


def calculate_cyclone_risk(data):
    risk_scores = []

    for _, row in data.iterrows():
        score = 0

        if row["wind_speed"] >= 120:
            score += 40
        elif row["wind_speed"] >= 80:
            score += 25
        else:
            score += 10

        if row["rainfall"] >= 200:
            score += 30
        elif row["rainfall"] >= 100:
            score += 20
        else:
            score += 10

        if row["pressure"] <= 980:
            score += 30
        elif row["pressure"] <= 995:
            score += 20
        else:
            score += 10

        risk_scores.append(score)

    data["cyclone_risk_score"] = risk_scores

    data["risk_level"] = data["cyclone_risk_score"].apply(
        lambda x: "HIGH" if x >= 70
        else "MEDIUM" if x >= 40
        else "LOW"
    )

    return data


if __name__ == "__main__":
    data = pd.read_csv("../data/cyclone_data.csv")

    result = calculate_cyclone_risk(data)

    print(result)
