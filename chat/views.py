from django.shortcuts import render, redirect , get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
 
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })



"""

def room(request, room_id , user_id):
    user = User.objects.get(id = user_id)
    room_details = Room.objects.get(id=room_id)
    return render(request, 'discuss.html', {
        'username': user.username,
        #'room': room,
        'room_details': room_details
    })
"""

def landlordCheckview(request, user1_id , user2_id):

    try:
        room = Room.objects.get(Q(user1=user1_id, user2=user2_id)|
                                Q(user1 = user2_id , user2 = user1_id))
    except:
        room = None

    if room != None:
        return render(request , 'chat/discuss_with_client.html' , locals())
    else: 
        user1 = get_object_or_404(User, id=user1_id)
        user2 = get_object_or_404(User, id=user2_id)
        new_room = Room.objects.create(user1 = user1, user2 = user2)
        new_room.save()
        return render(request , 'chat/discuss_with_client.html' , locals())


def clientCheckview(request, user1_id , user2_id):

    try:
        room = Room.objects.get(Q(user1=user1_id, user2=user2_id)|
                                Q(user1 = user2_id , user2 = user1_id))
    except:
        room = None

    if room != None:
        return render(request , 'chat/discuss_with_landlord.html' , locals())
    else: 
        user1 = get_object_or_404(User, id=user1_id)
        user2 = get_object_or_404(User, id=user2_id)
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
"""