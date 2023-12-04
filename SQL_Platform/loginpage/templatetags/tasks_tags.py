from django import template
from loginpage.models import *
from django.db.models import Q


register = template.Library()


@register.simple_tag()
def get_active_themes():
    return Themes.objects.filter(is_active=True)

@register.simple_tag()
def get_active_students():
    return User.objects.filter(is_active=True).order_by("-tasks_completed")

@register.simple_tag()
def get_active_tasks_in_theme(theme):
    return Tasks.objects.filter(Q(id_theme_id=theme.id) & Q(is_active=1))

@register.simple_tag()
def if_user_admin(user_id):
    user = User.objects.get(pk=user_id)
    return user.is_superuser

@register.simple_tag()
def get_status_of_task(task, user):
    return Solutions.objects.filter(Q(tasks_id=task.id) & Q(user_id=user.id))

@register.simple_tag()
def if_any_success_in_solutions(solutions):
    for solution in solutions:
        if solution.status == 0:
            return True
    return False

@register.simple_tag()
def get_n_solutions(user):
    return Solutions.objects.filter(Q(user_id=user.id)).count()

@register.simple_tag()
def get_percent_success_solutions(user):
    return 100 * Solutions.objects.filter(Q(user_id=user.id) & Q(status=0)).count() / Solutions.objects.filter(Q(user_id=user.id)).count()