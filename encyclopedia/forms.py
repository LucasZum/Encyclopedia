from django import forms


class CreateEntry(forms.Form):
    title = forms.CharField(
        required=True,
        max_length=100,
        label="Title",
        widget=forms.TextInput(attrs={
        'class': 'title-input',
        'placeholder': 'Title...',
        'name': 'title'
        })
    )

    content = forms.CharField(
        required=True,
        label='Content',
        widget=forms.Textarea(attrs={
        'placeholder': 'Your content here...',
        'class': 'content-input',
        'name': 'content'
        })
    )