import pytest
from posts.main.post import Post
from posts.main.post_main import Post_main


def check_fields(post):
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

    for field in fields:
        assert hasattr(post, field), f'Нет поля {field}'

class TestPostsMain:

    @pytest.fixture
    def post_main(self):
        post_main_instance = Post_main('post_test_js.json')
        return post_main_instance

    #Функция получения всех постов

    def test_get_all_types(self, post_main):

        posts = post_main.get_all()
        assert type(posts) == list, 'Incorrect type for result'

        posts = post_main.get_all()[0]
        assert type(posts) == Post, 'Incorrect type for single item'

    def test_get_all_fields(self, post_main):

        posts = post_main.get_all()
        post = post_main.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_main):
        posts = post_main.get_all()
        correct_pks = [1, 2, 3]
        pks = [post.pk for post in posts]
        assert pks == correct_pks, 'Не совпадают полученные id'

    #Функция получения по pk

    def test_get_by_pk_types(self, post_main):
        post = post_main.get_by_pk(1)
        assert type(post) == Post, 'Incorrect type for single item'

    def test_get_by_pk_fields(self, post_main):
        post = post_main.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_main):
        post = post_main.get_by_pk(999)
        assert post is None, 'Should be None for not existing pk'

    @pytest.mark.parametrize('pk', [1,2,3])
    def test_get_by_pk_correct_id(self, post_main, pk):
        post = post_main.get_by_pk(pk)
        assert post.pk == pk, f'Incorrest pk for requested post with pk = {pk}'

    # Функция поиска по вхождению
    def test_search_in_content_types(self, post_main):
        posts = post_main.search_in_content('ага')
        assert type(posts) == list, 'Incorrect type for result'
        post = post_main.get_all()[0]
        assert type(post) == Post, 'Incorrect type for single item'

    def test_search_in_content_fields(self, post_main):
        posts = post_main.search_in_content('ага')
        post = post_main.get_all()[0]
        check_fields(post)

    def test_search_in_content_not_found(self, post_main):
        posts = post_main.search_in_content('98657')
        assert posts == [], 'Shoulf be [] for not existing substring'

    @pytest.mark.parametrize("s, expected_pks)", [
        ('Ага', {1}),
        ('Вышел', {2}),
        ('на', {1, 2, 3}),

    ])
    def test_search_in_content_results(self, post_main, s, expected_pks):
        posts = post_main.search_in_content(s)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f'Incorrect results for {s}'

    # Функция поиска по автору

    def test_get_by_poster_types(self, post_main):
        posts = post_main.get_by_poster('hank')
        assert type(posts) == list, 'Incorrect type for result'

        post = post_main.get_all()[0]
        assert type(post) == Post, 'Incorrect type for single item'

    def test_get_by_poster_fields(self, post_main):
        posts = post_main.get_by_poster('leo')
        post = post_main.get_all()[0]
        check_fields(post)

    def test_get_by_poster_not_found(self, post_main):
        posts = post_main.get_by_poster('dfdsf')
        assert posts == [], 'Shoulf be [] for not existing substring'

    @pytest.mark.parametrize("poster, expected_pks", [
            ('leo', {1}),
            ('johnny', {2}),
            ('hank', {3}),

        ])
    def test_get_by_poster_results(self, post_main, poster, expected_pks):
            posts = post_main.get_by_poster(poster)
            pks = set([post.pk for post in posts])
            assert pks == expected_pks, f'Incorrect results for {poster}'

