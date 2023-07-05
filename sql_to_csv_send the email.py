import Con
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import config
import pandas
class Email_To_Client:
    #connect_smtp_server funtion helps to establish the smtp connection
    def connect_smtp_server(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("surajkesarwani2@gmail.com", config.gmailpass)
        return server
    #get_data_from_db funtion help to estsblish the connection by using Con_file(DB Connection File) and getting the data from table 
    def get_data_from_db(self):
        DB= Con.db
        cur = DB.cursor()
        query = "select Name, Age from data230"
        cur.execute(query)
        All_data = cur.fetchall()
    #db_data_to_csv is taking the data and convert this to csv by using pandas library
    def db_data_to_csv(self):
        name=[]
        age=[]
        for Name ,Age in self.All_data:
            name.append(Name)
            age.append(Age)
            df={
                'Name ':name,
                'Age':age
                }
            dataframe=pd.DataFrame(df)
            dt_csv=dt.to_csv("data.csv")

    #email_content function is creating the content for email while using email.mime library package
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
    #attach_images_csv_files fuction is attaching the image and csv file in the email while Mimeimage and Mimeapplication Email Package
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
    #Maine fuction is use to call all function sequentially
     def main(self):
        self.connect_smtp_server()
        self.get_data_from_db()
        self.db_data_to_csv()
        self.email_content()
        self.attach_images_csv_files()
        self.send_email()

client_email=Email_To_Client()
client_email.main()




