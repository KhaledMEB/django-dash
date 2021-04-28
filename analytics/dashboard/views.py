from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers

# directs a user to the dashboard_with_pivot.html templates
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

# sends the response with data to the pivot table on the app's front-end
def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)