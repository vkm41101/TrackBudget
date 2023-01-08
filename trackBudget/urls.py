"""trackBudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recharge/<mobileNumber>/<amount>', views.recharge),
    path('friendRequest/<requestSender>/<requestReciever>', views.addFriend),
    path('payTo/<transactionFrom>/<transactionTo>/<amount>', views.makeTransaction),
    path('addPendingTransaction/<transactionRequestFrom>/<transactionRequestTo>/<transactionRequestAmount>',
         views.addPendingTransaction),
    path('pendingTransactions/<MobileNumber>', views.getPendingTransactions),
    path('findUser/<MobileNumber>', views.findUser),
    path('findFriendsOfUser/<MobileNumber>', views.getFriends),
    path('register', views.register_request),
    path('login', views.login_request),
    path('logout', views.logout_request),
]
