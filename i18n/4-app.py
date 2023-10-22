#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, request, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config translate
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""config app"""


@babel.localeselector
def get_locale():
    """
    get local lang
    """
    local_lang = request.args.get("locale")
    supp_lang = app.config["LANGUAGES"]
    if local_lang in supp_lang:
        return local_lang
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    """
    hello world
    """
    return render_template("4-index.html")
