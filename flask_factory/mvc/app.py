from flask import Flask
from view import user_info

app = Flask(__name__)
app.register_blueprint(user_info, url_prefix='/user_info')


@app.errorhandler(404)  # 없는 페이지를 요청했을 때의 에러
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

