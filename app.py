from flask import Flask, render_template
from config import PROJECT, PAGES

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", project=PROJECT)

@app.route("/market-overview")
def market_overview():
    return render_template("tableau.html", project=PROJECT, page="market", pages=PAGES)

@app.route("/performance-analysis")
def performance_analysis():
    return render_template("tableau.html", project=PROJECT, page="performance", pages=PAGES)

@app.route("/story")
def story():
    return render_template("tableau.html", project=PROJECT, page="story", pages=PAGES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
