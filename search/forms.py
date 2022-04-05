from django import forms


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select District"),
        ("Alappuzha","Alappuzha"),
        ("Ernakulam","Ernakulam"),
        ("Idukki","Idukki"),
        ("Kannur","Kannur"),
        ("Kasaragod","Kasaragod"),
        ("Kollam","Kollam"),
        ("Kottayam","Kottayam"),
        ("Kozhikode","Kozhikode"),
        ("Malappuram","Malappuram"),
        ("Palakkad","Palakkad"),
        ("Pathanamthitta","Pathanamthitta"),
        ("Thiruvananthapuram","Thiruvananthapuram"),
        ("Thrissur","Thrissur"),
        ("Wayanad","Wayanad"),
        
    )
    select_blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    
    

