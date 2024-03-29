from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from config.utils import (upload_university_logo_path,
                          upload_university_cover_path,
                          upload_course_cover_path,
                          upload_subject_cover_path,
                          unique_slug_generator,)


class University(models.Model):

    # Fields
    name = models.CharField(max_length=128)
    university_code = models.CharField(max_length=8)
    description = models.TextField()
    founded = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to=upload_university_logo_path,
                             null=True, blank=True)
    cover = models.ImageField(
        upload_to=upload_university_cover_path, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "universities"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('universities_university_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('universities_university_update', args=(self.pk,))


class Course(models.Model):

    # Choices
    COURSE_TYPE_CHOICES = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
    )
    DEGREE_TYPE_CHOICES = (
        ('be', 'Bachelor of Engineering'),
        ('btech', 'Bachelor of Technology'),
    )

    # Fields
    name = models.CharField(max_length=128)
    course_type = models.CharField(max_length=12, choices=COURSE_TYPE_CHOICES)
    degree_type = models.CharField(max_length=32, choices=DEGREE_TYPE_CHOICES)
    years = models.IntegerField()
    description = models.TextField()
    course_code = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True)
    cover = models.ImageField(upload_to=upload_course_cover_path,
                              null=True, blank=True)

    # Relationship Fields
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if len(self.course_code.split('-')) > 1:
            self.course_code = self.course_code.split('-')[1]
        self.course_code = '{}-{}'.format(
            self.university.university_code,
            self.course_code
            )
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name+"-"+self.university.university_code

    def get_absolute_url(self):
        return reverse('universities_course_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('universities_course_update', args=(self.slug,))


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(course_pre_save_receiver, sender=Course)


class Subject(models.Model):

    # Fields
    name = models.CharField(max_length=128)
    semester = models.IntegerField(default=2)  # remove default in production
    year = models.IntegerField()
    subject_code = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    cover = models.ImageField(upload_to=upload_subject_cover_path,
                              null=True, blank=True)

    # Relationship Fields
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if len(self.subject_code.split('-')) > 2:
            self.subject_code = self.subject_code.split('-')[2]
        self.subject_code = '{}-{}'.format(
            self.course.course_code,
            self.subject_code
            )
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('universities_subject_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('universities_subject_update', args=(self.slug,))


def subject_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(subject_pre_save_receiver, sender=Subject)
