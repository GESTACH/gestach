from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string







def send_confirmation_email(user, password):
    # Render HTML template with user and password
    html_content = render_to_string('utilisateur_mail_inscription.html', {
        'username': user.username,
        'password': password
    })

    # Define email subject and body
    subject = 'Confirmation de votre inscription'
    message = ''

    # Send email to user
    send_mail(
        subject=subject,
        message=message,
        html_message=html_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )