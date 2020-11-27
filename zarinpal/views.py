from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Transaction
from .forms import TransactionForm

from .zp import Zarinpal, ZarinpalError

'''
 if you want to test youre code on your machine without a real transaction
 you able to use zarinpal sandbox like following code
 if you want use in your product, remove sandbox and replace real mercand and callback url then use it!
'''
zarin_pal = Zarinpal('XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 
                    'http://127.0.0.1:8000/verify',
                    sandbox = True)

def index(request):
    return render(request, 'zarinpal/pay.html')

def pay(request: HttpRequest):

    amount = request.POST.get('amount')
    description = request.POST.get('description')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')

    try:
        # try to create payment if success get url to redirect it
        redirect_url = zarin_pal.payment_request(amount, description, mobile=mobile, email=email)
        form = TransactionForm(request.POST)
        if form.is_valid():

            # create new transaction and save it
            new_transaction = Transaction()
            new_transaction.description = description
            new_transaction.amount = amount
            new_transaction.mobile = mobile
            new_transaction.authority = zarin_pal.authority
            new_transaction.email = email
            new_transaction.save()

            # redirect user to zarinpal payment gate to paid
            return redirect(redirect_url)

        # this showing erro not safe!
        return HttpResponse(form.errors.as_json())

    # if got error from zarinpal 
    except ZarinpalError as e:  
        return HttpResponse(e)

def verify(request):

    if request.GET.get('Status') == 'OK':
        authority = int(request.GET['Authority'])
        try:
            # try to found transaction
            try:
                transaction = Transaction.objects.get(authority=authority)

            # if we couldn't find the transaction
            except ObjectDoesNotExist:
                return HttpResponse('we can\'t find this transaction')

            code, message, ref_id = zarin_pal.payment_verification(transaction.amount, authority)

            # everything is okey 
            if code == 100:
                transaction.reference_id = ref_id
                transaction.save()
                content = {
                    'type' : 'Success',
                    'ref_id' : ref_id
                    }
                return render(request, 'zarinpal/transaction_status.html', context=content)
            # operation was successful but PaymentVerification operation on this transaction have already been done
            elif code == 101:
                content = {
                    'type' : 'Warning'
                    }
                return render(request, 'zarinpal/transaction_status.html', context=content)

        # if got an error from zarinpal
        except ZarinpalError as e:
            return HttpResponse(e)
    
    return render(request, 'zarinpal/transaction_status.html')

def transactions(request):
    all_transaction = Transaction.objects.all()
    content = {
        'transactions' : all_transaction
    }
    return render(request, 'zarinpal/transactions.html', context=content)