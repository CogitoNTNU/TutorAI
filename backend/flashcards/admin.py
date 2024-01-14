from django.contrib import admin

from flashcards.models import Flashcard, Cardset

# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Cardset)