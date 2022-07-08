
from ast import alias

from django.db import models

class Stockgroup(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)


class Unit(models.Model):
    type=models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    foramlname=models.CharField(max_length=225)
    unitcode=models.CharField(max_length=225)
    decimal=models.IntegerField()

class Godowns(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    godown=models.CharField(max_length=225)

class StockCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)

