from django.shortcuts import render, redirect , get_object_or_404
from chat.models import Room, Message
from spaces.models import Deal, House, Landlord, Proposal
from django.contrib.auth.models import User
from django.db.models import Q
from spaces.models import Deal
 
# Create your views here.

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    # On ramasse tous les rooms dont l'utilisateur actif en fait parti.
    rooms = Room.objects.filter(
        Q(user1=request.user)|Q(user2 = request.user)
    )
    # on recupère tous les messages du room.
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', locals())

"""def dealt(request , room_id):
     room = Room.objects.get(id=room_id)
     deal = Deal.objects.get(Q(client = room.user1,landlord = room.user2)
     |Q(client = room.user2,landlord = room.user1))"""


def checkviewClient(request, house_id):
    house = get_object_or_404(House, id=house_id)

    try:
        room = Room.objects.get(Q(user1=request.user, user2=house.landlord.user)|
                                Q(user1=house.landlord.user, user2=request.user))
    except:
        room = None

    if room != None:
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
        user2 = get_object_or_404(User, username=request.user)
        user1 = get_object_or_404(User, username=house.landlord.user)
        room = Room.objects.create(user1 = user1, user2 = user2)
        room.save()
        deal = Deal.objects.create(client=user2.client, landlord=user1.landlord, house=house,concluded=False)
        deal.save()
        return render(request , 'chat/discuss_with_landlord.html' , locals())


def checkviewLandlord(request, other_user, proposal_id):
    # On éssai de récupérer l'id du proposal.
    proposal = get_object_or_404(Proposal, id=proposal_id)
    # On éssai de récupérer toutes les maisons du landlord (propriétaire).
    houses = House.objects.filter(landlord=request.user.landlord)
    # On éssai de récupérer la maison qui match avec les données du proposal trouvé.
    house = houses.get(
        Q(house_area__icontains=proposal.area_desire,
        house_township__icontains=proposal.township_desire,
        house_deposit=proposal.deposit_proposal,
        house_rent=proposal.rent_proposal)|
        Q(house_area__icontains=proposal.area_desire,
        house_township__icontains=proposal.township_desire,
        house_deposit__lte=proposal.deposit_proposal + proposal.deposit_proposal * 0.1,
        house_deposit__gte=proposal.deposit_proposal - proposal.deposit_proposal * 0.1,
        house_rent__lte=proposal.rent_proposal + proposal.rent_proposal * 0.1,
        house_rent__gte=proposal.rent_proposal - proposal.rent_proposal * 0.1 )
    )
    other_user = get_object_or_404(User, username=other_user)

    try:
        room = Room.objects.get(Q(user1=request.user, user2=other_user)|
                                Q(user1 = other_user, user2 = request.user))
    except:
        room = None

    if room != None:
        return render(request, 'chat/discuss_with_client.html', locals())
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
        user1 = get_object_or_404(User, username=request.user)
        user2 = get_object_or_404(User, username=other_user)
        room = Room.objects.create(user1 = user1, user2 = user2)
        room.save()
        deal = Deal.objects.create(client=user2.client, landlord=user1.landlord, house=house,concluded=False)
        deal.save()
        return render(request, 'chat/discuss_with_client.html', locals())

"""
def checkview(request, house_id, other_user):
    house = get_object_or_404(House, id=house_id)
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
        
        1 - On vérifie si l'utilisateur est un landlord ou un client.
        2 - Si l'utilisateur est un landlord:
            a - Alors la varariable user1 reçoit le landlord.
            b - La variable user2 reçoit le client.
        3 - Sinon si l'utilisateur est un client:
            a - Alors la varariable user1 reçoit le landlord.
            b - La variable user2 reçoit le client.
        Le but est de mettre en premier le landlord puis en second le client pour faciliter les liens urls.
        
        try:
            request.user.landlord != None
            user1 = get_object_or_404(User, username=request.user)
            user2 = get_object_or_404(User, username=other_user)
            room = Room.objects.create(user1 = user1, user2 = user2)
            room.save()
            deal = Deal.objects.create(client=user2.client, landlord=user1.landlord, house=house, concluded=False)
            deal.save()
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
            deal = Deal.objects.create(client=user2.client, landlord=user1.landlord, house=house,concluded=False)
            deal.save()
            try:
                user2.landlord.user_id != None
                return render(request , 'chat/discuss_with_client.html' , locals())
            except:
                user2.client.user_id != None
                return render(request , 'chat/discuss_with_landlord.html' , locals())
"""