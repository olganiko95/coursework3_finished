from flask import Blueprint, jsonify
from werkzeug.exceptions import abort

from config import DATA_PATH_POST, DATA_PATH_COMMENTS
from posts.main.comment_main import Comment_main
from posts.main.post_main import Post_main
from posts.main.post import Post
import logging

bp_api = Blueprint('bp_api', __name__)

post_main = Post_main(DATA_PATH_POST)
comments_main = Comment_main(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")

@bp_api.route('/')
def api_posts_hello():
    return 'Попроси у меня документацию'


@bp_api.route('/posts/')
def api_posts_all():
    all_posts = post_main.get_all()
    api_logger.debug('Запрошены все посты')
    return jsonify([post.as_dict() for post in all_posts]), 200

@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk):
    post = post_main.get_by_pk(pk)

    if post is None:
        api_logger.debug('Обращение к несуществующему посту')
        abort(404)
    api_logger.debug(f'Обращение к посту {pk}')
    return jsonify(post.as_dict()), 200

