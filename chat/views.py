from django.shortcuts import render, redirect , get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
 
# Create your views here.

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', locals())


def checkview(request, other_user):
    other_user = get_object_or_404(User, username=other_user)

    try:
        room = Room.objects.get(Q(user1=request.user, user2=other_user)|
                                Q(user1 = other_user, user2 = request.user))
    except:
        room = None

    if room != None:
        try:
            request.user.landlord.user_id != None
            return render(request , 'chat/discuss_with_client.html' , locals())
        except:
            request.user.client.user_id != None
            return render(request , 'chat/discuss_with_landlord.html' , locals())

    else:
        user1 = get_object_or_404(User, username=request.user)
        user2 = get_object_or_404(User, username=other_user)
        room = Room.objects.create(user1 = user1, user2 = user2)
        room.save()
        try:
            user1.landlord.user_id != None
            return render(request , 'chat/discuss_with_client.html' , locals())
        except:
            user1.client.user_id != None
            return render(request , 'chat/discuss_with_landlord.html' , locals())

"""
def clientCheckview(request, user1 , user2):
    user1 = get_object_or_404(User, username=user1)
    user2 = get_object_or_404(User, username=user2)

    try:
        room = Room.objects.get(Q(user1=user1, user2=user2)|
                                Q(user1 = user2, user2 = user1))
    except:
        room = None

    if room != None:
        return render(request , 'chat/discuss_with_landlord.html' , locals())
    else: 
        user1 = get_object_or_404(User, username=user1)
        user2 = get_object_or_404(User, username=user2)
        new_room = Room.objects.create(user1 = user1, user2 = user2)
        new_room.save()
        return render(request , 'chat/discuss_with_landlord.html' , locals())
"""

def send(request, user_id, room_id):

    message = request.POST['message']
    print(message)
    user = User.objects.get(id=user_id)
    try:
        client_user = get_object_or_404(Client, user_id=user.id)
        if client_user:
            room = Room.objects.get(id = room_id)
            new_message = Message.objects.create(value=message, user=user, room=room)
            new_message.save()
            return render(request, 'chat/discuss_with_landlord.html', locals())
    except:
        landlord_user = get_object_or_404(Landlord, user_id=user.id)
        if landlord_user:
            room = Room.objects.get(id = room_id)
            new_message = Message.objects.create(value=message, user=user, room=room)
            new_message.save()
            return render(request, 'chat/discuss_with_client.html', locals()) 

def receive(request, room_id):
    room_details = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages":list(messages.values())})
