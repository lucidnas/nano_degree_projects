from twilio.rest import Client

account_sid = "AC6c338c6372f1198f1f77631890947e4f"
auth_token = "b04046732e45c0359b1b47f6f6dcf9fe"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Hello Twilio!",
    to= "+13476100639",
    from_="+12019493976"
)
print message.sid