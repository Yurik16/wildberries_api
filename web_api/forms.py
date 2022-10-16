from django import forms


class SingleReqForm(forms.Form):
    article = forms.IntegerField(label='article')
