from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:beproductive@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    post_content = db.Column(db.String(400))

    def __init__(self, title):
        self.title = title
        self.completed = False


@app.route('/blog', methods=['POST', 'GET'])
def blog():

    if request.method == 'POST':
        blog_title = request.form['blog-title']
        new_task = Task(task_name)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.filter_by(completed=False).all()
    completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('new-post.html',title="build-a-blog", 
        tasks=tasks, completed_tasks=completed_tasks)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    task_id = request.form['task-id']
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/new-post')


if __name__ == '__main__':
    app.run()