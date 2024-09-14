#!/usr/bin/env python3
"""
Basic Flask app with a single route.
Displays 'Welcome to Holberton' as the page title.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the index page with a title and a header"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
