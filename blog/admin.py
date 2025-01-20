from django.contrib import admin

from .models import Recipe, About



@admin.register(About)

class AboutAdmin(admin.ModelAdmin):

    list_display = ('title',)



@admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'cooking_time', 'serving', 'created_at')

    list_filter = ('created_at',)

    search_fields = ('title', 'description') 
