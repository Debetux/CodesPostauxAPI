from flask import abort, jsonify, render_template, request

from app import app
from models import City


@app.route('/', methods=['GET', 'POST'])
def homepage():
    query = request.args.get('postal_code', '84510')

    results = []

    for city in City.select().where(City.postal_code == query):
        results.append({
            "insee": city.insee,
            "name": city.name,
            "postal_code": city.postal_code,
            "label": city.label
        })

    return jsonify(results=results)
