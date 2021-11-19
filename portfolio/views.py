import os

from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render
from smtplib import SMTPException

from portfolio.models import DeniedWordsManager

from portfolio_config.settings.common import (
    DEFAULT_FROM_EMAIL,
    MY_MAIL,
    PHONE_NUMBER,
    CV_LINK
)
from portfolio.forms import ContactForm
from portfolio.email_templates import (
    SENDER_SUMMARY_SUBJECT,
    SENDER_SUMMARY_MESSAGE,
    MSG_FOR_ME_SUBJECT,
    MSG_FOR_ME_CONTENT
)

denied_words = DeniedWordsManager()

def homepage(request):
    if request.method == 'POST':
        message_is_valid = True
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            """Get form data"""
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            """ check the content of the email """
            for denied in denied_words.in_email():
                if denied.word in email:
                    messages.error(request,f'Vous ne pouvez pas utiliser un Email contenant {denied.word}')
                    message_is_valid = False
            """ check the content of the message """
            for denied in denied_words.in_message():
                if denied.word in message:
                    messages.error(request,f'Vous ne pouvez pas utiliser \"{denied.word}\" dans votre message')
                    message_is_valid = False
            """ send messages if valid """
            if message_is_valid:
                """ formated date and time """
                raw_now = datetime.now()
                now=f'{raw_now:%d/%m/%Y %H:%M}'
                """ builds the principal message """
                msg_for_me_content = MSG_FOR_ME_CONTENT.format(
                                    now, name, email, subject, message
                                    )
                """ sends principal message """
                try:
                    send_mail(
                        MSG_FOR_ME_SUBJECT,
                        msg_for_me_content,
                        DEFAULT_FROM_EMAIL,
                        [MY_MAIL]
                    )
                    messages.success(
                        request,"Votre message a été envoyé à Emmanuel"
                    )
                except SMTPException as smtp_error:
                    messages.error(
                        request,"Un problème est survenu\n({})".format(smtp_error)
                    )
                except BadHeaderError:
                    messages.error(request,"En-tête non valide")

                """ builds sender's summary message """
                summary_message = SENDER_SUMMARY_MESSAGE.format(
                            CV_LINK, PHONE_NUMBER, now, subject, message
                            )
                """ sends summary message """
                try:
                    send_mail(
                        SENDER_SUMMARY_SUBJECT,
                        summary_message,
                        DEFAULT_FROM_EMAIL,
                        [email]
                    )
                    messages.success(
                        request,
                        "Un message de confirmation a été envoyé a {}".format(
                            email)
                    )
                except SMTPException as smtp_error:
                    messages.error(
                        request,"Un problème est survenu\n({})".format(smtp_error)
                    )
                except BadHeaderError:
                    messages.error(request,"En-tête non valide")

    context = {
        'contact_form': ContactForm(),
    }

    return render(request, 'homepage.html', context)
