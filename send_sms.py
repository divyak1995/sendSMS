from twilio.rest import Client
from credentials import *

client=Client(account_sid, auth_token)

my_msg=''.join(['Good Night\n' for i in range(10)])

message=client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)


print(message.sid)
