import os
import smtplib
from mailer import Mailer
from xml_parser import Data_from_xml

SMTP_SERVER = os.getenv("SMTP_SERVER", None)
SMTP_PORT = os.getenv("SMTP_PORT", None)
SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)
SMTP_PWORD = os.getenv("SMTP_PWORD", None)

class WorkMailer(Mailer):
    """[summary]
    Connects to SMTP server and sends email
    """
    def __init__(self, data_from_xml: Data_from_xml):
        super().__init__(data_from_xml)

    def send(self):
        try:
            # Connect to the server
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Use TLS
                # Login to the email server
                server.login(SMTP_EMAIL, SMTP_PWORD)
                recipients = self.name_of_lender_1
                server.sendmail(from_addr=self.name_of_lender_2,
                                to_addrs=recipients,
                                msg=self.msg.as_string())
                server.quit()  # Logout of the email server
        except smtplib.SMTPException as e:
            print(e)
            raise e
