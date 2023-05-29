from django.db import models


class Users(models.Model):
    username = models.CharField('Имя', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    date_joined = models.DateField('Дата регистрации', default='2021-12-12')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f'/posts/user/{self.id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Posts(models.Model):
    author_id = models.ForeignKey(Users, verbose_name='Автор', on_delete=models.CASCADE)
    post = models.TextField('Пост')
    like = models.IntegerField('Кол-во лайков')
    date_created = models.DateField('Дата написания', default='2021-12-12')

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return f'/posts/post/{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Likes(models.Model):
    post = models.ForeignKey(Posts, verbose_name='Пост', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Пользователь', on_delete=models.CASCADE)
    date_like = models.DateField('Дата постановки', default='2021-12-12')

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        return f'/posts/like/{self.id}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Subscribes(models.Model):
    follower = models.ForeignKey(Users, verbose_name='Подписчик', related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(Users, verbose_name='Блогер', related_name='following', on_delete=models.CASCADE)
    date_follow = models.DateField('Дата подписки', default='2021-12-12')

    def __str__(self):
        return str(self.follower)

    def get_absolute_url(self):
        return f'/posts/subscribe/{self.id}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Images(models.Model):
    post = models.OneToOneField(Posts, verbose_name='Пост', on_delete=models.CASCADE)
    image = models.TextField('Ссылка на картинку')

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        return f'/posts/image/{self.id}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


