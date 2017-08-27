from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:07131989j@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(400))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    blogs = Blog.query.all()
    blog_id = request.args.get('id')
    if request.method == 'POST':
        blog_title = request.form['new_post_title']
        blog_body = request.form['new_post_body']
        if blog_title == '' or blog_body == '':
            return redirect('/new_post', code=307)
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()
        blogs = Blog.query.all()
        return render_template('blog.html',
        base_title="build-a-blog",
        blogs=blogs)

    if blog_id:
        single_blog = Blog.query.filter_by(id=blog_id).first()
        return render_template('single_blog.html',
        base_title="build-a-blog",
        single_blog=single_blog)

    else:
        return render_template('blog.html',
            base_title="build-a-blog",
            blogs=blogs)


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    title_head = 'Add Blog Post'
    if request.method == 'POST':
        # title = request.form['new_post_title']
        # body = request.form['new_post_body']
        # if title and body:
        #     new_blog = Blog(title, body)
        #     db.session.add(new_blog)
        #     db.session.commit()
        #     return redirect('/blog?id={0}'.format(new_blog.id))
        # if title == '' or body == '':
        title_error = "Please enter a blog title"
        body_error = "Please enter a blog description"
        return render_template('new_post.html', title_error=title_error, body_error=body_error)
        
        # return redirect('/new_post')
    else:
        return render_template('new_post.html', title="Build-A-Blog")


if __name__ == '__main__':
    app.run()