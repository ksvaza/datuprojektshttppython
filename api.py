from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/sensor/data", methods=["POST"])
def processData():
    data = request.get_json()
    if not data:
        print("err")
        return jsonify({"error": "Invalid"}), 400
    light = data.get("light", 0.0)
    temperature = data.get("temperature", 0.0)
    print(f"light {light}")
    print(f"temperature {temperature}")
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


