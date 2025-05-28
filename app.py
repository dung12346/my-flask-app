from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "✅ Flask app chạy trên Render bằng gunicorn!"

if __name__ == '__main__':
    # Chỉ chạy local test
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
