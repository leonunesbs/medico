from django.db import models

# importing slugify from django
from django.utils import text, timezone


class Article(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=1, choices=[
                              ('d', 'draft'), ('p', 'published')])
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True, related_name='articles')

    author = models.ForeignKey(
        'colaboradores.Colaborador', on_delete=models.SET_NULL, blank=True, null=True, related_name='author')

    published_at = models.DateTimeField(auto_now_add=True)

    last_update = models.DateTimeField()
    last_update_by = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        self.last_update = timezone.now()
        super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.name)
        super(Category, self).save(*args, **kwargs)
