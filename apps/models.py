from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a title for the project')
    description = models.TextField()
    link = models.URLField()

    def __str__():
        return f'{self.name}\n\n{self.description}'

class Photo(models.Model):
    PEOPLE = 'PE'
    LANDSCAPE = 'LA'
    CLOSE_UP = 'CL'
    MISC = 'MS'

    YEAR_IN_SCHOOL_CHOICES = (
        (PEOPLE, 'People'),
        (LANDSCAPE, 'Landscape'),
        (CLOSE_UP, 'Close-up'),
        (MISC, 'Misc')
    )
    
    name = models.CharField(max_length=200, help_text='Enter a title for the project')
    description = models.TextField()
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=MISC,
    )

    def __str__():
        return f'{self.name}({self.year_in_school})' 