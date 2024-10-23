from twilio.rest import Client


account_sid = "ACbe3bfb7accbd49859ce291ecf47c45a1"
account_token = "61264c82e0d1758b2f307b94eaf141fc"
client = Client(account_sid, account_token)

message = client.messages.create(
  from_='+18647218530',
  to='+5511989792260',
  body = "Olá Lucas"
)

print(message.sid)