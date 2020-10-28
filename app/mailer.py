import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from jinja2 import Template

SMTP_EMAIL = os.getenv("SMTP_EMAIL", None)


class Mailer():
    def __init__(self, data_from_xml):
        self.msg = MIMEMultipart()
        self.msg['From'] = SMTP_EMAIL
        self.msg['To'] = data_from_xml.name_of_lender_1
        self.msg['Subject'] = "Sample subject"
        with open('app/myimagecid.png', 'rb') as f:
            # set attachment mime and file name, the image type is png
            mime = MIMEBase('image', 'png', filename='app/myimagecid.png')
            # add required header data:
            mime.add_header('Content-Disposition', 'attachment', filename='app/myimagecid.png')
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            # read attachment file content into the MIMEBase object
            mime.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(mime)
            # add MIMEBase object to MIMEMultipart object
            self.msg.attach(mime)
        self.data = {
            'Analysis_number': data_from_xml.Analysis_number,
            'name_of_lender_1': data_from_xml.name_of_lender_1,
            'name_of_lender_2': data_from_xml.name_of_lender_2,
            'Fb_link': data_from_xml.Fb_link,
            'Forum_link': data_from_xml.Forum_link,
            'is_send_to_forum': data_from_xml.is_send_to_forum,
            'show_optimal_reference': data_from_xml.show_optimal_reference,
            'money_saved_from_interest': data_from_xml.money_saved_from_interest,
            'money_saved_from_mixture': data_from_xml.money_saved_from_mixture,
            'better_mixture_exists': data_from_xml.better_mixture_exists,
            'margin_diff': data_from_xml.margin_diff,
        }
        try:
            letter_text = Template(open("app/email_template.html", "rt", encoding="utf-16").read()).render(data=self.data)
            # with open("index.html", "wt") as f:
            #     f.write(letter_text)
        except Exception as e:
            print(e)
            raise e
        self.msg.attach(MIMEText(letter_text, 'html', _charset="utf-16"))
