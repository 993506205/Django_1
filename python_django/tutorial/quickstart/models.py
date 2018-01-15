# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	bookName = models.CharField(max_length=45)
	authors = models.CharField(max_length=100)
	price = models.CharField(max_length=10)
	publish_date = models.DateField()
	
	def __str__(self):
		return self.bookName
