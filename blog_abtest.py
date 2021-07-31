from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
import os

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'dave_server'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


# @login_manager.user_loader
# def login_user(user_id):
#     return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return make_response(jsonify(success=False), 401)


@app.route('/')
def hello_world():
    return 'Hello Worl1d!'


@app.route('/')
def html_test():
    name = "Hoge"
    # return name
    print("test")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
    #app.run()
