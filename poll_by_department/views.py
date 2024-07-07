from django.shortcuts import render,HttpResponse
from .models import Main_Category

# Create your views here.

def category(request):
    main_category = Main_Category.objects.all().order_by('id')
    context = {
        'main_category': main_category,
    }
    return render(request,'second_task.html',context)