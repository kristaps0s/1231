def get_posts(cur):
    try:
        cur.execute('''SELECT * FROM posts''')
        rows = cur.fetchall()
        return rows
    except:
        cur.execute('''
            CREATE TABLE posts (
                title TEXT,
                content TEXT,
                image TEXT,
                author TEXT
            );
        ''')

def add_post(cur, post1):

    post = ("title", "content", "image", "author")

    cur.execute('''
        INSERT INTO posts(title, content, image, author) VALUES(?, ?, ?, ?)
    ''', post)