from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True,
                             on_delete=models.SET_NULL, related_name='comments')
    text = models.TextField()


    def __str__(self):
        return self.text