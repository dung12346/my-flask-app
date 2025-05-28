from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Chào mừng đến với Flask trên Render!"

if __name__ == '__main__':
    app.run()
