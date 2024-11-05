from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name='노래 제목')
    artist = models.CharField(max_length=100, verbose_name='가수')
    lowest_note = models.CharField(max_length=3, verbose_name='최저음')  # 예: 'C3'
    highest_note = models.CharField(max_length=3, verbose_name='최고음')  # 예: 'G4'
    
    class Meta:
        verbose_name = '노래'
        verbose_name_plural = '노래들'
        
    def __str__(self):
        return f"{self.title} - {self.artist}"