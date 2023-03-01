from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def getToken(request):
    appId = '47c99b347621411b9469311b6500f7d8'
    appCertificate = 'a4919859671a4221bab4336f57bc227e'
    channelName= request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24 
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1


    token =  RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid},safe=False)

def Welcome(request):
    return render(request, 'vid/welcome.html' , {})

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name= data['name'],
        uid = data['UID'],
        room_name= data['room_name'],
    )
    return JsonResponse({'name':data['name']}, safe=False)



def chatRoom(request):
    return render(request, 'vid/chatRoom.html' , {})


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')
    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name,
    )
    name =  member.name
    return JsonResponse({'name':member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name'],
    )
    member.delete()
    return JsonResponse('Member was deleted!', safe=False)
