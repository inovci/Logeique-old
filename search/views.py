from django.shortcuts import render
from .forms import SearchForm
from spaces.models import House , Landlord , Client
from django.db.models import Q
from django.shortcuts import Http404

# Create your views here.

def get_result(value, choice = 1):
    #the case where the user select all checkbox
    clients = []
    landlords = []
    houses = []
    clients_list = []
    landlords_list = []
    houses_list = []
    if (choice == 1):
        try:
            value = int(value)
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)|
                    Q(house_rent=int(value))|
                    Q(house_deposit=int(value))
                )
            )
        except ValueError:
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)
                )
            )
        if not houses_list:
            houses = houses_list = []
        try:
            value = int(value)
            clients_list = list(
                Client.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value) |
                    Q(kind_desire__icontains=value) |
                    Q(rooms_number_desire__icontains=int(value)) |
                    Q(rent_proposal__icontains=int(value))|
                    Q(deposit_proposal__icontains=int(value))
                )
            )
        except ValueError:
            clients_list = list(
                Client.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value) |
                    Q(kind_desire__icontains=value)
                )
            )
        if not clients_list:
            clients = clients_list = []
        try:
            value = int(value)
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value) |
                    Q(houses__house_rent=int(value))|
                    Q(houses__house_deposit=int(value))
                )
            )
        except ValueError:
            landlords_list = list(
                Landlord.objects.filter(
                   Q(user__username__icontains = value)|
                   Q(user__first_name__icontains=value)|
                   Q(user__last_name__icontains=value)|
                   Q(houses__house_township__icontains=value) |
                   Q(houses__house_area__icontains=value)
                )
            )
        if not landlords_list:
            landlords = landlords_list = []

     #The case where house checkbox is selected
    elif choice == 2:
        try:
            value = int(value)
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)|
                    Q(house_rent =int(value)) |
                    Q(house_deposit=int(value))
                )
            )
        except ValueError:
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)
                )
            )
        if not houses_list:
            houses = houses_list = []

    #The case where client checkbox is selected
    elif choice == 3:
        try:
            value = int(value)
            clients_list = list(
                Client.objects.filter(
    
                    Q(rooms_number_desire=int(value)) |
                    Q(rent_proposal = int(value))|
                    Q(deposit_proposal = int(value))
                )
            )
        except ValueError:
            clients_list = list(
                Client.objects.filter(
                    Q(kind_desire__icontains=value) |
                    Q(area_desire__icontains=value) |
                    Q(township_desire__icontains = value)|
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains = value)|
                    Q(user__last_name__icontains = value)
                )
            )
                #We will look for different clients registered which are looking for a particular house or with a particular name
        if not clients_list:
            clients = clients_list = []
            
            
    #The case where landlord checkbox is selected
    elif choice == 4:
        try:
            value = int(value)
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value) |
                    Q(houses__house_rent=int(value))|
                    Q(houses__house_deposit=int(value))
                )
            )
        except ValueError:
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value)
                )
            )
            #We will look for different landlords registered which own a particular house or with a particular name
        if not landlords_list:
            landlords = landlords_list = []
         
            
    if (len(clients_list) > 0 or len(houses_list) > 0 or len(landlords_list)> 0):
            clients = clients_list
            houses = houses_list 
            landlords = landlords_list
    context = {
        'clients':clients,
        'clients_list':clients_list,
        'houses':houses,
        'houses_list':houses_list,
        'landlords':landlords,
        'landlords_list':landlords_list
    }
    return context


def get_result_two(value , choice1 , choice2):
    clients = []
    landlords = []
    houses = []
    clients_list = []
    landlords_list = []
    houses_list = []
    #The case where house and client checkbox are selected
    if ((choice1 == 2 and  choice2 ==3) or (choice1 == 3 and choice2 == 2)):
        try:
            value = int(value)
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)|
                    Q(house_rent =int(value)) |
                    Q(house_deposit=int(value))
                )
            )
        except ValueError:
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)
                )
            )
        if not houses_list:
            houses = houses_list = []
        try:
            value = int(value)
            clients_list = list(
                Client.objects.filter(
                    Q(kind_desire__icontains=value) |
                    Q(rooms_number_desire=int(value)) |
                    Q(rent_proposal = int(value))|
                    Q(deposit_proposal = int(value))|
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains = value)|
                    Q(user__last_name__icontains = value)
                )
            )
            #We will look for different clients registered which are looking for a particular house or with a particular name
        except ValueError:
            clients_list = list(
                Client.objects.filter(
                    Q(kind_desire__icontains=value)|
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains = value)|
                    Q(user__last_name__icontains = value)
                )
            )
        if not clients_list:
            clients = clients_list = []
            
            
    #The case where house and landlord checkbox are selected
    if((choice1 == 2 and choice2 == 4) or (choice1 == 4 and choice2 == 2)):
        try:
            value = int(value)
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)|
                    Q(house_rent =int(value)) |
                    Q(house_deposit=int(value))
                )
            )
        except ValueError:
            houses_list = list(
                House.objects.filter(
                    Q(house_township__icontains=value) |
                    Q(house_area__icontains=value) |
                    Q(house_kind__icontains=value)
                )
            )
        if not houses_list:
            houses = houses_list = []
        try:
            value = int(value)
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value) |
                    Q(houses__house_rent=int(value))|
                    Q(houses__house_deposit=int(value))
                )
            )
            #We will look for different landlords registered which own a particular house or with a particular name
        except ValueError:
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value)
                )
            )
        if not landlords_list:
            landlords = landlords_list = []
    #The case where client and landlord checkbox are selected
    if((choice1 == 3 and choice2 == 4) or (choice1 == 4 and choice2 == 3)):
        try:
            value = int(value)
            clients_list = list(
                Client.objects.filter(
                    Q(kind_desire__icontains=value) |
                    Q(rooms_number_desire=int(value)) |
                    Q(rent_proposal = int(value))|
                    Q(deposit_proposal = int(value))|
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains = value)|
                    Q(user__last_name__icontains = value)
                )
            )
                #We will look for different clients registered which are looking for a particular house or with a particular name
        except ValueError:
            clients_list = list(
                Client.objects.filter(
                    Q(kind_desire__icontains=value)|
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains = value)|
                    Q(user__last_name__icontains = value)
                )
            )
        if not clients_list:
            clients = clients_list = []
    #The case where landlord checkbox is selected
        try:
            value = int(value)
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value) |
                    Q(houses__house_rent=int(value))|
                    Q(houses__house_deposit=int(value))
                )
            )
                #We will look for different landlords registered which own a particular house or with a particular name
        except ValueError:
            landlords_list = list(
                Landlord.objects.filter(
                    Q(user__username__icontains = value)|
                    Q(user__first_name__icontains=value)|
                    Q(user__last_name__icontains=value)|
                    Q(houses__house_township__icontains=value) |
                    Q(houses__house_area__icontains=value)
                )
            )
        if not landlords_list:
            landlords = landlords_list = []
    if (len(clients_list) > 0 or len(houses_list) > 0 or len(landlords_list)> 0):
            clients = clients_list
            houses = houses_list 
            landlords = landlords_list
    context = {
        'clients':clients,
        'houses':houses,
        'landlords':landlords,
    }
    return context
        
def search(request):
    form = SearchForm()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            value = form.cleaned_data['query']
            value_for_all = form.cleaned_data['query_for_all']
            value_for_house = form.cleaned_data['query_for_house']
            print(value_for_house)
            value_for_client = form.cleaned_data['query_for_client']
            print(value_for_client)
            value_for_landlord = form.cleaned_data['query_for_lanlord']
            values_array = [
                value_for_all,
                value_for_house ,
                value_for_client,
                value_for_landlord
            ] 
            if values_array[0]:
                context = get_result(value)
                print(f"context:{context}")
            elif (values_array[1] and values_array[2]):
                print("ok")
                context = get_result_two(value, 2, 3)
                print(context)
            elif (values_array[1] and values_array[3]):
                context = get_result_two (value, 2, 4)
            elif (values_array[2] and values_array[3]):
                context = get_result_two (value, 3, 4)
            elif values_array[1]:
                context = get_result(value, 2)
            elif values_array[2]:
                context = get_result(value, 3)
            elif values_array[3]:
                context = get_result(value, 4)
            
            else:
                context = get_result(value)
    return render(request, 'search/search_result.html', locals())

def test(value):
    clients =list(
        Client.objects.filter(
            Q(kind_desire__icontains=value)|
            Q(user__username__icontains = value)|
            Q(user__first_name__icontains = value)|
            Q(user__last_name__icontains = value)
        )
    )
    for client in clients:
        print(client.user.username)
