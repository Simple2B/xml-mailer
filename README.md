# xml-mailer project

Usage:
```bash
$ python3 send_email.py --xml-path <path to XML>
```
## Installation tutorial
0. I assume you are launching this program on some debian-like linux system. Prerequisites:
    1. First of all one must be sure that Python 3.8 is installed. To check that use the command:
    ```bash
    python3 -V
    ```
    2. Make sure python3-venv is installed. The easiest way is just installing it using the command:
    ```bash
    sudo apt-get install python3-venv
    ```
    If venv is already installed it will inform you.
    3. Make sure pip is installed using the command
    ```bash
    python3 -m pip -
    ```

1. Take everything from the repository using
```bash
git clone https://github.com/Simple2B/xml-mailer.git
```
while being in prefered directory.
2. Go to that directory using
```bash
cd xml-mailer
```
3. Install virtual environment to be able to install locally (meaning xml-mailer directory) all needed dependencies. To do that run
```bash
python3 -m venv .venv
```
4. After that one must enter that environment using the command
```bash
source  .venv/bin/activate
```
5. Now one needs to install all the dependencies using the command
```bash
pip -r requirements.txt
```
6. Congratulations! Program is ready to use. Just use the command
```bash
python3 send_email.py --xml-path <path to XML>
```
