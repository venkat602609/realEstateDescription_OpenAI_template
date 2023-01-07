import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        house = request.form["house"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(house),
            temperature=0.5,
            max_tokens=3500,
            top_p=1.0,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)


def generate_prompt(house):
    return """Generate a real estate adverstisement for a home with following description :\n House: """ + house

