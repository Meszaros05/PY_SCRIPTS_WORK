import smtplib
import os
import time
from pathlib import Path 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def Waiter():
    # Path to the target file
    current_file=Path(__file__).resolve()
    target_file_folder=current_file.parent.parent
    target_file=current_file.parent.parent / "Exports.xlsx"
    # Timeout in seconds
    timeout = 5
    start_time = time.time()
    
    while True:
        files=list(target_file_folder.glob("Exports*.xlsx"))
        
        if files:
            target_file_JSON = max(files, key=lambda f: f.stat().st_mtime)
            return target_file  # Return the file path when found

        if time.time() - start_time > timeout:
            return None  # Timeout, no file found

        time.sleep(1)


def Email():
    current_file=Path(__file__).resolve()
    target_file_folder=current_file.parent.parent
      
    target_file=Waiter()
    if target_file:
        target_file=max(target_file_folder.glob("Exports*.xlsx"), key=lambda f: f.stat().st_mtime)
        # Email configuration
        sender_email = "zabbix_server@hydro.com"
        receiver_email = "gergely.fekete@hydro.com"
        subject = "CSV Report Attached"
        body = "Hi,\n\nPlease find the attached CSV report.\n\nBest regards,\nPython Script"

        # Path to the CSV file in Downloads
        xlsx_filename = "Exports.xlsx"  # Replace with your actual file name
        #downloads_path = os.path.abspath(csv_filename)
        current_file=Path(__file__).resolve()
        target_file=current_file.parent.parent / "Exports.xlsx"

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject


        # Attach the plain text body
        message.attach(MIMEText(body, "plain"))

        # Attach the CSV file
        try:
            with open(target_file, "rb") as file:
                part = MIMEApplication(file.read(), Name=xlsx_filename)
                part['Content-Disposition'] = f'attachment; filename="{xlsx_filename}"'
                message.attach(part)
        except FileNotFoundError:
            print(f"Error: File not found at {target_file}")
            exit(1)


        # SMTP server configuration
        smtp_server = "mail.hydro.com"
        smtp_port =25


        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.set_debuglevel(1)
                server.starttls()
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")


    else: print("Excel is not created")
