from work_mailer import WorkMailer
from dotenv import load_dotenv
from xml_parser import Data_from_xml

load_dotenv()


def send_email(xml_file):
    data_from_xml = Data_from_xml()
    data_from_xml.from_xml(xml_file)
    # send e-mail
    mailer = (
        WorkMailer(data_from_xml)
    )
    mailer.send()
