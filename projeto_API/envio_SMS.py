from twilio.rest import Client


account_sid = "XXXXXXXXXXXXXX"
account_token = "XXXXXXXXXXXXXX"
client = Client(account_sid, account_token)

message = client.messages.create(
  from_='+18647218530',
  to='+5511989792260',
  body = "Olá Lucas"
)

print(message.sid)