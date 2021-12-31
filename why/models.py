from django.db import models


class WhyUs(models.Model):
    image = models.ImageField(upload_to='why',blank=True,null=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]