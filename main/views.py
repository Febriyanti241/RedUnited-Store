from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'RedUnited Store',
        'name': 'Febriyanti',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)