from flask_blog import create_app, db
from flask_blog.models import User, Post

app = create_app()


@app.shell_context_processor
def make_shell_processor():
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run
