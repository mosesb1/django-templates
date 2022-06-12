from django.shortcuts import render
from django.http.response import HttpResponse

def home_view(request):
    return render(request, 'sample_app/home.html')

def variables_view(request):

    my_var = {
        'first_name': 'moses',
        'last_name': 'burkhart',
        'some_list': [1,2,3],
        'user_logged_in': False,
        'some_dict': {'inside_key': 'inside_value'}
    }

    return render(request, 'sample_app/variables.html', context=my_var)