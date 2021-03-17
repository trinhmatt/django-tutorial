from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("ello mate")

@csrf_exempt
def createItem(request):
    if (request.method == "POST"):
        
        #Convert bytes to json string
        body_unicode = request.body.decode('utf-8')

        #Convert to object
        body = json.loads(body_unicode)

        #Access variables
        print(body['test'])

        return HttpResponse(body_unicode)
