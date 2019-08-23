from django import template
# Import your model
from users.models import CustomUser

register = template.Library()

@register.inclusion_tag('users/admin/sidebar.html')
def admin_sidebar_tags():
    users = CustomUser.objects.all()
    all = []
    for user in users:
        if user.is_staff:
            pass
        else:
            all.append(user)
    return {'users':all}
