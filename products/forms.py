from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, ButtonHolder, Submit, HTML
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price']

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('description', css_class='form-control mb-3'),
        Field('image', css_class='form-control'),
        Field('price', css_class='form-control'),
        Div(
            ButtonHolder(
                Div(
                    HTML('{% if product %}'
                         '<a href="{% url "delete" pk=product.id %}" class="btn btn-secondary">Delete</a>'
                         '{%endif%}'),
                    style="float:left;"
                ),
                Div(
                    HTML('<a href="{% url "index" %}" class="btn btn-secondary">Cancel</a> '),
                    HTML('<input type="hidden" name="_method" value="post">'),
                    Submit('submit', 'Save changes', css_class='btn btn-primary'),
                    style="float: right;"
                )
            )
        )
    )
