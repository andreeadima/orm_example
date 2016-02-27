from django.db import models
from django.core import validators

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=250,
                                  null=False,
                                  blank=False)
    last_name = models.CharField(max_length=250,
                                 null=False,
                                 blank=False)
    email = models.EmailField()
    gender = models.SmallIntegerField(choices=[(0, 'male'),
                                               (1, 'female')])
    birth_date = models.DateField()
    age = models.PositiveIntegerField(validators=[
        validators.MaxValueValidator(100),
        validators.MinValueValidator(18)])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} {1}, joined on {2}".format(self.first_name,
                                               self.last_name,
                                               self.date_joined.strftime(format='%d %m %Y'))

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name,
                                self.last_name)


class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=1000)

    user = models.ForeignKey(to='User',
                             related_name='posts')

    def __str__(self):
        return "{0}, by {1}, on {2}".format(self.title,
                                            self.user.full_name,
                                            self.date_added.strftime(format='%d %m %Y'))


class Comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)

    user = models.ForeignKey(to='User',
                             related_name='comments')
    post = models.ForeignKey(to='Post',
                             related_name='comments')

    def __str__(self):
        return "Comment on {0}, by {1} on {2}".format(self.post.title,
                                                      self.user.full_name,
                                                      self.date_added.strftime(format='%d %m %Y'))
