from django.db import models 
from research_facilities.models import research_facility

class medicine (models.Model):
    name = models.CharField(max_length=70, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=1,null=False)
    research_facility = models.ForeignKey(research_facility, on_delete=models.CASCADE, related_name='medicines')

    def __str__(self) -> str:
        return self.name