from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *


@app.route("/")
def main():
    return "Welcome to Penn Club Review!"


@app.route("/api")
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})

@app.route("/api/clubs", methods=["GET"])
def get_clubs():
    clubs = Club.query.all()
    clubs_list = [{
        "id": club.id,
        "code": club.code,
        "name": club.name,
        "description": club.description,
        "tags": club.tags
    } for club in clubs]
    return jsonify(clubs_list)

@app.route("/api/user/<username>", methods=["GET"])
def get_user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "username": user.username,
            "email": user.email
        })
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route("/api/clubs/search", methods=["GET"])
def search_clubs():
    search_term = request.args.get("q", "").lower()
    clubs = Club.query.filter(Club.name.ilike(f"%{search_term}%")).all()
    clubs_list = [{
        "id": club.id,
        "code": club.code,
        "name": club.name,
        "description": club.description,
        "tags": club.tags
    } for club in clubs]
    return jsonify(clubs_list)

@app.route("/api/clubs", methods=["POST"])
def create_club():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    new_club = Club(
        code=data.get("code"),
        name=data.get("name"),
        description=data.get("description"),
        tags=data.get("tags", [])
    )
    db.session.add(new_club)
    db.session.commit()
    return jsonify({
        "id": new_club.id,
        "code": new_club.code,
        "name": new_club.name,
        "description": new_club.description,
        "tags": new_club.tags
    }), 201

@app.route("/api/clubs/<int:club_id>/favorite", methods=["POST"])
def favorite_club(club_id):
    club = Club.query.get(club_id)
    if not club:
        return jsonify({"error": "Club not found"}), 404

    club.favorite_count += 1
    db.session.commit()
    return jsonify({
        "id": club.id,
        "name": club.name,
        "favorite_count": club.favorite_count
    })

@app.route("/api/clubs/<int:club_id>", methods=["PUT"])
def modify_club(club_id):
    club = Club.query.get(club_id)
    if not club:
        return jsonify({"error": "Club not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    club.name = data.get("name", club.name)
    club.description = data.get("description", club.description)
    club.tags = data.get("tags", club.tags)
    db.session.commit()
    return jsonify({
        "id": club.id,
        "code": club.code,
        "name": club.name,
        "description": club.description,
        "tags": club.tags
    })

@app.route("/api/tags", methods=["GET"])
def get_tags():
    clubs = Club.query.all()
    tag_counts = defaultdict(int)
    for club in clubs:
        for tag in club.tags:
            tag_counts[tag] += 1
    return jsonify(tag_counts)

if __name__ == "__main__":
    app.run()
