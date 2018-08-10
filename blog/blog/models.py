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
    active = models.BooleanField(default=True,      # Показать/Скрыть тему
                                 blank=True,
                                 verbose_name="Отображать тему и связанные посты в блоге"
                                 )

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Theme"
        # verbose_name_plural = ""
