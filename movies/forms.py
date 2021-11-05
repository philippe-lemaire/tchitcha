from django import forms


class BuyTicketsForm(forms.Form):

    num_tickets = forms.IntegerField(
        min_value=1, max_value=10, label="Nombre de places :"
    )
