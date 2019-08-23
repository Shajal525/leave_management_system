from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import CustomUser
from datetime  import date

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name', 'last_name')

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_first_name(self):
        fst_nm = self.cleaned_data['first_name']
        return fst_nm[0].upper()+fst_nm[1:].lower()

    def clean_last_name(self):
        lst_nm = self.cleaned_data['last_name']
        return lst_nm[0].upper()+lst_nm[1:].lower()

    def clean(self):
        cleaned_data = super().clean()
        if self.is_valid():
            return cleaned_data
        else:
            raise forms.ValidationError(_('Data invalid!'), code='invalid')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'bio', 'image')

    def clean_first_name(self):
        fst_nm = self.cleaned_data['first_name']
        return fst_nm[0].upper()+fst_nm[1:].lower()

    def clean_last_name(self):
        lst_nm = self.cleaned_data['last_name']
        return lst_nm[0].upper()+lst_nm[1:].lower()

    def clean(self):
        cleaned_data = super().clean()
        if self.is_valid():
            return cleaned_data
        else:
            raise forms.ValidationError(_('Data invalid!'), code='invalid')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('password',)
        
    def clean(self):
        cleaned_data = super().clean()
        if self.is_valid():
            return cleaned_data
        else:
            raise forms.ValidationError(_('Data invalid!'), code='invalid')
