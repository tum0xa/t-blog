from django.db import models


class Theme(models.Model):

    """
    Class Theme
    Темы постов
    """

    name = models.CharField(default='UnknownTheme', # Название темы
                            max_length=255,
                            unique=True,
                            blank=False
                            )
    active = models.BooleanField(default=True,      # Показать/Скрыть тему
                                 blank=True,
                                 )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тему"
        verbose_name_plural = "темы"
