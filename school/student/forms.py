from . models import Articlee

from django.forms import ModelForm

from account.models import CustomUser

class ArticleForm(ModelForm):
    class Meta:

        model = Articlee
        fields = ['title', 'content',]


class UpdateUserForm(ModelForm):
    password = None

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name',]
        exclude = ['password1', 'password2',]

    