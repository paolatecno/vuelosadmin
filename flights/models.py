# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class Aeropuerto(models.Model):
	codigo = models.CharField(primary_key=True, max_length=20)
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return "%s %s" % (self.nombre, self.codigo)


class Vuelo(models.Model):
	numero = models.CharField(primary_key=True, max_length=20)
	fecha = models.DateTimeField('Salida')
	hora_salida = models.TimeField()
	hora_llegada = models.TimeField()
	hora_embarque = models.TimeField()
	numero_embarque = models.CharField(max_length=20)
	precio = models.IntegerField(default=0)
	origen = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
	destino = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='destino_of')

	def __str__(self):
		return "%s / Desde %s - hasta - %s" % (self.numero, self.origen, self.destino)


class Ticket_cliente(models.Model):
	numero_ticket = models.CharField(primary_key=True, max_length=200)
	ci = models.CharField(max_length=50)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	asiento = models.CharField(max_length=10)
	vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)

	def __str__(self):
		return "%s %s %s" % (self.numero_ticket, self.nombre, self.apellido)
