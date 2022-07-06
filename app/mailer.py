import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
import datetime

SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)
MAIL_FROM = os.getenv("MAIL_FROM", None)
MAIL_SUBJECT = os.getenv("MAIL_SUBJECT", None)


def get_date(date):
    date_type = [int(i) for i in date.split("-")]
    format_date = datetime.datetime(date_type[0], date_type[1], date_type[2]).strftime(
        "%d.%m.%Y"
    )
    return format_date


class Mailer:
    def __init__(self, data_from_xml):
        self.msg = MIMEMultipart()
        self.msg["From"] = f"{MAIL_FROM} <{SMTP_EMAIL}>"
        self.msg["To"] = data_from_xml.email_address
        self.msg["Subject"] = MAIL_SUBJECT
        self.data = {
            "email_address": data_from_xml.email_address,
            "prepayment_calc": "{:,}".format(int(data_from_xml.prepayment_calc)),
            "calculation_type": data_from_xml.calculation_type,
            "loan_type": data_from_xml.loan_type,
            "months": int(data_from_xml.months),
            "loan_interest": round(float(data_from_xml.loan_interest), 2),
            "remaining_principal": "{:,}".format(
                int(data_from_xml.remaining_principal)
            ),
            "months_to_repayment": int(data_from_xml.months_to_repayment),
            "interest_rate_date_of_repayment": round(
                float(data_from_xml.interest_rate_date_of_repayment), 2
            ),
            "has_eligibility": data_from_xml.has_eligibility,
            "month_bank_paid": get_date(data_from_xml.month_bank_paid),
            "loan_end_date": get_date(data_from_xml.loan_end_date),
            "submission_id": data_from_xml.submission_id,
        }
        try:
            with open("app/email_template.html", "rt", encoding="utf-16") as f_template:
                template = Template(f_template.read())
                letter_text = template.render(a=self.data)
                # Debug propose only
                # with open("index.html", "wt") as f:
                #     f.write(letter_text)
                self.msg.attach(MIMEText(letter_text, "html", _charset="utf-16"))
                with open("app/myimagecid.png", "rb") as f:
                    # set attachment mime and file name, the image type is png
                    mime = MIMEBase("image", "png", filename="myimagecid.png")
                    # add required header data:
                    mime.add_header(
                        "Content-Disposition", "attachment", filename="myimagecid.png"
                    )
                    mime.add_header("X-Attachment-Id", "0")
                    mime.add_header("Content-ID", "<0>")
                    # read attachment file content into the MIMEBase object
                    mime.set_payload(f.read())
                    # encode with base64
                    encoders.encode_base64(mime)
                    # add MIMEBase object to MIMEMultipart object
                    self.msg.attach(mime)
                with open("app/finwiz-logo.png", "rb") as f:
                    # set attachment mime and file name, the image type is png
                    mime = MIMEBase("image", "png", filename="finwiz-logo.png")
                    # add required header data:
                    mime.add_header(
                        "Content-Disposition", "attachment", filename="finwiz-logo.png"
                    )
                    mime.add_header("X-Attachment-Id", "1")
                    mime.add_header("Content-ID", "<1>")
                    # read attachment file content into the MIMEBase object
                    mime.set_payload(f.read())
                    # encode with base64
                    encoders.encode_base64(mime)
                    # add MIMEBase object to MIMEMultipart object
                    self.msg.attach(mime)
        except Exception as e:
            print(e)
            raise e
