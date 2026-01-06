from flask import Flask, request, jsonify, render_template
import json, subprocess, os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("flipkart.html")  # loads templates/flipkart.html

@app.route("/log", methods=["POST"])
def log_action():
    data = request.get_json()
    log_entry = json.dumps(data)

    # Save locally
    os.makedirs("logs", exist_ok=True)
    with open("logs/user_logs.json", "a") as f:
        f.write(log_entry + "\n")

    # Try to append to HDFS (optional)
    try:
        subprocess.run(
            ["hdfs", "dfs", "-appendToFile", "-", "/ecom_logs/user_logs.json"],
            input=log_entry.encode(),
            check=True
        )
        print(f"✅ Logged to HDFS: {log_entry}")
    except Exception as e:
        print(f"⚠️ HDFS append failed: {e}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    print("✅ E-commerce Tracking Backend Running on http://127.0.0.1:5000/")
    app.run(debug=True)
