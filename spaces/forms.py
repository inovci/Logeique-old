from django import forms

CHOICES = [('client', 'Client'),
           ('landlord', 'Propriétaire')]

TOWNSHIP_CHOICES = [
    ('AB', 'ABOBO'),
    ('AD', 'ADJAME'),
    ('AN', 'ANYAMA'),
    ('AT', 'ATTECOUBE'),
    ('BI' , 'BINGERVILLE')
    ('CO', 'COCODY'),
    ('KO', 'KOUMASSI'),
    ('MA', 'MARCORY'),
    ('PL', 'PLATEAU'),
    ('PO', 'PORT-BOUET'),
    ('SO', 'SONGON')
    ('TR', 'TREICHVILLE'),
    ('YO', 'YOPOUGON')
]

ABOBO_AREA_CHOICES = [
    ('Abb' , 'Abobo Baoulé'),
    ('Abc' , 'Abobo Centre'),
    ('Abd' , 'Abobo Dokoui'),
    ('Abn' , 'Abobo Nord'),
    ('Abs' , 'Abobo Sud'),
    ('Abt' , 'Abobo Té'),
    ('Agb' , 'Agbékoi'),
    ('Ago' , 'Agouéto'),
    ('Aké' , 'Akéikoi'),
    ('Ano' , 'Anonkoua Kouté'),
    ('Avo' , 'Avocatier'),
    ('Col' , 'Colatier'),
    ('Ken' , 'Kennedy Clouetcha'),
    ('Ndo' , 'Ndotré'),
    ('Pla' , 'Plaque'),
    ('Sag' , 'Sagbé'),
    ('Sog' , 'Sogephia'),
    ('Ban' , 'Banco'),
    ('Dji' , 'Djibi Village'),
]
ADJAME_AREA_CHOICES = [
    ('MaI', 'Mairie I'),
    ('MaII', 'Mairie II'),
    ('Bro', 'Bromakoté'),
    ('Adj', 'Adjamé Nord'),
    ('L220', '220 logements'),
    ('Hex', 'Habitat extension'),
    ('Pal', 'Pallier'),
    ('Mat', 'Marie Thérèse'),
    ('Smi', 'Saint Michel'),
    ('Veb', 'Village Ebrié'),
    ('Dal', 'Dallas'),
    ('Ind', 'Indénié'),
    ('WiI', 'Williamsville I'),
    ('WiII', 'Williamsville II'),
    ('WiIII', 'Williamsville III'),
    ('Sof', 'SODECI- FILTISAC'),
    ('Mir', 'Mirador'),
    ('Adn', ' Adjamé Nord-est'),
    ('Qeb', 'Quartier Ebrié'),
]

ANYAMA_AREA_CHOICES = [
    ('Att' , 'Attingué'),
    ('Ako' , ' Akoupé-Zeudji'),
    ('Aad' , 'Anyama-Adjamé'),
    ('Ebi' , 'Ebimpé'),
    ('All' , 'Allokoi'),
    ('Ado' , 'Adonko'),
    ('Aah' , 'Anyama Ahouabo'),
]

ATTECOUBE_AREA_CHOICES = [
    ('Agb' , 'Agban Attié'),
    ('At3' , 'Attécoubé 3'),
    ('Dje' , 'Djéné Ecaré'),
    ('Sae' , 'Santé Ecole'),
    ('S3r1' , 'Santé 3 Résidentiel 1'),
    ('S3r2' , 'Santé 3 Résidentiel 2'),
    ('S3e' , 'Santé 3 Extension'),
    ('Fro' , 'Fromager'),
    ('Déi' , 'Déindé'),
    ('Asa' , 'Asapsu'),
    ('Awa' , 'Awa'),
    ('Jp2' , 'Jean-Paul 2'),
    ('Sca' , 'Santé Carrefour'),
    ('Aké' , 'Akélié'),
    ('Lac' , 'Lackman'),
    ('Dou' , 'Douagoville'),
    ('Cad' , 'Camp Douane'),
    ('Jré' , 'Jérusalem Résidentiel'),
    ('Jé1' , 'Jérusalem 1'),
    ('Jé2' , 'Jérusalem 2'),
    ('Jé3' , 'Jérusalem 3'),
    ('Seb' , 'Sebroko'),
    ('Lpa' , 'La Paix'),
    ('Lag' , 'Lagune'),
    ('Esp' , 'Espoir'),
    ('Mos' , 'Mosquée'),
    ('Sjo' , 'Saint-Joseph'),
    ('Eco' , 'Ecole'),
    ('Gbe' , 'Gbebouto'),
    ('Cfo' , 'Cantonnement Forestier'),
    ('Cf1' , 'Cité Fairmont 1'),
    ('Cf2' , 'Cité Fairmont 2'),
    ('Efo' , 'Ecole Forestière'),
    ('Bid' , 'Bidjanté'),
    ('Lok','Lokodjro'),
    ('Adm' , 'Abobo-Doumé')
]

COCODY_AREA_CHOICES = [
    ('IIpa' , 'II Plateaux Aghien'),
    ('IIpcz' , 'II Plateaux carrefour ZOO '),
    ('IIpbv' , 'II Plateaux Bassin du Vallon'),
    ('Alos' , ' Angré les OSCARS'),
    ('As9b' , 'Angré Star 9 B+'),
    ('Asf' , ' Angré SCI Fandasso '),
    ('Acl' , 'Angré cité Latrille'),
    ('Acfg' , 'Angré château fin goudron'),
    ('Cda' , 'Cocody Danga'),
    ('Blok' , 'Blokosso'),
    ('Sies' , 'Sicogi-Espérance'),
]

MARCORY_AREA_CHOICES = [
    ('Abia' , 'Abia-Abety'),
    ('Abik' , 'Abia-Koumassi'),
    ('Adei' , 'Adeimin'),
    ('Alio' , 'Aliodan'),
    ('Anoum' , 'Anoumabo'),
    ('Biét' , 'Biétry'),
    ('Cham' , 'Champroux'),
    ('Gnan' , 'Gnanzoua'),
    ('Hibi' , 'Hibiscus'),
    ('Jbm' , 'Jean-Baptiste Mockey'),
    ('Kbf' , 'Kablan Brou Félix'),
    ('Kra' , 'Konan Raphaël'),
    ('Mko' , 'Marie Koré'),
    ('Rési' , 'Résidentiel'),
    ('Zon4' , 'Zone 4 C'),
    ]

    KOUMASSI_AREA_CHOICES = [
        ('Sko'  , 'SICOGI- Koumassi'),
        ('Prk'  , 'Prodomo-Koumassi'),
        ('Sopk'  , 'Sopim-Koumassi'),
        ('Sogk'  , 'SOGEFIHA-Koumassi'),
    ]

    TREICHVILLE_AREA_CHOICES = [
        ('Apol' , 'Apollo'),
        ('Arra' , ' Arras'),
        ('Biaf' , ' Biafra'),
        ('Bell' , 'Belleville'),
    ]

    YOPOUGON_AREA_CHOICES = [
        ('Béag' , 'Béago'),
        ('Kouv' , 'Kouté village'),
        ('Ayapb' , 'Ayakro-Petit Bouaké'),
        ('Yopk' , 'Yopougon kouté'),
        ('Niad' , 'Niangon Adjamé'),
        ('Niat' , 'Niangon Attié'),
        ('Adio' , 'Adioppodoumé'),
        ('Nilo' , 'Niangon Lokoua'),
        ('Ilbo' , 'ILES Boulay'),
        ('Kofe' , 'Konan Ferrand'),
        ('Azsi' , 'Azito-Sikasso'),
        ('Yosa' , 'Yopougon Santé')
    ]


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='Pseudo : ',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Pseudo',
                'placeholder': 'Entrez votre pseudo',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    first_name = forms.CharField(
        label='Prénom : ',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Prenom',
                'placeholder': 'Entrez votre Prénom',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    last_name = forms.CharField(
        label='Nom : ',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Nom',
                'placeholder': 'Entrez votre Nom',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    email = forms.EmailField(
        label='Email : ',
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Email',
                'placeholder': 'Adresse électronique',
                'id': 'lo_em',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    contact = forms.CharField(
        label='Contact : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Contact',
                'placeholder': 'Exemple : 00-00-00-00',
                'id': 'lo_nu',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    password = forms.CharField(
        label='Mot de passe : ',
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Mot de passe',
                'placeholder': 'Mot de passe',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    password_verification = forms.CharField(
        label='Vérification : ',
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Vérification',
                'placeholder': 'Entrez votre mot de passe à nouveau',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )


class SignInForm(SignUpForm):
    first_name = None
    last_name = None
    email = None
    contact = None
    password_verification = None


class EditClientForm(forms.Form):
    username = forms.CharField(
        label='Pseudo ',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Pseudo',
                'placeholder': 'Entrez votre pseudo',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    first_name = forms.CharField(
        label='Prénom ',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Prenom',
                'placeholder': 'Entrez votre Prenom',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    last_name = forms.CharField(
        label='Nom ',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Nom',
                'placeholder': 'Entrez votre Nom',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    email = forms.EmailField(
        label='Email ',
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Email',
                'placeholder': 'Adresse électronique',
                'id': 'lo_em',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    contact = forms.CharField(
        label='Contact ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Contact',
                'placeholder': 'Ex : +225 00-00-00-00-00',
                'id': 'lo_nu',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    password = forms.CharField(
        label='Mot de passe ',
        required=False,
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Mot de passe',
                'placeholder': 'Nouveau mot de passe',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    password_verification = forms.CharField(
        label='Vérification ',
        required=False,
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Vérification',
                'placeholder': 'Entrez le à nouveau',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    rent_proposal = forms.IntegerField(
        label='Budget loyer',
        required=False
    )
    deposit_proposal = forms.IntegerField(
        label='Budget caution',
        required=False
    )
    avatar = forms.ImageField(
        label='Avatar ',
        required=False
    )


class EditLandlordForm(EditClientForm):
    deposit_proposal = None
    rent_proposal = None


class AddHouseForm(forms.Form):
    house_township = forms.CharField(
        max_length=50,
        label='Commune : ',
        widget=forms.Select(
            choices = TOWNSHIP_CHOICES,
            attrs={
                'class': 'form-control',
                'placeholder': 'Commune de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_area = forms.CharField(
        max_length=50,
        label='Quartier : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_rent = forms.IntegerField(
        label='Prix : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Prix du Loyer',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_deposit = forms.IntegerField(
        label='Caution : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Caution de la caution',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_kind = forms.CharField(
        max_length=50,
        label='Type : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type de maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_rooms_number = forms.IntegerField(
        label='Pièces : ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de pièces',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    house_available = forms.BooleanField(
        label='En location : ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_cl',
            }
        )
    )
    house_to_sell = forms.BooleanField(
        label='À vendre : ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_cl',
            }
        )
    )
    house_image = forms.ImageField(
        label='Image',
        required=False
    )


class ClientProposalForm(AddHouseForm):
    house_available = None
    house_to_sell = None
    house_image = None
