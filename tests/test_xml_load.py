import pathlib
import pytest
from send_email import parse_xml

TEST_XML = (pathlib.Path(__file__).parent / "test.xml").resolve()


@pytest.mark.skip(reason="test sends email")
def test_xml_load():
    # assert not parse_xml("bad_file_path")
    assert parse_xml(TEST_XML)
