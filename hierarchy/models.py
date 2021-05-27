from django.db import models

class AppModel(models.Model):
    '''Model having a foreign key relationship with itself'''

    title = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.parent}'
    
    class Meta:
        verbose_name = 'Model'