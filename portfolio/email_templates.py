SENDER_SUMMARY_SUBJECT = (
    "Confirmation du message envoyé à Emmanuel Oudot"
)
SENDER_SUMMARY_MESSAGE = (
    "Bonjour,\n"
    "Je vous remercie pour votre message, "
    "je vous répondrai le plus rapidement possible.\n\n"
    "Si besoin vous pouvez télécharger mon cv à cette adresse :\n"
    "{}\n\n"
    "Je suis également joignable par téléphone :\n"
    "{}\n\n"
    "Cordialement\nEmmanuel Oudot\n\n"
    "_______________________________________________________________\n"
    "Rappel du message ({}):\n\n"
    "Sujet:\n"
    "   {}\n"
    "Message : \n"
    "   {}\n\n"
    "_______________________________________________________________\n"
    "www.emmanuel-oudot.fr | contact@emmanuel-oudot.fr"
)#.format(CV_LINK, PHONE_NUMBER, now, subject, message)

MSG_FOR_ME_SUBJECT = "[Urgent] Nouveau message depuis le portfolio"
MSG_FOR_ME_CONTENT = (
"{} - Nouveau messages :\n"
"Nom: \n{}\n"
"Email: \n{}\n"
"Sujet: \n{}\n"
"Message: \n{}\n"
)#.format(datetime.now(),name,email,subject,message)
