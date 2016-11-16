from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.http import require_http_methods
from imagebook.models import *


def listData(data):
    datas = []
    for d in data:
        datas.append({
            'id':d.id,
            'image':d.image,
            'creator':d.creator,
            'created_at':d.created_at,
            'updated_at':d.updated_at
        })
    return datas


@require_http_methods(["GET", "POST"])
def books(request):
    if request.method == 'GET':
        creator = request.GET.get('creator','chulin')
        bks = imagebook.objects.filter(creator=creator)
        data = listData(bks)
        return JsonResponse(data,safe=False)

    # create a new iamgebook list
    if request.method == 'POST':
        image = request.POST.get('image','default/image')
        creator = request.POST.get('creator','chulin')
        imag = imagebook.objects.create(
            image=image,
            creator=creator
        )
        data = {
            'id':imag.id,
            'image':imag.image,
            'creator':imag.creator,
            'created_at':imag.created_at,
            'updated_at':imag.updated_at
        }

        return JsonResponse({'deta':data})




def booktime(request,year,month,day):
    # time = year+'-'+month+'--'+day
    # return HttpResponse('the time is '+time)
    return JsonResponse([year, month, day], safe=False)


@require_http_methods(["GET", "POST","DELETE"])
def bookdetail(request,pk):
    obj = imagebook.objects.get(id=pk)

    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse('delete ok!')

    if request.method == 'POST':
        image = request.POST.get('image','')
        if image:
            obj.image = image
            obj.save()

    data = {
        'id':obj.id,
        'image':obj.image,
        'creator':obj.creator,
        'created_at':obj.created_at,
        'updated_at':obj.updated_at
    }
    return JsonResponse(data)
