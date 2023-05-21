from flask import Flask

app = Flask(__name__)   # app이라는 이름을 가진 Flask 클래스의 객체 생성

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()