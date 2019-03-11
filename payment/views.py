# import braintree
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from orders.models import Order,OrderItem
from django.conf import settings

from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
import juspayp3 as Juspay
from random import randint
import json

# Create your views here.
# braintree.Configuration.configure(braintree.Environment.Sandbox,
#     merchant_id=settings.BRAINTREE_MERCHANT_ID,
#     public_key=settings.BRAINTREE_PUBLIC_KEY,
#     private_key=settings.BRAINTREE_PRIVATE_KEY)


    # if request.method=="POST":
    #     nonce=request.POST.get('payment_method_nonce',None)

    #     result=braintree.Transaction.sale({'amount':'{:.2f}'.format(order.get_total_cost()),
    #                                         'payment_method_nonce':nonce,
    #                                         'options':{'submit_for_settlement':True}
    #                                         })
    #     if result.is_success:
    #         order.paid=True

    #         order.braintree_id=result.transaction.id
    #         order.save()
    #         return redirect('payment:done')
    # else:
    #     client_token=braintree.ClientToken.generate()
    #        
    # paypal_dict = {
    #    'business': settings.PAYPAL_RECEIVER_EMAIL ,
    #     # 'business':"amit.kadivar3@gmail.com",
    #    'amount': order.get_total_cost(),
    #     # 'amount':'1000000',
    #     'item_name': 'name',
    #     'invoice': 'Test Payment Invoice',
    #     # 'notify_url': 'http://{}{}'.format(host, reverse('payment:paypal-ipn')),
    #     # 'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
    #     # 'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    # #    'currency_code': 'INR',
    # #    'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
    # #    'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
    # #    'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    #    }
    # Juspay.api_key="3DB047B7006E4369A985EA299A8C286C"
    # Juspay.environment = 'production'

    # juspay.environment = 'production'
    # customer_id=Juspay.Customers.list()
    # for customer in customer_id:
    #     print(customer)
    # print(customer_id[list])
    # my_new_order = Juspay.Orders.create(customer_id='guest_user_101',
	# 	customer_email='customer@gmail.com',
	# 	customer_phone='9988665522',
    #     order_id=order_id_gen,
    #     amount=1,
    #     status="CHARGED",
    #     return_url='http://{}{}'.format(host,reverse('payment:response')))  
    # print("juspay order ",my_new_order)
    # payment=vars(my_new_order)
    # print(payment)
    # links=vars(my_new_order.payment_links)
    # web_links=links['web']
    # print()
    # form = PayPalPaymentsForm(initial=paypal_dict)
    # return render(request, 'pets/payment_process.html', {'form': form })*
import razorpay
client =razorpay.Client(auth=(settings.RAZORPAY_PUBLIC_KEY,settings.RAZORPAY_SECRET_KEY))
client.set_app_details({"title" : "Django", "version" : "1.8.17"})
amount=0
def create_order(request):
    order_id=request.session.get('order_id')
    order=get_object_or_404(Order,id=order_id)
    amount=int(order.get_total_cost()*100)
    amount_inr=amount//100
    print("Type amount ",amount)
    print("Type amount ",type(amount))
    print("Order is -> ",order)
    return render(request,'payment/created.html',{'order_id':order_id,'public_key':settings.RAZORPAY_PUBLIC_KEY,'amount':amount_inr,'amountorig':amount})
    #order detail
    # payment_process view 
    # order_id=request.session.get('order_id')
    # order=get_object_or_404(Order,id=order_id)
    # host = request.get_host()
    # order_id_gen=randint(100000,200000)
    # data={'amount':100,'currency':"INR","receipt":str(order_id_gen),"payment_capture":0}
    # client.order.create(data=data)
    # client_order=client.order.fetch(str(order_id_gen))

def payment_process(request):
    order_id=request.session.get('order_id')
    order=get_object_or_404(Order,id=order_id)
    print("Payment",order)
    if request.method=="POST":
        order.paid=True
        
        order.save()
        print("Payment order",order.paid)
        orderitem=get_object_or_404(OrderItem,order=order)
        print("Order Item",orderitem.get_cost())
        amount=int(orderitem.get_cost())*100
        amount_inr=amount//100
        print("Amount ",amount)
        print("Type amount str to int ",amount)
        payment_id=request.POST['razorpay_payment_id']
        order.braintree_id=payment_id
        order.save()
        # print("Multiple value",payment_id)
        print("Payment Id",payment_id)
        payment_client_capture=(client.payment.capture(payment_id,amount))    
        print("Payment Client capture",payment_client_capture)
        payment_fetch=client.payment.fetch(payment_id)
        status=payment_fetch['status']
        amount_fetch=payment_fetch['amount']
        amount_fetch_inr=amount_fetch//100
        print("Payment Fetch",payment_fetch['status'])
        return render(request,'payment/done.html',{'amount':amount_fetch_inr,'status':status})   
    # else:
    #     return render(request, 'payment/done.html',{"amount":"Get Method"})

        
    # return redirect(web_links)
def payment_done(request):
    return render(request, 'payment/done.html',{})
 
 
def payment_canceled(request):
    return render(request, 'payment/canceled.html',{})

def response(request):
    res=dict()
    res['order_id']=request.GET.get('order_id')
    res['status']=request.GET.get('status')
    res['signature']=request.GET.get('signature')
    res['signature_algorithm'] = request.GET.get('signature_algorithm')
    print(res)
    return render(request,'payment/done.html',{'res':res})