from django import forms

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


class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)

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
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 10:
            raise forms.ValidationError(
                "Enter a name with at least 10 charecter.")

        if '.com' not in valemail:
            raise forms.ValidationError("Email must contain .com")
