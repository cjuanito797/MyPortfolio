from django import forms


class ContactMe(forms.Form):
    email = forms.EmailField(
        label=("Email"),
        widget=forms.EmailInput
    )
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea())


