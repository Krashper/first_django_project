from django.shortcuts import render

# Create your views here.
def main(request):
    data = {
        'title': 'Главная страница',
        'content': ['Здесь', 'должен', 'быть', 'контент'],
    }
    return render(request, 'main/main.html', data)

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})