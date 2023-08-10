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
