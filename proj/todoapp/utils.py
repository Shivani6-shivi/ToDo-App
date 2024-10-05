from twilio.rest import Client

import json
import requests
import random

from django.core.mail import send_mail

def verifyEmail(request,user):
	activation_code=random.randrange(111111111111,999999999999)
	request.session['activation_code'] = activation_code
		
	subject='Welcome to ToDoApp!!'
	message='''We are happy to see you on our platform. <br /><br />
			   Please click over the <a href='http://localhost:8000/todoapp/actact/?id={}&act_code={}&uname={}'>link</a> to activate your account. 	
			'''.format(user.id,activation_code,user.first_name+' '+user.last_name)
	
	send_mail(subject,'','ToDoApp Welcomes you',[request.POST.get('email')],fail_silently=False,html_message=message)		


def reCaptcha(request):
	responsekey=request.POST.get('g-recaptcha-response')
	secretkey='6LervUjhgjhjhkjkhkjhkjhkQi06jhu_qnHDTI'
	
	captchadata={'secret':secretkey,'response':responsekey}
	
	resp=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
	
	respdict=json.loads(resp.text)
	
	return respdict['success']


def sendOTP(mobnum,request):
	# Your Account SID from twilio.com/console
	account_sid = "AC447jhjjjhhghghghghc14ec2c6187"
	
	# Your Auth Token from twilio.com/console
	auth_token  = "3f741bjggghjkjkj26fkjjkjk0de"

	client = Client(account_sid, auth_token)

	otp = str(random.randrange(111111,999999))
	request.session['otp'] = otp
	print(otp+' ----------##########~~~~~~~~~~~~###########')

	message = client.messages.create(
		to="+91"+mobnum, 
		from_="+91677777777",
		body="Hello from ISRDC ToDoApp! Your OTP: "+otp)

	print(message.sid,' ~~~~~~~~~~~#####~~~~~~~~~~~~')