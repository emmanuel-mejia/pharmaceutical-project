from django.db import models
from research_facilities.models import ResearchFacility

class Medicine (models.Model):
    name = models.CharField(max_length=70, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=1,null=False)
    research_facility = models.ForeignKey(ResearchFacility, on_delete=models.CASCADE, related_name='medicines')

    @property
    def price_format(self):
        return f'${self.price}.00'
        #return f'${self.price / 100}.00'

    def __str__(self) -> str:
        return self.name