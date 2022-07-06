from app.work_mailer import WorkMailer


class DataFromArray:
    def __init__(self, email_input: list):
        self.email_address = email_input[0]
        self.prepayment_calc = email_input[1]
        self.calculation_type = email_input[2]
        self.loan_type = email_input[3]
        self.months = email_input[4]
        self.loan_interest = email_input[5]
        self.remaining_principal = email_input[6]
        self.months_to_repayment = email_input[7]
        self.interest_rate_date_of_repayment = email_input[8]
        self.has_eligibility = email_input[9]
        self.month_bank_paid = email_input[10]
        self.loan_end_date = email_input[11]
        self.submission_id = email_input[12]


def send_decorated_email(email_input: list):
    data_from_array = DataFromArray(email_input)
    mailer = WorkMailer(data_from_array)
    mailer.send()
    return True
