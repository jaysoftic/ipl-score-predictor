import numpy as np
import pickle
import json
import gzip

model = None
features = None

def load_artifacts():
    global model
    global features

    with gzip.open("artifacts/ipl.pickle.gz", "rb") as f:
        model = pickle.load(f)

    with open("artifacts/features.json", "r") as f:
        features = json.load(f)

def get_team():
    load_artifacts()
    global features

    return features["team"]

def get_venue():
    global  features

    return features["venue"]


def predict_score(runs, wickets, overs, runs_last_5, wickets_last_5, bat_team, bowl_team, venue):
    try:
        global features
        global model
        columns = features["columns"]
        X_pred = np.zeros(len(columns))

        if bat_team != "chennai super kings":
            # because we removed first columns for prevent dummy variable trap
            # and first column of bat_team was chennai super kings

            bat_team_index = np.where(columns == "bat_team_" + bat_team)[0]

        if bowl_team != "chennai super kings":
            # because we removed first columns for prevent dummy variable trap
            # and first column of bowl_team was chennai super kings

            bowl_team_index = np.where(columns == "bowl_team_" + bowl_team)[0]

        if venue != "barabati stadium":
            # because we removed first columns for prevent dummy variable trap
            # and first column of venue was barabati stadium
            venue_index = np.where(columns == venue)[0]

        numeric_columns = [runs, wickets, overs, runs_last_5, wickets_last_5]
        for i in range(5):
            X_pred[i] = numeric_columns[i]

        result = model.predict([X_pred])[0]
        return result
    except :
        return 1 # error code 1

if __name__ == "__main__":
    print(get_team())
    print("-------------------------------")
    print(get_venue())
    print("-------------------------------")
    print(predict_score(61, 2, 7.2, 40, 2, "chennai super kings", "mumbai indians",
                  "barabati stadium"))

