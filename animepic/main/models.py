from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Character(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Name of the character')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL of the character")
    anime = models.CharField(max_length=255, blank=True, verbose_name='Name of Anime')
    content = models.TextField(verbose_name='content')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_upload = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='is published?')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Anime Character'
        verbose_name_plural = 'Anime Characters'
        ordering = ['-time_create', 'name']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL of the category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']