import Con
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import config
import csv
class Email_To_Client:
    def connect_smtp_server(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("surajkesarwani2@gmail.com", config.gmailpass)
        return server
    def get_data_from_db(self):
        DB= Con.db
        cur = DB.cursor()
        query = "select Name, Age from data230"
        cur.execute(query)
        All_data = cur.fetchall()
    def db_data_to_csv(self):
        with open("data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Age"])
            writer.writerows(self.All_data)
    def email_content(self):
        sender = "surajkesarwani2@gmail.com"
        reciever= "surajkesarwani2@gmail.com"
        subject = "This is my Test email for Checking flow of db to csv"
        msg = '''Hello \n
        This is my test email for checking the flow of data coming from db which passes through gmail \n
        let me know sir if need to make any changes in it \n
    

        Regards,
        Suraj '''
        mssg = MIMEMultipart()
        mssg["From"] = sender
        mssg["to"] = reciever
        mssg["subject"] = subject
        mssg.attach(MIMEText(msg, 'plain'))
    def attach_images_csv_files(self):
        with open('download.jpeg', 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-Disposition', 'attachment', filename="download.jpeg")
            self.mssg.attach(img)
        with open('img.jpeg', 'rb') as img_file2:
            img = MIMEImage(img_file2.read())
            img.add_header('Content-Disposition', 'attachment', filename="img.jpeg")
            self.mssg.attach(img)

        with open("data.csv", 'rb') as csv1:
            attachment = MIMEApplication(csv1.read())
            attachment.add_header('Content-Disposition', "attachment", filename="data.csv")
            self.mssg.attach(attachment)
        with open("data23.csv", "rb") as csv2:
            attachment2 = MIMEApplication(csv2.read())
            attachment2.add_header("Content-Disposition", "attachment", filename="data.csv")
            self.mssg.attach(attachment2)
    def send_email(self):
        self.server.send_message(self.mssg)
        self.server.close()

client_email=Email_To_Client()
client_email.connect_smtp_server()
client_email.get_data_from_db()
client_email.db_data_to_csv()
client_email.email_content()
client_email.attach_images_csv_files()
client_email.send_email()

