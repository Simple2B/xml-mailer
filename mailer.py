from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


class Mailer():
    def __init__(self, data_from_xml):
        self.msg = MIMEMultipart()
        self.msg['From'] = data_from_xml.name_of_lender_2
        self.msg['To'] = ', '.join(data_from_xml.name_of_lender_1)
        self.msg['Subject'] = "Sample subject"

        data = {
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
        letter_text = Template(open("email_template.html").read()).render(var="TEXT", data=data)
        self.msg.attach(MIMEText(letter_text, 'html'))
