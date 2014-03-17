from django import forms

class RawMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    key = forms.CharField(max_length=256, widget=forms.PasswordInput,
                          label="Encryption Key")
    key2 = forms.CharField(max_length=256, widget=forms.PasswordInput,
                           label="Encryption Key (again)")

    def clean(self):
        key = self.cleaned_data.get('key')
        key2 = self.cleaned_data.get('key2')

        if key and key != key2:
            raise forms.ValidationError("Keys don't match")

        return self.cleaned_data
        
class DecodeForm(forms.Form):
    key = forms.CharField(max_length=256, widget=forms.PasswordInput, label="Key")
