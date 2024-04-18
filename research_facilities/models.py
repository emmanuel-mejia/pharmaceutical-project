from django.db import models

class ResearchFacility (models.Model):
    name = models.CharField(max_length=70, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name