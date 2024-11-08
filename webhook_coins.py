
### python Webhook;

from flask import Flask, request, app, jsonify
import json
import smtplib
import pandas as pd
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from sqlalchemy import text, create_engine

# connect to postgre for acess to mail addresses

with open ('postgre_aut.txt', 'r') as f:
    aut = f.read()[:-1]

engine = create_engine(aut)

with engine.connect() as conn:

    data = conn.execute(text("SELECT * FROM customer_mail;"))


df_mail_bank = pd.DataFrame(data)


# read the file with e-mail and password;
with open('mail_aut.txt', 'r') as f2:
    lines = f2.read().splitlines()
    login = lines[0]
    passw = lines[1]


def send_mail(msg):
    
    message = MIMEMultipart()
    message["Subject"] = "US-EU exchange prices"
    html = f"""
    <p> Seguem as novas cotações recebidas pelo webhook </p>
    {pd.DataFrame(msg).to_html(index = False)} 
    """
    message.attach(MIMEText(html, "html"))

    try:
        mail_list = df_mail_bank.mail_address.values
    except Exception as e: 
        return print(f'An error while  trying to e-mail: {e}')


    for dest in mail_list:

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(login, passw)
        body = message.as_string()
        s.sendmail(login,dest,body)
        s.quit()
    
    return print('mail sent!')


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    
    if request.method == 'POST':
       
        data = request.get_json()
        # now we follow based on data receveid from POST:
        if data.get('type') == 'inclusion':

            with engine.connect() as conn:  # first, refresh the variable;

                data_mail = conn.execute(text("SELECT * FROM customer_mail;"))
                df_mail_bank = pd.DataFrame(data_mail)

                print(df_mail_bank)


            if not df_mail_bank.empty:
            
                if data.get('mail_address') in df_mail_bank.mail_address.values:
                
                    return jsonify('e-mail already registered')
                
            else:

                df_mail = pd.DataFrame(data).drop(columns = 'type')
                df_mail.to_sql('customer_mail', engine, if_exists='append', index = False)

                return jsonify ({'message': 'e-mail subscribed'})
            

        elif data.get('type') == 'alert':
                    
            send_mail(data["data"])
            return jsonify({"message": "New coin prices received!"})

        else:

            return jsonify({"Invalid type key! please follow the instructions"})



    if request.method == 'GET': # we will just display some instructions

        return jsonify({"message": """Hello, this is the route to webhook. Use \
                        POST to send us your e-mail address and the coin you want to \
                        receive updates""",
                        'Tutorial': 'Use type: include for subscrib to our warnings'})





if __name__ == '__main__':
    app.run(debug = True)

