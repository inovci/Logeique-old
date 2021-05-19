from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(
        label='Pseudo : ',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Pseudo',
                'placeholder': 'Entrez votre pseudo'
            }
        )
    )
    first_name = forms.CharField(
        label='Prenom : ',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Prenom',
                'placeholder': 'Entrez votre Prenom'
            }
        )
    )
    last_name = forms.CharField(
        label='Nom',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Nom',
                'placeholder': 'Entrez votre Nom'
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
                'placeholder': 'Entrez votre addresse electronique',
                'id': 'lo_em'
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
                'id': 'lo_nu'
            }
        )
    )
    client = forms.BooleanField(
        label='Client : ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_cl'
            }
        )
    )
    landlord = forms.BooleanField(
        label='Propriétaire : ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_la'
            }
        )
    )
    password = forms.CharField(
        label='Mot de passe :',
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Mot de passe',
                'placeholder': 'Entrez votre mot de passe'
            }
        )
    )
    password_verification = forms.CharField(
        label='Vérification',
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Vérification',
                'placeholder': 'Entrez votre mot de passe à nouveau'
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
        label='Pseudo : ',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Pseudo',
                'placeholder': 'Entrez votre pseudo'
            }
        )
    )
    first_name = forms.CharField(
        label='Prenom : ',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Prenom',
                'placeholder': 'Entrez votre Prenom'
            }
        )
    )
    last_name = forms.CharField(
        label='Nom',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Nom',
                'placeholder': 'Entrez votre Nom'
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
                'placeholder': 'Entrez votre addresse electronique',
                'id': 'lo_em'
            }
        )
    )
    contact = forms.CharField(
        label='Contact : ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Contact',
                'placeholder': 'Exemple : + 225 00-00-00-00',
                'id': 'lo_nu'
            }
        )
    )
    password = forms.CharField(
        label='Mot de passe :',
        required=False,
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Mot de passe',
                'placeholder': 'Entrez votre mot de passe'
            }
        )
    )
    password_verification = forms.CharField(
        label='Vérification',
        required=False,
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control inbox',
                'title': 'Vérification',
                'placeholder': 'Entrez votre mot de passe à nouveau'
            }
        )
    )
    rent_proposal = forms.IntegerField(
        label='budget loyer',
        required=False
    )
    deposit_proposal = forms.IntegerField(
        label='budget caution',
        required=False
    )
    avatar = forms.ImageField(
        label='ajoute avatar',
        required=False
    )

class EditLandlordForm(EditClientForm):
    deposit_proposal = None
    rent_proposal = None


class AddHouseForm(forms.Form):
    house_township = forms.CharField(
        max_length=50,
        label='Commune de la maison: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Commune'
            }
        )
    )
    house_area = forms.CharField(
        max_length=50,
        label='Quartier de la maison: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quartier'
            }
        )
    )
    house_rent = forms.IntegerField(
        label='Prix du loyer de la maison: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Montant du Loyer'
            }
        )
    )
    house_deposit = forms.IntegerField(
        label='Caution de la maison: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Montant de la caution'
            }
        )
    )
    house_kind = forms.CharField(
        max_length=50,
        label='Type de maison: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type de maison'
            }
        )
    )
    house_rooms_number = forms.IntegerField(
        label='Nombres de pieces: ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de pièces'
            }
        )
    )
    house_available = forms.BooleanField(
        label='Disponible: ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_cl',
                'type': 'radio'
            }
        )
    )
    house_to_sell = forms.BooleanField(
        label='A vendre: ',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input stick',
                'onclick': 'active()',
                'id': 'is_cl',
                'type': 'radio'
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
