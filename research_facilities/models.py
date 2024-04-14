from django.db import models

class research_facility (models.Model):
    name = models.CharField(max_length=70, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name