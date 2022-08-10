import logging

from flask import Flask, Blueprint, render_template, current_app, request
from werkzeug.exceptions import abort

from config import DATA_PATH_POST, DATA_PATH_COMMENTS
from posts.main.comment_main import Comment_main
from posts.main.post_main import Post_main

posts = Blueprint('post_main', __name__, template_folder='templates')

post_main = Post_main(DATA_PATH_POST)
comments_main = Comment_main(DATA_PATH_COMMENTS)


@posts.route('/')
def page_posts_index():
    all_posts = post_main.get_all()
    return render_template('index.html', posts=all_posts)

@posts.route('/posts/<int:pk>/')
def page_posts_single(pk):
    post = post_main.get_by_pk(pk)
    comments = comments_main.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)

    return render_template('post.html', post=post, comments=comments)

@posts.route('/users/<poster_name>/')
def page_posts_by_user(poster_name):
    posts = post_main.get_by_poster(poster_name)

    if not posts:
        abort(404, 'Извините, нет такого пользователя')
    return render_template('user-feed.html', posts=posts, poster_name=poster_name)

@posts.route('/search/')
def page_posts_search():
    query = request.args.get('s', '')
    if query == '':
        posts = []
    else:
        posts = post_main.search_in_content(query)
    return render_template('search.html', posts=posts, query=query, posts_len=len(posts))