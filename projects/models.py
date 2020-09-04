from django.db import models

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    tools = models.ManyToManyField('Tool', related_name='project')
    cover = models.ImageField(null=True, blank=True, upload_to="img/")
    githubLink = models.CharField(max_length=255)
    demoLink = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.title
