import django_filters
from django import forms
from .models import Car

class CarFilter(django_filters.FilterSet):
    price_per_day__gt = django_filters.NumberFilter(field_name='price_per_day', lookup_expr='gt', label='Price greater than')
    price_per_day__lt = django_filters.NumberFilter(field_name='price_per_day', lookup_expr='lt', label='Price less than')
    year__gt = django_filters.DateFilter(widget=forms.DateInput(attrs={'type':'date'}), field_name='year', lookup_expr='gte', label='Year greater than')
    year__lt = django_filters.DateFilter(widget=forms.DateInput(attrs={'type':'date'}), field_name='year', lookup_expr='lte', label='Year less than')

    transmission = django_filters.MultipleChoiceFilter(
        choices=Car.TRANSMISSION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Transmission',
    )

    class Meta:
        model = Car
        fields = ['price_per_day__gt', 'price_per_day__lt', 'year__gt', 'year__lt', 'transmission']
