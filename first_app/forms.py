from django import forms
from django.core import validators
# widgets == field to html input


class contactForm(forms.Form):
    name = forms.CharField(
        label="User Name:", help_text="Total length 70 char", required=False, disabled=False, widget=forms.Textarea(attrs={'id': 'text_area', 'placeholder': 'Enter your name'}))
    # file = forms.FileField()

    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    meal = [('p', 'pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(
        choices=meal, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError(
    #             "Enter a name with at least 10 charecter.")
    #     return valname

    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email must contain .com")
    #     return valemail
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError(
    #             "Enter a name with at least 10 charecter.")

    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email must contain .com")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('At least 10 charecters')


class StudentData(forms.Form):
    name = forms.CharField(validators=[
                           validators.MaxLengthValidator(10, message='At least maximum 10 char')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[
                            validators.EmailValidator(message="Valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(
        34, message="Age maximum 34"), validators.MinValueValidator(24, message="age must minimum 24")])
    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg'], message="Upload pdf file")])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name at least 15 char")
