from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.json'):
            raise forms.ValidationError("The uploaded file must be a .json file.")
        return file
