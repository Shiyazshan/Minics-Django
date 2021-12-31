from django.db import models


class About(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='product',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


