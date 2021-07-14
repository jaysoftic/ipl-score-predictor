import numpy as np
import pickle
import json
import gzip


model = None
scaler = None
columns = None
encoded_teams = None

def load_artifacts():
    global model
    global scaler
    global columns
    global encoded_teams

    with gzip.open("artifacts/model.pickle.gz", "rb") as f:
        model = pickle.load(f)

    with open("artifacts/scaler.pickle", "rb") as f:
        scaler = pickle.load(f)

    with open("artifacts/columns.json", "r") as f:
        columns = np.array(json.load(f)["columns"])

    with open("artifacts/encodedteams.json", "r") as f:
        encoded_teams = json.load(f)

    return list(encoded_teams.keys()), list(columns[7:]) + ["Barabati Stadium"]


def predict_score(overs, wickets, runs, wickets_last_5, runs_last_5, bat_team, bowl_team, venue):
    try:
        X_pred = np.zeros(columns.size)

        X_pred[0:7] = [overs, wickets, runs, wickets_last_5, runs_last_5, encoded_teams[bat_team], encoded_teams[bowl_team]]

        if venue != "Barabati Stadium":
            # because i removed first columns for prevent dummy variable trap
            # and first column of venue was Barabati Stadium
            venue_index = np.where(columns == venue)[0][0]

        X_pred = scaler.transform([X_pred])

        result = model.predict(X_pred)[0]
        return result
    except :
        return 1 # error code 1

if __name__ == "__main__":
    load_artifacts()
    print("-------------------------------")
    print(predict_score(7, 0, 52, 0, 24, "Sunrisers Hyderabad", "Delhi Capitals", "Sheikh Zayed Stadium"))

