from flask import Flask, request, render_template
import util

app = Flask(__name__)

@app.route("/")
def home():
    team = util.get_team()
    venue = util.get_venue()
    return render_template("home.html", team = team, venue = venue)

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

        result = int(util.predict_score(runs, wickets, overs, runs_last_5, wickets_last_5, bat_team, bowl_team, venue))
        if result == 1:
            return "Something is wrong please fill proper input!!"
        else:
            return "Predicted score range of " + bat_team + " is between " + str(result - 10) + " to " + str(result + 5)
    except :
        return "Something is wrong please fill proper input!!"

if __name__ == "__main__":
    app.run()
