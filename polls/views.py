from django.shortcuts import render
from .models import activity,user
from django.core import serializers
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    data = dict()
    responce = final_data_function()
    data["ok"] = True
    data["members"] = responce


    return JsonResponse(data, safe=False)

def final_data_function():
    outer_list = []
    inner_list = []
    for act in activity.objects.all()[:3]:

        temp_dict = dict()
        temp_dict["id"] = act.user_activity.id
        temp_dict["real_name"] = act.user_activity.real_name
        temp_dict["tz"] = act.user_activity.tz

        temp_dict1 = dict()
        temp_dict1["start_time"] = str(act.start_time)
        temp_dict1["end_time"] = str(act.end_time)
        inner_list.append(temp_dict1)

        temp_dict["activity_periods"] = inner_list
        outer_list.append(temp_dict)



    return outer_list















