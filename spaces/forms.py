from django import forms

from .forms_constants import STATUS_CHOICES , TOWNSHIP_CHOICES , ABOBO_AREA_CHOICES ,ADJAME_AREA_CHOICES,ANYAMA_AREA_CHOICES ,ATTECOUBE_AREA_CHOICES , COCODY_AREA_CHOICES ,MARCORY_AREA_CHOICES ,KOUMASSI_AREA_CHOICES , TREICHVILLE_AREA_CHOICES , YOPOUGON_AREA_CHOICES , TYPE_CHOICES


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
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
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
    abobo_areas = forms.CharField(
        max_length=50,
        label='Quartiers Abobo : ',
        widget=forms.Select(
            choices  = ABOBO_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    adjame_areas = forms.CharField(
        max_length=50,
        label='Quartiers Attecoube : ',
        widget=forms.Select(
            choices  = ATTECOUBE_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    """bingerville_areas = forms.CharField(
        max_length=50,
        label='Quartiers Attecoube : ',
        widget=forms.Select(
            choices  = BINGERVILLE_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )"""
    cocody_areas = forms.CharField(
        max_length=50,
        label='Quartiers cocody : ',
        widget=forms.Select(
            choices  = COCODY_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    koumassi_areas = forms.CharField(
        max_length=50,
        label='Quartiers Koumassi : ',
        widget=forms.Select(
            choices  = KOUMASSI_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    marcory_areas = forms.CharField(
        max_length=50,
        label='Quartiers Marcory : ',
        widget=forms.Select(
            choices  = MARCORY_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    """plateau_areas = forms.CharField(
        max_length=50,
        label='Quartiers Plateau : ',
        widget=forms.Select(
            choices  = PLATEAU_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )"""
    """port_boue_areas = forms.CharField(
        max_length=50,
        label='Quartiers Port-Bouet : ',
        widget=forms.Select(
            choices  = ATTECOUBE_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )"""
    """songo_areas = forms.CharField(
        max_length=50,
        label='Quartiers Songon : ',
        widget=forms.Select(
            choices  = SONGON_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )"""
    treichville_areas = forms.CharField(
        max_length=50,
        label='Quartiers Attecoube : ',
        widget=forms.Select(
            choices  = TREICHVILLE_AREA_CHOICES , 
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier de la maison',
                'style': 'border-top: 0rem;border-left: 0rem;border-right: 0rem; font-size:15px;'
            }
        )
    )
    yopougon_areas = forms.CharField(
        max_length=50,
        label='Quartiers Yopougon : ',
        widget=forms.Select(
            choices  = YOPOUGON_AREA_CHOICES , 
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
        widget=forms.Select(
            choices = TYPE_CHOICES,
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
