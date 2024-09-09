from django.shortcuts import render, get_object_or_404
from .models import Wine, Category
from datetime import datetime


def product_list(request):
    """
    View function to display a list of all wines.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template with the list of wines.
    """
    # Fetch all Wine and Category items
    wines = Wine.objects.all() 
    categories = Category.objects.all() 

    # Fetch all Wine items with optional filters
    category_filter = request.GET.get('category')
    rating_filter = request.GET.get('rating')

    if category_filter:
        wines = wines.filter(category__name=category_filter)

    if rating_filter:
        wines = wines.filter(rating__gte=rating_filter)

    context = {
        'wines': wines,
        'categories': categories,
    }
    return render(request, 'product_list.html', context)


def product_details(request, wine_id):
    """
    View to display the details of a single wine item and handle adding it to user basket.
    """
    wine = get_object_or_404(Wine, id=wine_id)
    return render(request, 'product_details.html', {'wine': wine})
