from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()


# Create your forms here.

class NewUserForm(UserCreationForm):
    MobileNumber = forms.CharField(required=True, max_length=10)
    name = forms.CharField(required=True, max_length=20)
    dob = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ("MobileNumber", 'name', "dob", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.MobileNumber = self.cleaned_data['MobileNumber']
        user.name = self.cleaned_data['name']
        user.dob = self.cleaned_data['dob']
        if commit:
            user.save()
        return user
