from django.contrib.auth.forms import UserCreationForm
from django import forms


from user_task.models import Task


from user_task.models import CustomUser, Task


class RegistrationForm(UserCreationForm):
    ''' Model for Custom User model'''
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
    


class LoginForm(forms.Form):
    ''' Custom form for handdling the login'''

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_username(self):
        username = CustomUser.objects.filter(username=self.cleaned_data.get('username'))
        if username.exists():
            return self.cleaned_data['username']
        raise forms.ValidationError('user not found')



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('user',) # excluded the user field to show up in the form, will add the value later inside view using request.user
    
    