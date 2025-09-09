from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Footsal.', 
        'name': 'Nadia Aisyah Fazila',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)