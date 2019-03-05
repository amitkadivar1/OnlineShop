from django.urls import path,re_path,include
from . import views

app_name='payment'

urlpatterns = [
    path('process/',views.create_order,name="process"),
    path('response/',views.payment_process,name="response"),
    # path('response/',views.response,name="response"),
    path('canceled/',views.payment_canceled,name="canceled"),
    re_path(r'^paypal/', include('paypal.standard.ipn.urls'),name="paypal-ipn"),
    # re_path(r'^payment_process/$', api_views.payment_process, name='payment_process' ),

    # re_path(r'^payment_done/$', TemplateView.as_view(template_name= "pets/payment_done.html"), name='payment_done'),

    # re_path(r'^payment_canceled/$', TemplateView.as_view(template_name= "pets/payment_canceled.html"), name='payment_canceled'),
    

]
