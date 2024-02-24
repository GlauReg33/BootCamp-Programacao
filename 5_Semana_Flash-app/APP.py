from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = requests.get(url)
    data = response.json()

    return render_template("characters.html", characters=data["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url)
    data = response.json()

    return render_template("profile.html", profile=data)


@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = requests.get(url)
    data = response.json()

    characters = []

    for character in data["results"]:
        character_info = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character_info)

    return {"characters": characters}



   