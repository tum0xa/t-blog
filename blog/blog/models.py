from django.db import models


class Theme(models.Model):

    """
    Class Theme
    Темы постов
    """

    name = models.CharField(default='UnknownTheme', # Название темы
                            max_length=255,
                            unique=True,
                            blank=False,
                            verbose_name="Название темы"
                            )
    slug = models.SlugField(default='unknowntheme',
                            max_length=64,
                            blank=False,
                            verbose_name="Относительный url-адрес"
                            )
    active = models.BooleanField(default=True,      # Показать/Скрыть тему
                                 blank=True,
                                 verbose_name="Отображать тему и связанные посты в блоге"
                                 )
    short_description = models.TextField(default='Short description of the theme',
                                   unique=False,
                                   blank=True,
                                   verbose_name="Короткое описание темы"
                                         )

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Theme"
        # verbose_name_plural = ""


class Post(models.Model):
    """
    Class Post
    Публикация
    """

    title = models.CharField(default="Unknown Post",
                             max_length=255,
                             blank=False,
                             unique=True,
                             verbose_name="Заголовок публикации"
                             )
    slug = models.SlugField(default="unknownpost",
                            max_length=128,
                            blank=False,
                            verbose_name="Относительный url-адрес")
    content = models.TextField(default="Some text of post",
                               blank=False,
                               verbose_name="Содержимое публикации")
    # TODO Add theme
    # TODO Add author
    publication_date = models.DateField(auto_now_add=True,
                                        verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Post"
        # verbose_name_plural = ""
