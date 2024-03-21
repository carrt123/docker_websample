from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello You!"


@app.route('/docker')
def docker_test():
    return "This is a docker test"


if __name__ == '__main__':
    app.run()