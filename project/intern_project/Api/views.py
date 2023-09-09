from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timezone

# Create your views here.


def my_view(request):

    
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    
    utc_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day = datetime.now().strftime('%A')
    github_repo_url="https://github.com/solutionasepe/hngx-stage-one.git"
    github_file_url = "https://github.com/solutionasepe/hngx-stage-one/blob/main/Api/views.py"

    # Do something with the values
    response = {
        "slack_name": slack_name,
        "utc_time": utc_time,
        "track" : track,    
        "current_day":current_day,
        "github_file_url":github_file_url,
        "github_repo_url":github_repo_url

    }

    return JsonResponse(response, safe=False)
    

