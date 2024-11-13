import json
import os
from random import shuffle
from dotenv import load_dotenv

from flask import Flask, render_template, url_for, request, redirect, session

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
questions = None


def get_questions() -> list[dict[str, str | list[str]]]:
    global questions
    if questions is None:
        with open("../questions.json") as file:
            questions = json.load(file)
    return questions


@app.route("/")
def home():
    session["score"] = session.get("score", 0)
    session["question_index"] = session.get("question_index", 0)
    return render_template("index.html")


@app.route("/secret")
def secret():
    return render_template("secret.html")


@app.route("/data-packets")
def data_packets():
    return render_template("data_packets.html")


@app.route("/ip-addresses")
def ip_addresses():
    return render_template("IP_addresses.html")


@app.route("/dns")
def domain_name_systems():
    return render_template("DNS.html")


@app.route("/interactive-sites-pages")
def interactive_pages():
    return render_template("interactive.html")


@app.route("/ecommerce")
def ecommerce():
    return render_template("ecommerce.html")


@app.route("/progressive-webapps")
def pwa():
    return render_template("pwa.html")


@app.route("/result")
def result():
    score = session.get("score", 0)
    total_questions = len(get_questions())
    return render_template("result.html", score=score, total_questions=total_questions)


@app.route("/reset-score")
def reset_score():
    session["score"] = 0
    session["question_index"] = 0
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = get_questions()
    question_index = session.get("question_index", 0)
    if question_index >= len(questions):
        return redirect(url_for("result"))

    question = questions[question_index]
    if request.method == "POST":
        selected_ans = request.form.get("answer")
        session["question_index"] += 1
        if selected_ans == question["answer"]:
            session["score"] += 1
            return redirect(url_for("quiz"))
        else:
            msg = f"Incorrect! The correct solution was '{question["answer"]}'."
            return render_template("feedback.html", feedback=msg)
    shuffle(question["options"])
    return render_template(
        "question.html",
        question=question,
        question_num=question_index + 1,
        total_questions=len(get_questions()),
    )


if __name__ == "__main__":
    app.run()
