from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root"),
        database=os.getenv("MYSQL_DB", "devops")
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/db-test")
def db_test():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"MySQL connected successfully! Version: {version[0]}"

    except Exception as e:
        return f"MySQL connection failed: {str(e)}", 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )