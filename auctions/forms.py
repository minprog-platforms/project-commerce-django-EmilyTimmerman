from django import forms
from django.forms import ModelForm
import auctions.models


# Create a Listing Entry Form
class ListingForm(ModelForm):
    class Meta:
        model = auctions.models.AuctionListing
        fields = ("title", "description", "price", "picture")

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'picture': forms.URLInput(attrs={'class':'form-control', 'placeholder':'URL'}),
        }




