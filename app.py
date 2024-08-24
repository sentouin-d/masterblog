#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('mock.json') as mock_data:
        blog_posts = json.load(mock_data)

    return render_template('index.html', posts=blog_posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        pass

    return render_template("add.html")