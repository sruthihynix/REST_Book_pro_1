from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=200)
    book_year=models.IntegerField()

    class Meta:
        db_table="table_book"
