import sys
import click
from dotenv import load_dotenv

from app import send_email


load_dotenv()


def parse_xml(xml_path: str) -> bool:
    try:
        with open(xml_path, "rb") as f:
            send_email(f)
        print("OK")
        return True
    except Exception:
        sys.stderr.write(
            "The xml file uploaded cannot be parsed."
            " Please check you have uploaded the correct file."
        )
        return False


@click.command()
@click.option("--xml-path", help="Path to xml file.")
def start(xml_path):
    parse_xml(xml_path)


if __name__ == "__main__":
    start()
