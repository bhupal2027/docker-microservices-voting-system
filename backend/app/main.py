from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/")
def home():
    return jsonify({"msg": "Backend running"})

@app.route("/api/vote", methods=["POST"])
def vote():
    data = request.json
    animal = data.get("animal")

    if animal not in ["cat", "dog"]:
        return jsonify({"error": "invalid vote"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO votes (animal) VALUES (%s)", (animal,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "success", "animal": animal})

@app.route("/api/votes")
def get_votes():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT animal, COUNT(*) FROM votes GROUP BY animal;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = {"cat": 0, "dog": 0}
    for animal, count in rows:
        result[animal] = count

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
