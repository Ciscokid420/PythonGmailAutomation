import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
# Load CSV file
csv_file = 'C:\\Users\\AKhan\\Documents\\clients.csv'  # Replace with your CSV FULL FILE path
clients = pd.read_csv(csv_file)

# Email settings
smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
smtp_port = 587  # TLS port
email_user = 'akhanetskyy@rentalstoremember.com'  # Your Gmail address
email_password = 'jpvj dmtk sord yvit'  # Your App Password

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Secure the connection
    server.login(email_user, email_password)
    for index, client in clients.iterrows():
        first_name = client['First Name']
        last_name = client['Last Name']
        email_to = client['Email']

        # Compose the email
        subject = "Design Consults Available!"
        link = '<a href="https://calendly.com/rentalstoremember"> Here is the link to our calendar!</a>'
        body = f"""
        

Dear {first_name} {last_name},

<p>How is wedding planning going? We met briefly at the Bohemia Manor and wanted to check in with you! Rentals to Remember is a full service special event rental company offering tents, tables, chairs, china, glassware, flatware and linen.  Our design team works closely with your vendors to ensure all of the little details make your big day perfect! </P>
<br>
<p>We offer our design consultations at our Eastern Shore & Annapolis Design Studios or virtually for your convenience! </p> 
<br>
<p>So excited to be a part of your special day! {link} </P>
<br>
<br>
Best, 
Ginny Hockey  
        """

        msg = MIMEMultipart()
        msg['From'] = 'info@rentalstoremember.com'
        msg['To'] = email_to
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'html'))
        current_date = datetime.now().strftime("%B %d, %Y")
        # Send the email
        try:
            server.sendmail(email_user, email_to, msg.as_string())
            print(f"Email sent to {first_name} {last_name} at {email_to}")
        except Exception as e:
            print(f"Failed to send email to {first_name} {last_name}: {e}")
