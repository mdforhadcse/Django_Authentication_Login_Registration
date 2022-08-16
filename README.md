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