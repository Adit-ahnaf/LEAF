from django.contrib import admin
from .models import Book
# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
	list_display = ["title"]
	search_fields = ["title"]
class Meta:
	model = Book


admin.site.register(Book, BookModelAdmin)