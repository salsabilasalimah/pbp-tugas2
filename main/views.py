from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406432734',
        'name': 'Salsabila Salimah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)