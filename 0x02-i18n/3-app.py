#!/usr/bin/env python3
"""A Flask app with i18n support and parametrized templates.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Select the best language match for the user."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def index():
    """Render the home page."""
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
