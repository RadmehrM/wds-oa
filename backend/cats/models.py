from django.db import models

class CatImage(models.Model):
    image = models.BinaryField()
    description = models.TextField()

    def __str__(self):
        return self.description[:50]
