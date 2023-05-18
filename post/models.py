from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Post(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.title} | " \
               f"Average of upvotes: {self.body[:20]} | " \
               f"PostID: {self.id}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Upvote(models.Model):
    user = models.ForeignKey(User,
                             related_name='upvotes',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='upvotes',
                             on_delete=models.CASCADE)
    points = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(5)))

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} has given {self.points} points to {self.post.title} and postID is: {self.post.id}"
