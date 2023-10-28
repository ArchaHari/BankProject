from django import forms

class regform(forms.Form):
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    image=forms.FileField()
    pin=forms.CharField(max_length=20)
    rpin=forms.CharField(max_length=20)

class logform(forms.Form):
    username=forms.CharField(max_length=50)
    pin=forms.CharField(max_length=20)

class newsfeedform(forms.Form):
    topic=forms.CharField(max_length=50)
    content=forms.CharField(max_length=1000)
    image=forms.FileField()

class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


# class ministatementform(forms.Form):
#     dropdown=forms.CharField(max_length=30)