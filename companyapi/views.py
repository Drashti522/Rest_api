from django.http import HttpResponse,JsonResponse

def homepage(request):
    print("home page request")
    friend=[
        'arati',
        'ravi',
        'tanisha'
    ]
    return JsonResponse(friend,safe=False)