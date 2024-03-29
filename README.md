# xml-mailer project

Usage:
```bash
$ python send_email.py --xml-path <path to XML>
```

`The code sample in which you need to enter data is in example.xml`
## Installation tutorial

  Prerequisites:
  1. First of all one must be sure that Python 3.9 is installed. To check that use the command:
  ```bash
  python -V
  ```
  2. Make sure pip is installed using the command
  ```bash
  python -m pip -V
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
python3.9 -m venv .venv
```
4. After that one must enter that environment using the command
```bash
.venv\Scripts\activate.bat
```
5. Now one needs to install all the dependencies using the command
```bash
pip install -r requirements.txt
```
6. One has to unzip env.zip archive to xml-mailer directory. After unzipping .env file will appear. You should enter the email address from which you will send mail and password to that email in .env file.

7. Congratulations! Program is ready to use. Just use the command
```bash
python send_email.py --xml-path <path to XML>
```
