from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import os
from worksheets.storage import OverwriteStorage

# Create your models here.
class Worksheet(models.Model):
	name = models.CharField(max_length=100)
	file = models.FileField(max_length=100, storage=OverwriteStorage(), upload_to = 'worksheets/')
	isSolution = models.BooleanField()
	worksheetNumber = models.IntegerField()
	variablesAndFunctions = models.BooleanField() 
	controls = models.BooleanField()
	wwpd = models.BooleanField()
	environmentDiagrams = models.BooleanField()
	higherOrderFunctions = models.BooleanField()
	lambdaExpressions = models.BooleanField()
	recursion = models.BooleanField()
	treeRecursion = models.BooleanField()
	dataAbstraction = models.BooleanField()
	ordersOfGrowth = models.BooleanField()
	pythonLists = models.BooleanField()
	linkedLists = models.BooleanField()
	mutableTrees = models.BooleanField()
	nonloc = models.BooleanField()
	oop = models.BooleanField()
	scheme = models.BooleanField()
	schemeLists = models.BooleanField()
	tailRecursion = models.BooleanField()
	interpreters = models.BooleanField()
	macros = models.BooleanField()
	iteratorsAndGenerators = models.BooleanField()
	streams = models.BooleanField()
	sequel = models.BooleanField()
	midterm1 = models.BooleanField()
	midterm2 = models.BooleanField()
	final = models.BooleanField()

	def __str__(self):
		return self.name