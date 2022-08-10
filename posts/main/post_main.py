from posts.main.post import Post
import json
from json import JSONDecodeError
from exceptions.exceptions import DataSourseError


class Post_main:

    def __init__(self, path):
        self.path = path

    def _load(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourseError(f'Не удается получить данные из файла {self.path}')

        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    def get_all(self):
        posts = self._load()
        return posts

    def get_by_pk(self, pk):

        if type(pk) != int:
            raise TypeError('pk должно быть целым числом!')

        posts = self.get_all()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):

        substring = str(substring)
        posts = self.get_all()
        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts

    def get_by_poster(self, username):

        username = str(username).lower()
        posts = self.get_all()
        matching_posts = [post for post in posts if post.poster_name.lower() == username]
        return matching_posts


