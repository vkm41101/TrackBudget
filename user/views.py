from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from user.models import *
from user.forms import NewUserForm
import time


# Create your views here.
def recharge(request, mobileNumber, amount):
    querySet = list(User.objects.filter(MobileNumber=mobileNumber))
    reqUser = querySet[0]
    reqUser.walletTransac += int(amount)
    reqUser.save()
    print('Recharge')
    return HttpResponse(status=201)


def generateIdAtTheMoment():
    return str(hex(int(time.time() * 1000)))[2:]


def addFriend(request, requestSender, requestReciever):
    friendship = Friendship(friendshipId=generateIdAtTheMoment(), MobileNumber1=requestSender,
                            MobileNumber2=requestReciever)
    friendship.save()
    friendship = Friendship(friendshipId=generateIdAtTheMoment(), MobileNumber1=requestReciever,
                            MobileNumber2=requestSender)
    friendship.save()
    return HttpResponse(status=201)


def makeTransaction(request, transactionFrom, transactionTo, amount):
    userFrom = None
    userTo = None
    try:
        userFrom = list(User.objects.filter(MobileNumber=transactionFrom))[0]
        userTo = list(User.objects.filter(MobileNumber=transactionTo))[0]
    except:
        return HttpResponse("<h1> 404:User Not Found </h1>", status=404)
    balance = userFrom.walletTransac
    if balance < amount:
        return HttpResponse("<h1>400:Insufficient Balance (Bad Request)</h1>")
    userFrom.walletTransac -= amount
    userTo.walletTransac += amount

    transaction = Transaction(transactionId=generateIdAtTheMoment(), transactionFrom=transactionFrom,
                              transactionTo=transactionTo, transactionAmount=amount)
    transaction.save()

    return HttpResponse(status=200)


def addPendingTransaction(request, transactionRequestFrom, transactionRequestTo, transactionRequestAmount):
    pendingtransaction = pendingTransaction(pendingTransactionId=generateIdAtTheMoment(),
                                            transactionFrom=transactionRequestFrom, transactionTo=transactionRequestTo,
                                            transactionAmount=transactionRequestAmount)
    pendingtransaction.save()
    return HttpResponse(status=200)


def findUser(request, MobileNumber):
    userFound = list(User.objects.filter(MobileNumber=MobileNumber))
    data = serialize('json', userFound, fields=('name', 'dob'))
    return HttpResponse(data, content_type='application/json')


def getFriends(request, MobileNumber):
    userFriends = Friendship.objects.filter(MobileNumber1=MobileNumber)
    data = serialize('json', userFriends)
    return HttpResponse(data, content_type='application/json')


def getPendingTransactions(request, MobileNumber):
    transactionsRemaining = pendingTransaction.objects.filter(transactionFrom=MobileNumber)
    data = serialize('json', transactionsRemaining)
    return HttpResponse(data, content_type='application/json')


def removePendingTransactions(request, pendingTransactionId):
    transactionRem = pendingTransaction.objects.filter(pendingTransactionId=pendingTransactionId)
    transactionRem.delete()
    return HttpResponse(status=201)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponse("<h1>Success</h1>")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            MobileNumber = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(MobileNumber)
            print(password)
            user = authenticate(MobileNumber=MobileNumber, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {MobileNumber}.")
                return HttpResponse("<h1>Logged In</h1>")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponse(status=200)
