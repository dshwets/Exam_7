from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=250, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return '{}. {}'.format(self.pk, self.question)


class Choice(models.Model):
    text = models.TextField(max_length=250, verbose_name='Текст варианта')
    poll_choice = models.ForeignKey('webapp.Poll', related_name='choices',
                                    on_delete=models.CASCADE, verbose_name='Опрос')


class Answer(models.Model):
    pool = models.ForeignKey('webapp.Poll', related_name='answers',on_delete=models.CASCADE, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    choice = models.ForeignKey('webapp.Choice', related_name='answers', on_delete=models.CASCADE, verbose_name='Вариант ответа')