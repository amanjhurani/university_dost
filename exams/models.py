from django.urls import reverse
from config.settings.base import AUTH_USER_MODEL
from django.db import models
from universities.models import Subject
from config.utils import (upload_question_body_path,
                          random_string_generator,)
from markdownx.models import MarkdownxField


class Exam(models.Model):

    # Choices
    MONTH_CHOICES = (
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December')
    )
    TERM_CHOICES = (
        ('summer', 'Summer'),
        ('winter', 'Winter')
    )

    # Fields
    month = models.CharField(max_length=128, choices=MONTH_CHOICES)
    year = models.CharField(max_length=4)
    term = models.CharField(max_length=12, choices=TERM_CHOICES)
    date = models.DateField()
    total_time = models.CharField(max_length=12)
    total_marks = models.IntegerField()
    exam_code = models.CharField(max_length=128, blank=True, null=True)
    exam_complete = models.BooleanField(default=False)

    # Relationship Fields
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if self.exam_code and len(self.exam_code.split('-')) > 3:
            self.exam_code = self.exam_code.split('-')[3]
        self.exam_code = '{}-{}'.format(self.subject.subject_code, random_string_generator(size=5))
        qs_exists = Exam.objects.filter(exam_code=self.exam_code).exists()
        if qs_exists:
            self.exam_code = '{}-{}'.format(self.subject.subject_code,
                                            random_string_generator(size=5))
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject.name + " " + self.term + "-" + self.year

    def get_absolute_url(self):
        return reverse('exams_exam_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('exams_exam_update', args=(self.pk,))


class Question(models.Model):

    # Choices
    QUESTION_TYPE_CHOICES = (
        ('mcq', 'MCQ'),
        ('short_question', 'Short Question'),
        ('descriptive_question', 'Descriptive Question'),
    )

    # Fields
    question_code = models.CharField(max_length=128, blank=True, null=True)
    question_number = models.CharField(max_length=128)
    question_body = MarkdownxField()
    question_type = models.CharField(
        max_length=12, choices=QUESTION_TYPE_CHOICES)
    answer = MarkdownxField(blank=True, null=True)
    explanation = MarkdownxField(blank=True, null=True)
    marks = models.IntegerField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    # Relationship Fields
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if len(self.question_code.split('-')) > 4:
            self.question_code = self.question_code.split('-')[4]
        self.question_code = '{}-{}'.format(self.exam.exam_code, self.question_code)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_number + " | " + self.exam.term + "-" + self.exam.year

    def get_absolute_url(self):
        return reverse('exams_question_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('exams_question_update', args=(self.pk,))


class AnswerFeedback(models.Model):

    # Choices
    FEEDBACK_TYPE_CHOICES = (
        ('wrong_answer', 'Wrong Answer'),
        ('improvement', 'Improvement'),
    )

    # Fields
    feedback_title = models.CharField(max_length=256, blank=True, null=True)
    feedback_body = models.TextField()
    feedback_type = models.CharField(
        max_length=128, choices=FEEDBACK_TYPE_CHOICES)
    user_email = models.EmailField(max_length=256, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    # Relationship Fields
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.feedback_title

    def get_absolute_url(self):
        return reverse('exams_answer_feedback_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('exams_answer_feedback_update', args=(self.pk,))

