from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Articls(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="images/", blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
