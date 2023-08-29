from django.db import models

# data table for search logo
class SearchLogo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=10)
    logo_number = models.IntegerField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='logo')


    def __str__(self):
        return self.title
