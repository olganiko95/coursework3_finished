import json
from json import JSONDecodeError
from exceptions.exceptions import DataSourseError
from posts.main.comment import Comment


class Comment_main:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)

        except(FileNotFoundError, JSONDecodeError):
            raise DataSourseError(f'Не удается получить данные из файла {self.path}')

        return posts_data

    def _load_comments(self):
        comments_data = self._load_data()
        list_of_posts = [Comment(**comment_data) for comment_data in comments_data]
        return list_of_posts

    def get_comments_by_post_pk(self, post_pk):
        comments = self._load_comments()
        comments_match = [c for c in comments if c.post_id == post_pk]
        return comments_match

