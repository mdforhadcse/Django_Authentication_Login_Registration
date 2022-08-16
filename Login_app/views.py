from django.shortcuts import render
from Login_app.forms import UserForm, UserInfoFrom


# Create your views here.
def index(request):
    cont = {}
    return render(request, 'Login_app/index.html', context=cont)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_info_form = UserInfoFrom(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)    # password encryption
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_picture' in request.FILES:
                user_info.profile_picture = request.FILES['profile_picture']

            user_info.save()
            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoFrom()

    const = {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered}
    return render(request, 'Login_app/registration.html', const)
