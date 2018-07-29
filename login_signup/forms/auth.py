from django import forms



class SignUpForm(forms.Form):

    status_flag = forms.IntegerField(

        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status Flag 0 for Customer and 1 for Seller'})
    )

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    phno = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phno'})
    )
    email = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email id'})
    )
    dob=forms.DateField(


        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dob'})
    )


class SignUpSellerForm(forms.Form):

    status_flag = forms.IntegerField(

        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    phno = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phno'})
    )
    email = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email id'})
    )
    dob=forms.DateField(


        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dob'})
    )



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )