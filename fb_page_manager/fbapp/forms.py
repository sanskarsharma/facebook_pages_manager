from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class SimpleForm(forms.Form):
    name = forms.CharField(label="Page Name")
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login', css_class='btn-primary'))
