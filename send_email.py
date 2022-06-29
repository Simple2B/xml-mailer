import sys
import click
from dotenv import load_dotenv

load_dotenv()

from app import send_email


def parse_xml(xml_path: str) -> bool:
    try:
        with open(xml_path, "rb") as f:
            print("OK-1")
            send_email(f)
        print("OK-2")
        return True
    except Exception:
        print("exeption")
        sys.stderr.write(
            "The xml file uploaded cannot be parsed."
            " Please check you have uploaded the correct file."
        )
        return False


@click.command()
@click.option("--xml-path", help="Path to xml file.")
def start(xml_path):
    print("def start(xml_path) - start")
    parse_xml(xml_path)
    print("def start(xml_path) - end")


if __name__ == "__main__":
    print("__main__ - start")
    start()
