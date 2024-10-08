import pandas as pd
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

gerentes_df = pd.read_excel(r'Python\projeto_integração_email\Enviar E-mails.xlsx')

for i, email in enumerate(gerentes_df["E-mail"]):
    gerente = gerentes_df.loc[i, 'Gerente']
    area = gerentes_df.loc[i, 'Relatório']
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = f"Relatório de {area}"
    mail.Body = f'''Olá {gerente}, tudo bem?
    Conforme solicitado, segue o relatório de {area} em anexo.
    Qualquer dúvida estou à disposição
    Att,
    Lucas Lopes'''
    attachment = rf'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_integração_email\{area}.xslx'
    mail.Attachments.Add(Source=attachment)
    mail.display()
    mail.send()

