from django.shortcuts import render, redirect , get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
 
# Create your views here.

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    # On ramasse tous les rooms dont l'utilisateur actif en fait parti.
    rooms = Room.objects.filter(
        Q(user1=request.user)|Q(user2 = request.user)
    )
    print(rooms)
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
        """
        1 - On vérifie si l'utilisateur est un landlord ou un client.
        2 - Si l'utilisateur est un landlord:
            a - Alors la varariable user1 reçoit le landlord.
            b - La variable user2 reçoit le client.
        3 - Sinon si l'utilisateur est un client:
            a - Alors la varariable user1 reçoit le landlord.
            b - La variable user2 reçoit le client.
        Le but est de mettre en premier le landlord puis en second le client pour faciliter les liens urls.
        """
        try:
            request.user.landlord != None
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
        except:
            request.user.client != None
            user2 = get_object_or_404(User, username=request.user)
            user1 = get_object_or_404(User, username=other_user)
            room = Room.objects.create(user1 = user1, user2 = user2)
            room.save()
            try:
                user1.landlord.user_id != None
                return render(request , 'chat/discuss_with_client.html' , locals())
            except:
                user1.client.user_id != None
                return render(request , 'chat/discuss_with_landlord.html' , locals())
