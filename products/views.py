from django.shortcuts import render, get_object_or_404
from .models import Wine, Category
from datetime import datetime


def product_list(request):
    """
    View function to display a list of wines with optional filtering and sorting.

    Args:
        request (HttpRequest): The HTTP request object containing query parameters for filtering and sorting.

    Returns:
        HttpResponse: The rendered 'product_list.html' template with the filtered and sorted list of wines and available categories.

    Query Parameters:
        - category (str): Optional. Filters wines by the specified category name.
        - rating (str): Optional. Filters wines by rating. Only wines with a rating greater than or equal to the specified value are included.
        - sort (str): Optional. Specifies the sorting order of the wines. Possible values are:
            - 'rating_desc': Sorts wines by rating in descending order (most popular first).
            - 'name_asc': Sorts wines by name in ascending order.
            - 'price_asc': Sorts wines by price in ascending order (cheapest first).

    Filters:
        - category_filter: Filters wines based on the category name if provided.
        - rating_filter: Filters wines based on the minimum rating if provided.

    Sorting:
        - Orders wines based on the selected sorting option.
    """
    # Fetch all Wine and Category items
    wines = Wine.objects.all() 
    categories = Category.objects.all() 

    # Fetch all Wine items with optional filters
    category_filter = request.GET.get('category')
    rating_filter = request.GET.get('rating')

    # Apply category, price and availability filters
    if category_filter:
        wines = wines.filter(category__name=category_filter)

    if rating_filter:
        wines = wines.filter(rating__gte=rating_filter)

    # Get the sorting parameter
    sort = request.GET.get('sort')

    # Apply sorting based on the selected option
    if sort == 'rating_desc':
        wines = wines.order_by('-rating')
    elif sort == 'name_asc':
        wines = wines.order_by('name')
    elif sort == 'price_asc':
        wines = wines.order_by('price')

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
