from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)   # GET request
    all_posts = response.json()  # transform the data we get into JSON
    return render_template("index.html", posts=all_posts)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)  # GET request
    all_posts = response.json()  # transform the data we get into JSON
    # post_id = int(blog_id) - 1
    # blog_post = all_posts[post_id]
    return render_template('post.html', posts=all_posts, num=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
