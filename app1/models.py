
from ast import alias
from decimal import Decimal
from locale import currency
from unicodedata import decimal
from django.db import models

class Stockgroup(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.ForeignKey(listofgroups,on_delete=models.CASCADE,blank=False)


class Unit(models.Model):
    type=models.Foreginkey(type,on_delete=models.CASCADE,blank=False)
    symbol=models.CharField(max_length=225)
    foramlname=models.CharField(max_length=225)
    unitcode=models.CharField(max_length=225)
    decimal=models.IntegerField()

class godown(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharFiled(max_length=225)
    models.ForeignKey(godown,on_delete=models.CASCADE,blank=False)

class StockCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.ForeignKey(StockCategory,on_delete=models.CASCADE,blank=False)