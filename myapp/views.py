from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Fish

def home(request):
    return render(request, 'fish_library/home.html')

def fish_list(request):
    fishes = Fish.objects.all()
    paginator = Paginator(fishes, 10) 

    page = request.GET.get('page')
    try:
        fishes = paginator.page(page)
    except PageNotAnInteger:
        fishes = paginator.page(1)
    except EmptyPage:
        fishes = paginator.page(paginator.num_pages)

    return render(request, 'fish_library/fish_list.html', {'fishes': fishes})

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    return render(request, 'fish_library/fish_detail.html', {'fish': fish})
