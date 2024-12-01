import json
import os
import re
from random import shuffle
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from flask import Flask, render_template, url_for, request, redirect, session

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
questions = None


def get_questions() -> list[dict[str, str | list[str]]]:
    global questions
    if questions is None:
        questions = json.loads(render_template("questions.json"))
    return questions


@app.context_processor
def inject_sidebar():
    return {
        "sidebar": "toggled"
        if session.get("sidebar-toggled", "false") == "true"
        else ""
    }


@app.route("/")
def home():
    session["score"] = session.get("score", 0)
    session["question_index"] = session.get("question_index", 0)
    session["sidebar-toggled"] = session.get("sidebar-toggled", "false")
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


@app.route("/web-accessibility-initiative")
def wai():
    return render_template("wai.html")


@app.route("/internationalisation")
def internationalisation():
    return render_template("internationalisation.html")


@app.route("/web-security")
def web_security():
    return render_template("websec.html")


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


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query", "")
        session["latest_query"] = query

    links = {
        "data_packets": url_for("data_packets"),
        "DNS": url_for("domain_name_systems"),
        "ecommerce": url_for("ecommerce"),
        "index": url_for("home"),
        "interactive": url_for("interactive_pages"),
        "IP_addresses": url_for("ip_addresses"),
        "pwa": url_for("pwa"),
        "wai": url_for("wai"),
        "internationalisation": url_for("internationalisation"),
        "websec": url_for("web_security"),
    }

    results = []

    for page in links:
        page_content = render_template(f"{page}.html")
        bs4 = BeautifulSoup(page_content, "html.parser")
        if session["latest_query"].lower() in page_content.lower():
            desc = ""
            occurrences: list[str] = [
                q.text for q in bs4.findAll("div", {"class": "description"})
            ]
            for occurrence in occurrences:
                sentences = occurrence.split(". ")
                # only add to result if the div contains the searched text
                for sentence in sentences:
                    if session["latest_query"].lower() in sentence.lower():
                        # use regex for a case-insensitive replace
                        replacer = re.compile(
                            re.escape(session["latest_query"]), re.IGNORECASE
                        )
                        sentence = replacer.sub(
                            f"<mark>{session["latest_query"]}</mark>", sentence
                        )
                        desc += f"...{sentence}... "
            if desc:
                results.append(
                    {
                        "title": bs4.find("div", {"class": "title"}).find("h1").text,
                        "desc": desc,
                        "url": links[page],
                    }
                )

    return render_template(
        "search.html", query=session.get("latest_query", ""), results=results
    )


@app.route("/backend/toggle-sidebar", methods=["GET"])
def toggle_sidebar():
    session["sidebar-toggled"] = (
        "true" if session.get("sidebar-toggled", "false") == "false" else "false"
    )
    return session["sidebar-toggled"]


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
    # TODO: add this to contents when more pages are added, also to long pages where sections can be split
    # https://blog.hubspot.com/website/css-fade-in#text-transition
    # TODO: split pages into sections, e.g. Pros, Cons
