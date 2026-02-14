from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    return jsonify({
        "SERVER": "TEST_SERVER_RUNNING",
        "precautions": [
            "This is a test precaution",
            "If you see this, Flask is running THIS file"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
