from login_signup.views import *
from django.urls import path
from login_signup import views
from login_signup.views.auth import *

app_name="login_signup"

urlpatterns=[

    path('logout/', logout_view, name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
]