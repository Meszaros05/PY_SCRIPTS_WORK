import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# Email configuration
sender_email = "gerifekete@gmail.com"
receiver_email = "gerifekete69@gmail.com"
subject = "CSV Report Attached"
body = "Hi,\n\nPlease find the attached CSV report.\n\nBest regards,\nPython Script"

# Path to the CSV file in Downloads
csv_filename = "excel.csv"  # Replace with your actual file name
downloads_path = os.path.abspath(csv_filename)


# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the plain text body
message.attach(MIMEText(body, "plain"))

# Attach the CSV file
try:
    with open(downloads_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=csv_filename)
        part['Content-Disposition'] = f'attachment; filename="{csv_filename}"'
        message.attach(part)
except FileNotFoundError:
    print(f"Error: File not found at {downloads_path}")
    exit(1)


# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port =587
smtp_username = "gerifekete@gmail.com"
smtp_password = "dabx cuif rhui ioxc"

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.set_debuglevel(1)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")








