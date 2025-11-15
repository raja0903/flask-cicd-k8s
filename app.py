from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter("flask_requests_total", "Total HTTP requests")

@app.route("/")
def hello():
    REQUESTS.inc()
    return "🚀 Flask CI/CD on Kubernetes Works!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

