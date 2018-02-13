from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Hello {},\n\nYou have successfully placed an order at E-Shopper.' \
              '\nYour order id is {}.\nYou ordered {}. We will send a confirmation ' \
              'when your item ships'.format(order.first_name, OrderItem.product, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent