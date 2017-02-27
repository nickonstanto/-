import os
import json
import requests

key = "key-89b7c249c291eacb7bbc724d55f9c460"
url =  "https://api.mailgun.net/v3/sandboxf98dde8cbb124bba9e63db53f72a947c.mailgun.org/messages"
sandbox = "Mailgun Sandbox <postmaster@sandboxf98dde8cbb124bba9e63db53f72a947c.mailgun.org>"

#suanrtish gia na steiloume to mail
#y -> paraliptis
def send_simple_message(x,y,the_beer):
    auth=("api", key)
    data={"from": x,
           "to": y,
           "subject": "Take a Beer!!!",
           "text": the_beer}
    response = requests.post(url, auth = auth, data = data)
    response.raise_for_status()

#diavazoume to email
email_se_auton_pou_stelnw = raw_input('Dwse to email pou thes na steilw thn mpura -> ')

#trexoume to command
#kai apothikeuoume to arxeio me thn entolh > arxeio.json se json morfh
os.system('curl https://api.punkapi.com/v2/beers/random > beer_email.json')

#twra prepei na diavasoume to json
#exoume ./ epeidh eimaste ston idio fakelo
text_jason = open('./beer_email.json').read()

#lo einai o array poy theloume me ola ta data
lo = json.loads(text_jason)

print sandbox,email_se_auton_pou_stelnw,lo[0]['name']
send_simple_message(sandbox, email_se_auton_pou_stelnw ,lo[0]['name'])