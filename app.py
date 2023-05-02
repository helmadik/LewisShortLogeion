from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.config['SECRET_KEY'] = "abc"
"""
@app.route("/")
def home():
    return "Convert your Plautus Act Scene Lines!"""

if __name__ == '__main__':
    app.run(debug=True)