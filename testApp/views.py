from django.shortcuts import render
from testApp.models import FilterModel

# Create your views here.
def upperView(request):

    data_list = FilterModel.objects.all()
    return render(request, 'testApp/upper.html', {'data_list' : data_list})
