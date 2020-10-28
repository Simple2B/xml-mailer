import sys
import click

from app import send_email


@click.command()
@click.option('--xml-path', help='Path to xml file.')
def start(xml_path):
    try:
        with open(xml_path, "rb") as f:
            send_email(f)
        print("OK")
    except Exception:
        sys.stderr.write(
            "The xml file uploaded cannot be parsed."
            " Please check you have uploaded the correct file."
        )


if __name__ == '__main__':
    start()
