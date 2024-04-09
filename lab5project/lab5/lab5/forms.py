from django import forms

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=60)
    location = forms.MultipleChoiceField(choices=[('location A','Location A'),('location B','Location B'),('location C','Location C')],
        widget = forms.CheckboxSelectMultiple)


    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        if "garbage" in my_message:
            raise forms.ValidationError(f"Bad reviews are bad for business. Don't say 'Terrible' you said, {my_message}'")
        
        return my_message

