import sys
import click

from app import send_email


@click.command()
@click.option('--xml-path', prompt='Model', help='Path to xml file.')
def start(xml_path):
    try:
        with open(xml_path, "rb") as f:
            send_email(f)
    except Exception:
        sys.stderr.write(
            "The xml file uploaded cannot be parsed."
            " Please check you have uploaded the correct file."
        )
        return


if __name__ == '__main__':
    start()
