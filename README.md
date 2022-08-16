### Adding static and media folder to django project
<hr>
Go to settings.py and Write following code

    BASE_DIR = Path(__file__).resolve().parent.parent


    # Static files (CSS, JavaScript, Images)
    STATIC_URL = "static/"
    STATICFILES_DIRS = (BASE_DIR / "static",)

    # Media
    MEDIA_URL = "media/"
    MEDIA_ROOT = (BASE_DIR / "media",)


### Adding django model to admin panel
To view specific model's database in the admin dashboard:
<br>
Go to admin.py of your app folder and write

    from Login_app.models import UserInfo

    # Register your models here.
    admin.site.register(UserInfo)

### Creating django form
To make a form in our django application, django provide us built in facility make it easy.
First we create forms.py in our application folder and write following codes:

    from django import forms
    from django.contrib.auth.models import User
    from Login_app.models import UserInfo


    class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ('username', 'email', 'password')


    class UserInfoFrom(forms.ModelForm):
        class Meta:
            model = UserInfo
            fields = ('facebook_id', 'profile_picture')