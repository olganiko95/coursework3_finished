class Post():
    def __init__(self, pk=0, poster_name='', poster_avatar='', pic='', content='', views_count=0, likes_count=0):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count

    def __repr__(self):
        return f"Post({self.pk}, {self.poster_name}, {self.poster_avatar}, {self.pic}, {self.content}, {self.views_count}, {self.likes_count})"

    def as_dict(self):
        dict_data = {

            "pk": self.pk,
            "poster_name": self.poster_name,
            "poster_avatar": self.poster_avatar,
            "pic": self.pic,
            "content": self.content,
            "views_count": self.views_count,
            "likes_count": self.likes_count

        }
        return dict_data



