# The Python script running on AWS Lambda service. 
# The triggering cron job running on AWS EventBridge (CloudWatch Events) 
# Coded in Python 3.9 stable. 

import smtplib, sys, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def lambda_handler(event, context):
    #TODO implement 
    main()
    return {
        'statusCode': 200, 
        'body': json.dumps('The script has been worked successfully.')
    }
    
def main():
    # TODO implement
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("*******", "*******")
    
    sender = '*******'
    recipients = ['*******']
    
    # Data coming from the bank.  
    # bulten = ("https://gorsel.isbank.com.tr/kampanya/cmd/19586/bulten.pdf") 
    
    now = datetime.now()
    dtstring = now.strftime("%d/%m/%Y")
 
    mesaj = MIMEMultipart()
    mesaj["From"] = sender
    mesaj["To"] = ", ".join(recipients)
    mesaj["Subject"] = "Piyasalarda Bugün " + str(dtstring)
    
    # Mail body by combining plain and html.  
    body1 = str(dtstring) + " - İş Yatırım "
    body2 = """\
    <html>
        <head></head>
        <body>
            <p>Bugünün piyasa raporu için <a href="https://gorsel.isbank.com.tr/kampanya/cmd/19586/bulten.pdf"><b>tıkla.</b></a></p>
        </body>
    </html>
    """
 
    body_text = MIMEText(body1, "plain")
    body_html = MIMEText(body2, "html")
    
    mesaj.attach(body_text)
    mesaj.attach(body_html)
 
    mail.sendmail(mesaj["From"], recipients, mesaj.as_string())
    print("The mail has been sent from AWS Lambda.")
    mail.close()