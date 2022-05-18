from django.db import models
from django.conf import settings
# Create your models here.

MEMBERSHIP_SUBJECT = (
    ('MATH101', 'math101'),
    ('MATH102', 'math102'),
    ('BIO101', 'bio101')
)

class Membership(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(
    choices=MEMBERSHIP_SUBJECT, default='Math101',
    max_length=30
      )
def __str__(self):
       return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
    related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership,
    related_name='user_membership', on_delete=models.SET_NULL, null=True)
    def __str__(self):
       return self.user.username

