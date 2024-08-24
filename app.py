#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, flash, url_for
import json
import uuid

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    with open('mock.json', 'r', encoding='utf-8') as mock_data:
        blog_posts = json.load(mock_data)

    return render_template('index.html', posts=blog_posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        error = None

        if not (author or title):
            error = 'Missing author or title'

        if error is not None:
            flash(error)
        else:
            with open('mock.json', 'r', encoding='utf-8') as mock_data:
                blog_posts = json.load(mock_data)
                new_post = {
                    "id": str(uuid.uuid4()),
                    "author": author,
                    "title": title,
                    "content": content
                }
                blog_posts.append(new_post)

                with open('mock.json', 'w', encoding='utf-8') as mock_write:
                    updated_posts = json.dumps(blog_posts)
                    mock_write.write(updated_posts)

            return redirect(url_for('index'))

    return render_template("add.html")