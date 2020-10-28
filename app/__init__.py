from app.work_mailer import WorkMailer
from app.xml_parser import DataFromXml


def send_email(xml_file):
    data_from_xml = DataFromXml(xml_file)
    # send e-mail
    mailer = WorkMailer(data_from_xml)
    mailer.send()
