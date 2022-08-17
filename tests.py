import pytest

from main import app

class TestAPI:
    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    def test_app_all_posts_status_code(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_all_posts_have_correct_keys(self):
        result = app.test_client().get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        assert post.keys() == self.post_keys, 'Неправильные ключи у полученного словаря'

    def test_app_single_post_has_correct_status(self):
        result = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200, "Статус код запроса одного поста неверный"
        assert result.mimetype == "application/json", "Получен не JSON"

    def test_app_single_post_non_existenst(self):
        result = app.test_client().get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_app_single_post_has_correct_keys(self):
        result = app.test_client().get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = post.keys()
        assert post_keys == self.post_keys

    @pytest.mark.parametrize("pk", [(1), (2), (3), (4)])
    def test_app_single_post_has_correct_data(self, pk):
        result = app.test_client().get(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()

        assert post['pk'] == pk, f'Неправильный pk при запросе поста {pk}'
