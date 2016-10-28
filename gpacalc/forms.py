from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "input-lg col-md-4 col-md-offset-4"}),
    )

    password = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "input-lg col-md-4 col-md-offset-4"}),
    )

class SemesterForm(forms.Form):
    for x in range(5):
        classname = forms.CharField(max_length = 20, widget = forms.TextInput(attrs={'class': "form-control form-control-inline class-input"}))
        credits = forms.CharField(max_length=10, widget = forms.TextInput(attrs={'class': "form-control form-control-inline credits-input"}))
        grade = forms.CharField(max_length=1, widget=forms.TextInput(widget = forms.TextInput(attrs={'class': "form-control form-control-inline grade-input"})))



