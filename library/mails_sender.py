from django.utils import timezone
import os
from library.models import Borrower
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def remainder():
    borrowes = Borrower.objects.filter()

    for borrower in borrowes:
        if borrower.date_of_delivery <= timezone.now():
            message = Mail(
                from_email='django.library@gmail.com',
                to_emails=f'{borrower.e_mail}',
                subject='Sending with Twilio SendGrid is Fun',
                html_content=f'Czesc {borrower.user.first_name},'
                             f'Nie oddales na czas ksiazki pod tytulem {borrower.book.book_title}.'
                             f'Przypominam ze termin oddania ksiazki przypadal na {borrower.date_of_delivery}.'
                             f'Pozdrawiamy Zabka')
            try:
                sg = SendGridAPIClient(os.environ.get('EMAIL_PASSWORD'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)








