from xml.dom.minidom import CharacterData
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(blank=True, max_length=40)
    slug = models.SlugField(unique=True, blank=True, max_length=400)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cabinet', kwargs={'slug_as': self.slug})


class TaskList(models.Model):

    title = models.CharField(max_length=150, default='untitled')
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, related_name="taskslists", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def count(self):
        return self.tasks.count()

    def count_finished(self):
        return self.tasks.filter(is_finished=True).count()

    def count_open(self):
        return self.tasks.filter(is_finished=False).count()


class Task(models.Model):

    CHOICES = (
        ('Important', 'Important'),
        ('50/50 Important', '50/50 Important'),
        ('Not important', 'Not important'),
    )

    CHOICES_2 = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    user = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_to = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=50, choices=CHOICES)
    task_list = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)
    day_of_week = models.CharField(verbose_name='День недели', max_length=15, choices=CHOICES_2, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.task_list)

    def close(self):
        self.completed = True            
        self.completed_at = timezone.now()
        self.save()

    def reopen(self):
        self.completed = False
        self.completed_at = None
        self.save()

