# Copyright 2024 Joachim Alladio-Zerbé -- ALLJ28099800
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import g
from .database import Database

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.route("/")
def home():
    db = get_db()
    terme = request.args.get("q", "").strip()

    if terme:
        return redirect(url_for("resultat", q=terme))

    animaux = db.get_random_animaux()
    return render_template("index.html", animaux=animaux)

@app.route("/resultat")
def resultat():
    db = get_db()
    terme = request.args.get("q").strip()
    animaux = db.search_animaux(terme)
    if not animaux:
        message = "Aucun animal trouvé selon la recherche"
        return render_template("index.html", animaux=animaux, message=message)
    return render_template("index.html", animaux=animaux, message=None)


@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/animal/<int:animal_id>")
def animal_detail(animal_id):
    db = get_db()
    animal = db.get_animal(animal_id)
    if animal is None:
        return "Animal non trouvé", 404
    return render_template("animal.html", animal=animal)

@app.route("/liste")
def liste_animal():
    db = get_db()
    animaux = db.get_animaux()
    if not animaux:
        message = "Aucun animal en adoption pour le moment."
        return render_template("listeanimal.html", animaux=[], message=message)
    return render_template("listeanimal.html", animaux=animaux, message=None)

@app.route("/add", methods=["GET", "POST"])
def add():
    erreurs = {}
    form_data = {}
    db = get_db()
    ajoutReussi = "None"

    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        espece = request.form.get("espece", "").strip()
        race = request.form.get("race", "").strip()
        age = request.form.get("age", "").strip()
        description = request.form.get("description", "").strip()
        courriel = request.form.get("courriel", "").strip()
        adresse = request.form.get("adresse", "").strip()
        ville = request.form.get("ville", "").strip()
        cp = request.form.get("cp", "").strip()

        if not nom or len(nom) < 3 or len(nom) > 20:
            erreurs["nom"] = "Erreur serveur : Nom requis"
        if not espece:
            erreurs["espece"] = "Erreur serveur : Espèce requise"
        if not race:
            erreurs["race"] = "Erreur serveur : Race requise"
        if not age.isdigit() or int(age) < 0 or int(age) > 30:
            erreurs["age"] = "Erreur serveur : L'âge doit être un nombre positif"
        if not description:
            erreurs["description"] = "Erreur serveur : Description requise"
        if "@" not in courriel or not courriel:
            erreurs["courriel"] = "Erreur serveur : Courriel invalide"
        if not adresse:
            erreurs["adresse"] = "Erreur serveur : Adresse requise"
        if not ville:
            erreurs["ville"] = "Erreur serveur : Ville requise"
        if not cp:
            erreurs["cp"] = "Erreur serveur : Code postal requis"

        form_data = request.form

        if not erreurs:
            ajoutReussi = db.add_animal(nom, espece, race, age, description, courriel, adresse, ville, cp)
            if ajoutReussi != "None":
                return redirect(url_for("add_succes"))
    return render_template("form.html", erreurs=erreurs, form_data=form_data, ajout=ajoutReussi)

@app.route("/add_succes")
def add_succes():
    return render_template("add_succes.html")
