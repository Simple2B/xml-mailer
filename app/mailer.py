import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
import datetime

SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)


class Mailer():
    def __init__(self, data_from_xml):
        self.msg = MIMEMultipart()
        self.msg['From'] = SMTP_EMAIL
        self.msg['To'] = data_from_xml.email_address
        # self.msg['Subject'] = data_from_xml.subject
        self.data = {
            'email_address': data_from_xml.email_address,
            'PREPAYMENT_CALC': "{:,}".format(int(data_from_xml.PREPAYMENT_CALC)),
            'Calculation_type': bool(data_from_xml.Calculation_type),
            'Loan_type': data_from_xml.Loan_type,
            'Months': int(data_from_xml.Months),
            'Loan_interest': float(format(data_from_xml.Loan_interest, ".2f")),
            'Remaining_principal': "{:,}".format(int(data_from_xml.Remaining_principal)),
            'Months_to_repayment': int(data_from_xml.Months_to_repayment),
            'interest_rate_date_of_repayment': float(format(data_from_xml.interest_rate_date_of_repayment, ".2f")),
            'Has_eligibility': data_from_xml.Has_eligibility,
            'Month_bank_paid': datetime.datetime(data_from_xml.Month_bank_paid).strftime("%d.%m.%Y"),
            'Loan_end_date': datetime.datetime(data_from_xml.Loan_end_date).strftime("%d.%m.%Y"),
            'Submission_ID': data_from_xml.Submission_ID,
        }
        try:
            with open("app/email_template.html", "rt", encoding="utf-16") as f_template:
                template = Template(f_template.read())
                letter_text = template.render(data=self.data)
                # Debug propose only
                # with open("index.html", "wt") as f:
                #     f.write(letter_text)
                self.msg.attach(MIMEText(letter_text, 'html', _charset="utf-16"))
                with open('app/myimagecid.png', 'rb') as f:
                    # set attachment mime and file name, the image type is png
                    mime = MIMEBase('image', 'png', filename='myimagecid.png')
                    # add required header data:
                    mime.add_header('Content-Disposition', 'attachment', filename='myimagecid.png')
                    mime.add_header('X-Attachment-Id', '0')
                    mime.add_header('Content-ID', '<0>')
                    # read attachment file content into the MIMEBase object
                    mime.set_payload(f.read())
                    # encode with base64
                    encoders.encode_base64(mime)
                    # add MIMEBase object to MIMEMultipart object
                    self.msg.attach(mime)
                with open('app/finwiz-logo.png', 'rb') as f:
                    # set attachment mime and file name, the image type is png
                    mime = MIMEBase('image', 'png', filename='finwiz-logo.png')
                    # add required header data:
                    mime.add_header('Content-Disposition', 'attachment', filename='finwiz-logo.png')
                    mime.add_header('X-Attachment-Id', '1')
                    mime.add_header('Content-ID', '<1>')
                    # read attachment file content into the MIMEBase object
                    mime.set_payload(f.read())
                    # encode with base64
                    encoders.encode_base64(mime)
                    # add MIMEBase object to MIMEMultipart object
                    self.msg.attach(mime)
        except Exception as e:
            print(e)
            raise e
