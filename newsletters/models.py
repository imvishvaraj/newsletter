from django.db import models


class NewsletterUser(models.Model):
    email       = models.EmailField(primary_key=True)
    date_added  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
