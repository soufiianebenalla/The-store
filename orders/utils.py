from django.template.loader import render_to_string


def send_order_email(request, user, order):

    subject = f'Order with nr. {{ order.id }}, is Successfuly Completed.'

    context = {
        'user': user,
        'order': order,
        'products': order.items.all(),
        # 'total_price': order.total_price()
    }
    message = render_to_string('orders/order_email.html', context)

    user.email_user(subject, message)
