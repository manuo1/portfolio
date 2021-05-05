from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Nom',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )
        self.fields['subject'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Sujet',
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'name': '',
                'id': 'message',
                'cols': '30',
                'rows': '7',
                'class': 'form-control',
                'placeholder': 'Message',
            }
        )
