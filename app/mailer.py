import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2
import datetime

SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)


def get_date(date):
    date_type = [int(i) for i in date.split(",")]
    format_date = datetime.datetime(date_type[0], date_type[1], date_type[2]).strftime(
        "%d.%m.%Y"
    )
    return format_date


class Mailer:
    def __init__(self, data_from_xml):
        self.msg = MIMEMultipart()
        self.msg["From"] = SMTP_EMAIL
        self.msg["To"] = data_from_xml.email_address
        self.msg["Subject"] = "Test mail"
        self.data = {
            "email_address": data_from_xml.email_address,
            "prepayment_calc": "{:,}".format(int(data_from_xml.prepayment_calc)),
            "calculation_type": "false" not in data_from_xml.calculation_type.lower(),
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
            templateLoader = jinja2.FileSystemLoader(searchpath="./app/")
            templateEnv = jinja2.Environment(loader=templateLoader)
            TEMPLATE_FILE = "email.html"
            template = templateEnv.get_template(TEMPLATE_FILE)
            letter_text = template.render(a=self.data)

            self.msg.attach(MIMEText(letter_text, "html", _charset="utf-8"))

            # Example add picture to email attachment
            # with open('app/myimagecid.png', 'rb') as f:
            #     # set attachment mime and file name, the image type is png
            #     mime = MIMEBase('image', 'png', filename='myimagecid.png')
            #     # add required header data:
            #     mime.add_header('Content-Disposition', 'attachment', filename='myimagecid.png')
            #     mime.add_header('X-Attachment-Id', '0')
            #     mime.add_header('Content-ID', '<0>')
            #     # read attachment file content into the MIMEBase object
            #     mime.set_payload(f.read())
            #     # encode with base64
            #     encoders.encode_base64(mime)
            #     # add MIMEBase object to MIMEMultipart object
            #     self.msg.attach(mime)
            # with open('app/finwiz-logo.png', 'rb') as f:
            #     # set attachment mime and file name, the image type is png
            #     mime = MIMEBase('image', 'png', filename='finwiz-logo.png')
            #     # add required header data:
            #     mime.add_header('Content-Disposition', 'attachment', filename='finwiz-logo.png')
            #     mime.add_header('X-Attachment-Id', '1')
            #     mime.add_header('Content-ID', '<1>')
            #     # read attachment file content into the MIMEBase object
            #     mime.set_payload(f.read())
            #     # encode with base64
            #     encoders.encode_base64(mime)
            #     # add MIMEBase object to MIMEMultipart object
            #     self.msg.attach(mime)
        except Exception as e:
            print(e)
            raise e
