from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Car
from .filters import CarFilter


def cars_list(request):
    cars = Car.objects.filter(is_available=True)
    car_filter = CarFilter(request.GET, queryset=cars)
    filtered_cars = car_filter.qs

    paginator = Paginator( car_filter.qs, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'car_count': filtered_cars.count(),
        'filter': car_filter,
    }

    if 'HX-Request' in request.headers:
        return render(request, 'cotton/car_list.html', context)

    return render(request, 'cars-list.html', context)