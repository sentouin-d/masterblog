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
        blog_posts = json.load(mock_data).values()

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
                post_id = str(uuid.uuid4())
                new_post = {
                    "author": author,
                    "title": title,
                    "content": content
                }
                blog_posts[post_id] = new_post

                with open('mock.json', 'w', encoding='utf-8') as mock_write:
                    mock_write.write(json.dumps(blog_posts))

            return redirect(url_for('index'))

    return render_template("add.html")

@app.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    post = {}
    blog_posts = {}

    with open('mock.json', 'r', encoding='utf-8') as mock_data:
        blog_posts = json.load(mock_data)
        post = blog_posts[id]

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
            updated_post = {
                "author": author,
                "title": title,
                "content": content
            }
            blog_posts[id] = updated_post

            with open('mock.json', 'w', encoding='utf-8') as mock_write:
                mock_write.write(json.dumps(blog_posts))
            
            return redirect(url_for('index'))

    return render_template("update.html", post=post, post_id=id)

@app.route("/delete/<string:id>", methods=["POST",])
def delete(id):
    with open('mock.json', 'r', encoding='utf-8') as mock_data:
        blog_posts = json.load(mock_data)
        del blog_posts[id]

        with open('mock.json', 'w', encoding='utf-8') as mock_write:
            mock_write.write(json.dumps(blog_posts))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()