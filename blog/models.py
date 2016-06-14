from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    summary = models.TextField(blank=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Core(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    picture = models.ImageField(upload_to='profiles', blank=True)

    def __str__(self):
        return self.name

class Servant(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    picture = models.ImageField(upload_to='profiles', blank=True)

    def __str__(self):
        return self.name

class Praise(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    picture = models.ImageField(upload_to='profiles', blank=True)

    def __str__(self):
        return self.name

class Sermon(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    audio = models.FileField(upload_to='sermons')

    def __str__(self):
        return self.name