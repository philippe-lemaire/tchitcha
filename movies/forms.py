from django import forms


class BuyTicketsForm(forms.Form):

    num_tickets = forms.IntegerField(min_value=1, label="Nombre de places :")
