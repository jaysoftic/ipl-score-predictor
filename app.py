from flask import Flask, request, render_template
import util

app = Flask(__name__)

teams, venues = util.load_artifacts()
teams.sort()
venues.sort()

@app.route("/")
def home():
    return render_template("home.html", team = teams, venue = venues)

@app.route("/predictedScore", methods = ["POST"])
def predicted_score():
    try:
        venue = request.form["venue"]
        bat_team = request.form["bat_team"]
        bowl_team = request.form["bowl_team"]
        overs = float(request.form["overs"])
        runs = int(request.form["runs"])
        wickets = int(request.form["wickets"])
        runs_last_5 = int(request.form["runs_last_5"])
        wickets_last_5 = int(request.form["wickets_last_5"])

        result = int(util.predict_score(overs, wickets, runs, wickets_last_5, runs_last_5, bat_team, bowl_team, venue))
        if result == 1:
            return "Something is wrong please fill proper input!!"
        else:
            return "Predicted score range of " + bat_team + " is between " + str(result - 5) + " to " + str(result + 5)
    except :
        return "Something is wrong please fill proper input!!"

if __name__ == "__main__":
    app.run()
