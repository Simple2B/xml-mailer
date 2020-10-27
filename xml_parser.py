import xmltodict


class Data_from_xml():

    def from_xml(self, xml_file):
        xml_text = xml_file.read()
        xml_dict = xmltodict.parse(xml_text)
        self.email_data(xml_dict['email_information']['email_data'])
        self.saving_data(xml_dict['email_information']['saving_data'])

    def email_data(self, email_data_dict):
        self.Analysis_number = email_data_dict['Analysis_number']
        self.name_of_lender_1 = email_data_dict['name_of_lender_1']
        self.name_of_lender_2 = email_data_dict['name_of_lender_2']
        self.Fb_link = email_data_dict['Fb_link']
        self.Forum_link = email_data_dict['Forum_link']
        self.is_send_to_forum = email_data_dict['is_send_to_forum']

    def saving_data(self, saving_data_dict):
        self.show_optimal_reference = saving_data_dict['show_optimal_reference']
        self.money_saved_from_interest = saving_data_dict['money_saved_from_interest']
        self.money_saved_from_mixture = saving_data_dict['money_saved_from_mixture']
        self.better_mixture_exists = saving_data_dict['better_mixture_exists']
        self.margin_diff = saving_data_dict['margin_diff']
