from imap_tools import MailBox, AND, OR, NOT

username = "seu e-mail"
password = "sua senha"
email = MailBox("imap.gmail.com").login(username, password)

lista_email = email.fetch(AND(from_='E-mail de quem te enviou', to='Pra quem foi enviado o e-mail', subject='Assunto do e-mail'))
for email in lista_email:
    print(email.subject)
    print(email.text)
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "Nome do arquivo" in anexo.filename:
                info_anexo = anexo.payload
                with open('Relatorio.xlsx', 'wb') as arquivo:
                    arquivo.write(info_anexo)