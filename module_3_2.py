def send_mail(recipient, messege, sender ='university.help@gmail.com'):
    if '@' not in recipient:
        checker = False
    elif '.ru' or '.com' or '.net' in recipient:
        checker = True
    else:
        checker = True

    if checker == False:            #чего это он ругается?

        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)

    elif sender == recipient:

        print('Нельзя отправить письмо самому себе!')

    elif sender == 'university.help@gmail.com':

        print('Письмо успешно отправлено с адреса ', sender,  ' на адрес ', recipient)

    elif sender != 'university.help@gmail.com':

        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender,  ' на адрес ', recipient)

send_mail('universitygmail.com', 'Здравствуйте!')
send_mail('university.help@gmail.com', 'Здравствуйте!')
send_mail('university@gmail.com', 'Здравствуйте!')
send_mail('university@gmail.com', 'Здравствуйте!','none@mail.ru')
