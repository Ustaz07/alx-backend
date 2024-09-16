#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configure Babel with available languages and default locale
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

# Initialize Babel
babel = Babel(app)

# Locale selector function


@babel.localeselector
def get_locale():
    # Get the best match from the request's Accept-Language headers
    return request.accept_languages.best_match(
            app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
