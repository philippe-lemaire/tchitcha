from django import forms


class BuyTicketsForm(forms.Form):

    num_tickets = forms.IntegerField(
        min_value=1,
        label="Nombre de places :",
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
