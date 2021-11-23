from flask import Flask, render_template, request, url_for, redirect, session, jsonify, flash, g

import sqlite3

from werkzeug.wrappers import response
app = Flask(__name__)

from db import get_posts, add_post

DATABASE = './database/database.sqlite3'

# STARTUP, EXCEPTION HANDLING
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def aquire_db():
    db = getattr(g, '_database', None)
    if db is None:
        try:
            db = g._database = sqlite3.connect(DATABASE)
        except:
            open("./data/database.sqlite3", "a").close()
    return db

# ROUTES
@app.route('/posts/new', methods=['POST'])
def new_post():
    req = request.get_json()
    
    print(req)


    # title = req.title
    # content = req.content
    # image = req.image
    # author = req.author

    # if (title and content):
    #     post = (title, content, image, author)

    #     cur = aquire_db().cursor()
    #     add_post(cur, ())
        
    
@app.route('/', methods=['GET'])
def index_page():
    cur = aquire_db().cursor()
    print(get_posts(cur))

    return render_template('index.html')

# MULTITHREADING LOGIC
if __name__ == '__main__':
    app.run(debug=True)