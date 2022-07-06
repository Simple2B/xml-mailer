import pytest
from app import send_email

# from sample_data.values_list import email_input
from sample_data.values_list import email_input


# @pytest.mark.skip(reason="test sends email")
def test_send_letter():
    assert send_email(email_input)
