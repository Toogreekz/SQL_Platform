from django.db import models
from django.contrib.auth.models import AbstractUser


# Модель пользователя
class User(AbstractUser):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    tasks_completed = models.IntegerField(default=0)
    
    id_group = models.ForeignKey('Groups', on_delete=models.CASCADE, related_name='user', null=False)
    
    def __str__(self) -> str:
        return super().__str__()
    
# Модель Задач
class Tasks(models.Model):
    class Difficulty(models.IntegerChoices):
        EASY = 0, "Легко"
        MEDIUM = 1, "Медиум"
        HARD = 2, "Сложно"
        SUPER_HARD = 3, "Очень сложно"
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    difficulty = models.IntegerField(choices=Difficulty.choices)
    id_theme = models.ForeignKey('Themes', on_delete=models.CASCADE, related_name='tasks')
    benchmark_query = models.TextField(null=False, max_length=2000)
    
    def __str__(self):
        return f'{self.id}. {self.name}'

    class Meta:
        ordering = ['difficulty', 'name']
        db_table = 'Tasks'

# Модель Тем для задач
class Themes(models.Model):
    name = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.id}, {self.name}'
    
    class Meta:
        ordering = ['name']
        db_table = 'Themes'

# Модель групп
class Groups(models.Model):
    name = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    in_rating = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'Groups'

# Модель решений (многое ко многим Студенты-Задачи)
class Solutions(models.Model):
    class Status(models.IntegerChoices):
        SUCCESS = 0, 'Решено'
        FAILED = 1, 'Ошибка'
        NOT_STARTED = 2, 'Не приступал'

    time = models.DateTimeField(auto_now_add=True)
    input = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=2)
    
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='Solutions', null=False)
    tasks = models.ForeignKey('Tasks', on_delete=models.CASCADE, related_name='Solutions', null=False)
    
    def __str__(self):
        return f'{self.id}. user={self.user} task={self.tasks}'

    class Meta:
        db_table = 'Solutions'