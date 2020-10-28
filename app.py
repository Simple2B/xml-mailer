from work_mailer import WorkMailer
from xml_parser import DataFromXml


def send_email(xml_file):
    data_from_xml = DataFromXml(xml_file)
    # send e-mail
    mailer = WorkMailer(data_from_xml)
    mailer.send()
