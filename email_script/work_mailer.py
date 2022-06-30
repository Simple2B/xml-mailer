import os
import smtplib

from email_script.mailer import Mailer
from email_script.input_list_parser import DataFromInputList


MAIL_SERVER = os.getenv("MAIL_SERVER", None)
MAIL_PORT = os.getenv("MAIL_PORT", None)
SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", None)


class WorkMailer(Mailer):
    """[summary]
    Connects to SMTP server and sends email
    """

    def __init__(self, data_from_xml: DataFromInputList):
        super().__init__(data_from_xml)

    def send(self):
        try:
            # Connect to the server
            with smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT) as server:
                # Login to the email server
                server.login(SMTP_EMAIL, SMTP_PASSWORD)
                recipients = self.data["email_address"]
                ret_val = server.sendmail(
                    from_addr=SMTP_EMAIL, to_addrs=recipients, msg=self.msg.as_string()
                )
                print("SMTP_EMAIL --- ", SMTP_EMAIL)
                print("recipients --- ", recipients)
                print("server.sendmail - returns:", ret_val)
                server.quit()  # Logout of the email server
        except smtplib.SMTPException as e:
            print(e)
            raise e
