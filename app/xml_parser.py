import xmltodict


class DataFromXml(object):
    """[summary]
    Parses XML file and creates corresponding python object.
    """

    def __init__(self, xml_file):
        xml_text = xml_file.read()
        xml_dict = xmltodict.parse(xml_text)
        self.load_email_data(xml_dict["email_information"]["email_data"])
        # self.load_saving_data(xml_dict['email_information']['saving_data'])

    def load_email_data(self, email_data_dict):
        self.subject = email_data_dict["subject"]
        self.email_address = email_data_dict["email_address"]
        self.prepayment_calc = email_data_dict["prepayment_calc"]
        self.calculation_type = email_data_dict["calculation_type"]
        self.loan_type = email_data_dict["loan_type"]
        self.months = email_data_dict["months"]
        self.loan_interest = email_data_dict["loan_interest"]
        self.remaining_principal = email_data_dict["remaining_principal"]
        self.months_to_repayment = email_data_dict["months_to_repayment"]
        self.interest_rate_date_of_repayment = email_data_dict[
            "interest_rate_date_of_repayment"
        ]
        self.has_eligibility = email_data_dict["has_eligibility"]
        self.month_bank_paid = email_data_dict["month_bank_paid"]
        self.loan_end_date = email_data_dict["loan_end_date"]
        self.submission_id = email_data_dict["submission_id"]

    # def load_saving_data(self, saving_data_dict):
    #     self.show_optimal_reference = saving_data_dict['show_optimal_reference']
    #     self.money_saved_from_interest = saving_data_dict['money_saved_from_interest']
    #     self.money_saved_from_mixture = saving_data_dict['money_saved_from_mixture']
    #     self.better_mixture_exists = saving_data_dict['better_mixture_exists']
    #     self.margin_diff = saving_data_dict['margin_diff']
