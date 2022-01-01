from django.db import models


class Welcome(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='web',blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
        

class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to="web",blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]