"""

                                MULTIMESSENGER USING PYTHON

"""


from twilio.rest import Client
import smtplib
from email.message import EmailMessage
import fbchat
from fbchat import Client



print ("""-------------------------------------------------------------------------
-------------------------------------------------------------------------

			|	Multimessenger succesfully opened     		  
			|								 
			|	Built by :					 
			|					 
			|	Aman Pandey
			|   Ritu Priya Singh 
			|								 		 		  
			|	Lovely proffesional university		 		 
			|	(B.Tech CSE) - 2024			
			 		 
-------------------------------------------------------------------------
-------------------------------------------------------------------------""")





val = int(input("""
          Select your messaging option :
          EMAIL [1]  |  SMS [2]  |  FACEBOOK[3]
          """))
if (val==1):
    msg=EmailMessage()
    print("Enter the subject: ")
    msg['Subject']=input()
    print("Enter the Title Name: ")
    msg['From']=input()
    print("Enter the email IDs in which you want to send the email: ")
    msg['To']=input()
    print("Enter the message content: ")
    msg.set_content(input())
    server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("projpyth@gmail.com", "pyproj000")
    server.send_message(msg)
    server.quit()


elif(val==2) :


    my_ph_number = '+16108947383'
    acc_sid = 'AC2aac9fa89fb7f19ad7172e90e17e76d7'
    auth_token = '9764637414b249dcfe3e181ef34d6a32'
    target = '+91' + input("Enter the reciever's mobile number :")
    smsmsg=input("Type message : ")


    client = Client(acc_sid,auth_token)
    message = client.messages.create(
        body=smsmsg,
        from_= my_ph_number,
        to = target
    )

    print(message.body)

elif (val == 3):

    username = "7004864426"
    password = "doodlydoo$07"
    client = fbchat.Client(username, password)
    no_of_friends = int(input("number of friends"))
    for i in range(no_of_friends):
        name = str(input("name: "))
        friends = client.searchForUsers(name)
        friend = friends[0]
        msg = str(input("message: "))
        sent = client.send(fbchat.models.Message(msg), friend.uid)
        if sent:
            print("message sent successfully")

