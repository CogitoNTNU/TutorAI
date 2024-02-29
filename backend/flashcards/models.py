from django.db import models

# Create your models here.

class Flashcard(models.Model):
    """Model to store flashcards"""
    id = models.AutoField(primary_key=True)
    front = models.TextField(help_text="The front of the flashcard")
    back = models.TextField(help_text="The back of the flashcard")
    cardset = models.ForeignKey(
        "Cardset", on_delete=models.CASCADE, help_text="The cardset to which the flashcard belongs"
    )

    def __str__(self):
        return self.front

class Cardset(models.Model):
    """Model to store cardsets"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="The name of the cardset")
    description = models.TextField(help_text="The description of the cardset")
   

    def __str__(self):
        return self.name