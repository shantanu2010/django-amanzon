from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

from datetime import datetime
from threading import Timer
import threading

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import requests



@login_required
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

            mail=order.email
            phone=order.phone_no

            sender(mail,order.id)
            print("mail sent")
            smssender(phone,order.id)



            return render(request, 'orders/order/created.html', {'order': order})

        return render(request, 'orders/order/create.html', {'form': form})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


def sender(mail,id):

    msg=""
    msg = '<head><style>body{background-color:blue;} p{color:yellow; align : center; font-style: italic;font-size: 30px;font-weight: bold;} th{color:blue;}</style></head> <body style="background-color:powderblue;">'

    msg+="hello ur id is"+str(id)

    msg += '</body></html>'

    gmailaddress = 'shantanu.bhavanasi@gmail.com'
    gmailpassword = 'shasamvengopnih55$'
    mailto = mail


    try:
        client = None
        message = MIMEMultipart('alternative')
        message['from'] = gmailaddress
        message['to'] = mailto
        message['subject'] = f'admin from amazon '
        part1 = MIMEText(msg, 'html')
        message.attach(part1)
        client = smtplib.SMTP("smtp.gmail.com", 587)
        client.ehlo()
        client.starttls()
        client.login(gmailaddress, gmailpassword)
        msg = message.as_string()
        client.sendmail(gmailaddress, mailto, msg)

    except smtplib.SMTPAuthenticationError:

        return
    except smtplib.SMTPDataError:

        return
    except smtplib.SMTPConnectError:

        return
    except smtplib.SMTPNotSupportedError:

        return
    except smtplib.SMTPException:

        return



def smssender(phno,id):


    url = "https://www.fast2sms.com/dev/bulk"
    s = str(phno)
    msg = "Welcome to MyOnlineStore\n,Your Order id is : "+str(id)
    payload = "sender_id=FSTSMS&message=" + msg + "&language=english&route=p&numbers=" + s
    headers = {
        'authorization': "ST4UoGmi9IwHxXrLdKyBR2kl3vnusWNDhCfP7zEOaZ15eJjtM81nem5HptFfUxQEGJWObirvuqg9LzyZ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    print("sent")


