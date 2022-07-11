from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE = (
        ('Superuser','Superuser'),
        ('User','User'),
    )
    user_role = forms.ChoiceField(choices=ROLE)
    
    class Meta:
        model = User
        fields = {'username','user_role','password1','password2'}
    
    def save(self,commit=True):
        user = super(CustomUserCreationForm,self).save(commit=False)
        user.user_role = self.cleaned_data['user_role']
        if commit:
            user.save()

        return user