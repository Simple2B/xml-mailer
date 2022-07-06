import pytest
from email_script.send_mail import send_decorated_email
from sample_data.values_list import email_input


# @pytest.mark.skip(reason="test sends email")
def test_send_letter():
    assert send_decorated_email(email_input)
