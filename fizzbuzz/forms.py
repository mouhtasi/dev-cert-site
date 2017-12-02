from django import forms
from codemirror.widgets import CodeMirror


class PythonCodeInput(forms.Form):
    code_text = forms.CharField(widget=CodeMirror(mode='python'))


class GuestUserDetailsInput(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=100)
