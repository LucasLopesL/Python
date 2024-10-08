import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = "lucaslopesfnance@gmail.com"
mail.Subject = "Integração Python"
mail.Text = "Teste para validação do script Python para automação de envio de e-mail"
# mail.HTMLBody = "<h1>Título</h1>\n<h1>Teste para validação do script Python para automação de envio de e-mail</h1>"
attachments = r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_integracao-pastas\Arquivos_Lojas\201801_Amazonas Shopping_AM.csv'
mail.Attachments.Add(attachments)

mail.Send()
