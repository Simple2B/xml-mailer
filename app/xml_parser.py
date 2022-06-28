import xmltodict


class DataFromXml(object):
    """[summary]
    Parses XML file and creates corresponding python object.
    """

    def __init__(self, xml_file):
        xml_text = xml_file.read()
        xml_dict = xmltodict.parse(xml_text)
        self.load_email_data(xml_dict['email_information']['email_data'])
        self.load_saving_data(xml_dict['email_information']['saving_data'])

    def load_email_data(self, email_data_dict):
        self.email_address = email_data_dict['email_address']
        self.PREPAYMENT_CALC = email_data_dict['PREPAYMENT_CALC']
        self.Calculation_type = email_data_dict['Calculation_type']
        self.Loan_type = email_data_dict['Loan_type']
        self.Months = email_data_dict['Months']
        self.Loan_interest = email_data_dict['Loan_interest']
        self.Remaining_principal = email_data_dict['Remaining_principal']
        self.Months_to_repayment = email_data_dict['Months_to_repayment']
        self.interest_rate_date_of_repayment = email_data_dict['interest_rate_date_of_repayment']
        self.Has_eligibility = email_data_dict['Has_eligibility']
        self.Month_bank_paid = email_data_dict['Month_bank_paid']
        self.Loan_end_date = email_data_dict['Loan_end_date']
        self.Submission_ID = email_data_dict['Submission_ID']

    def load_saving_data(self, saving_data_dict):
        self.show_optimal_reference = saving_data_dict['show_optimal_reference']
        self.money_saved_from_interest = saving_data_dict['money_saved_from_interest']
        self.money_saved_from_mixture = saving_data_dict['money_saved_from_mixture']
        self.better_mixture_exists = saving_data_dict['better_mixture_exists']
        self.margin_diff = saving_data_dict['margin_diff']
