from django import forms


print("hello")
class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=50)

    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        if "a" in my_message:

            raise forms.ValidationError(f"message must not contain 'a'the message was '{my_message}'")
        
        return my_message
    


    
    