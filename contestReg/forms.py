from django import forms
from .models import Participant

class AddNewParticipant(forms.ModelForm):
    class Meta():
        model = Participant
        fields = {'name','email','number','college','paid','present'}
        
    # name    = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # email   = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # number  = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # college = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # paid    = forms.BooleanField(required=True)
    # present = forms.BooleanField(required=True)