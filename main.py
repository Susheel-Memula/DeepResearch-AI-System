from flask import Flask, render_template, request
from agents.researcher import research_agent
from agents.writer import writer_agent
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        query = request.form["query"]
        documents = research_agent(query)
        result = writer_agent(documents)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
