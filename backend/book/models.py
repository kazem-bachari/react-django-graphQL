from django.db import models

# Create your models here.


class Categorize(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Categorize,  on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.title
