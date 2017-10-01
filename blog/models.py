from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    YEAR_CHOICES = (('1', 'Zeroth-year'), ('2', 'Pre-pre-final-year'), ('3', 'Pre-final-year'), ('4', 'Final-year'))
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20, choices=YEAR_CHOICES, default='1')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.pk})


class Comment(models.Model):
    YEAR_CHOICES = (('1', 'Zeroth-year'), ('2', 'Pre-pre-final-year'), ('3', 'Pre-final-year'), ('4', 'Final-year'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20, choices=YEAR_CHOICES, default='1')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return 'Comment by ' + str(self.author) + 'on ' + str(self.publish)
