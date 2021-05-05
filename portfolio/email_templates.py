SENDER_SUMMARY_SUBJECT = (
    "Confirmation du message envoyé sur www.emmanuel-oudot.fr"
)
SENDER_SUMMARY_MESSAGE = (
    "Bonjour,\n"
    "Je vous remercie pour votre message, "
    "je vous répondrai le plus rapidement possible.\n\n"
    "Cordialement\nEmmanuel Oudot\n\n"
    "Rappel du message ({}):\n"
    "Sujet:\n"
    "   {}\n"
    "Message : \n"
    "   {}\n\n"
    "www.emmanuel-oudot.fr | contact@emmanuel-oudot.fr"
)#.format(now, subject, message)

MSG_FOR_ME_SUBJECT = "[Urgent] Nouveau message depuis le portfolio"
MSG_FOR_ME_CONTENT = (
"{} - Nouveau messages :\n"
"Nom: \n{}\n"
"Email: \n{}\n"
"Sujet: \n{}\n"
"Message: \n{}\n"
)#.format(datetime.now(),name,email,subject,message)
