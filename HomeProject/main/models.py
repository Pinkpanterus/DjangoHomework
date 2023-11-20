from django.db import models

# Create your models here.
class News:
    def __init__(self, title, text, author, date, category):
        self.title = title
        self.text = text
        self.author = author
        self.date = date
        self.category = category
