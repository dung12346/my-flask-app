from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Xin chào từ Flask trên Render!</h1>'

@app.route('/api')
def api():
    return {'message': 'API Flask hoạt động rồi nè'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # cổng 10000 là để test local, Render sẽ override bằng PORT
