from django import forms


class ContactMe(forms.Form):

    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea())


