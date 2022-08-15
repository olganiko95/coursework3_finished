import main
import pytest
import os

class TestApi:

    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        app.config['DATA_PATH_POST'] = os.path.join('posts', 'tests', 'posts_test_js.json')
        test_client = app.test_client()
        return test_client

    def test_all_posts_have_correct_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    def test_all_posts_have_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()

        assert post.keys() == self.post_keys, 'Неправильные ключи у полученного словаря'

    def test_single_post_has_correct_status(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_single_post_non_existenst(self, app_instance):
        result = app_instance.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_single_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = post.keys()
        assert post_keys == self.post_keys

    @pytest.mark.parametrize("pk", [(1), (2), (3), (4)])
    def test_single_post_has_correct_data(self, app_instance, pk):
        result = app_instance.get(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()

        assert post['pk'] == pk, f'Неправильный pk при запросе поста {pk}'


