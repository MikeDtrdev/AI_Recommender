from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Product

def product_list(request):
    """
    This view retrieves all products from the database and renders them in the product list page.
    """
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    """
    This view handles the form submission for adding a new product.
    If the form is valid, it saves the product and redirects to the product list page.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")  # Add a success message
            return redirect('product_list')  # Redirect to product list
        else:
            messages.error(request, "Error adding product. Please check the form.")  # Add an error message
    else:
        form = ProductForm()  # Create an empty form for GET request
    
    return render(request, 'store/add_product.html', {'form': form})
