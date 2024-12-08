from django.shortcuts import render
from django.db import connection
# Create your views here.


def index(request):
    template_path = 'homepage/index.html'
    with connection.cursor() as cursor:
        cursor .execute("SELECT * FROM subscriptions_type;")
        ans = cursor.fetchall()
        context = {'test' : ans}
        return render(request, template_path, context)
    
