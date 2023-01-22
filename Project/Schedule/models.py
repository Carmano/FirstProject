from django.db import models


class Schedule(models.Model):
    pass


class Teacher(models.Model):
    full_name = models.CharField(max_length='64')


class Office(models.Model):
    office_kod = models.IntegerField()
    corpus = models.IntegerField()


class Discipline(models.Model):
    name_discipline = models.CharField(max_length="64")


class LessonType(models.Model):
    type_lesson = models.CharField(max_length='24')


