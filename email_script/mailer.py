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
        self.msg["Subject"] = "Some title"
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
            templateLoader = jinja2.FileSystemLoader(searchpath="./email_script/")
            templateEnv = jinja2.Environment(loader=templateLoader)
            TEMPLATE_FILE = "email.html"
            template = templateEnv.get_template(TEMPLATE_FILE)
            letter_text = template.render(a=self.data)

            self.msg.attach(MIMEText(letter_text, "html", _charset="utf-8"))

        except Exception as e:
            print(e)
            raise e
