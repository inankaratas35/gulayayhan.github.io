from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    image = models.ImageField(upload_to='about/', verbose_name="Profil Fotoğrafı")
    
    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tarif Adı")
    description = models.TextField(verbose_name="Kısa Açıklama")
    ingredients = RichTextField(verbose_name="Malzemeler")
    instructions = RichTextField(verbose_name="Hazırlanışı")
    cooking_time = models.CharField(max_length=50, verbose_name="Pişirme Süresi")
    serving = models.CharField(max_length=50, verbose_name="Kaç Kişilik")
    image = models.ImageField(upload_to='recipes/', verbose_name="Yemek Fotoğrafı")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title