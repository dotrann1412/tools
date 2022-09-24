import sys, os

from services import html_mail, html_msg, build_email_content, MailService
from utils import print_color, print_indent, text_format
import datetime

import subprocess
from subprocess import PIPE

import colorama
colorama.init()

SENDER = 'dotrann1412.dev@gmail.com'
PASSWORD = 'tliinhkafztqxhma'

def runner(command: list, response_to):
    start = datetime.datetime.now()
    
    process = subprocess.Popen(command, stdout = PIPE, stderr = PIPE, shell = True)
    
    for line in process.stdout:
        print(line.decode())
    
    out, err = process.communicate()
    out, err = out.decode(), err.decode()
    exitcode = process.returncode
    
    durration = datetime.datetime.now() - start
    
    data_content = \
f"""{"-" * 20} STDOUT {"-" * 20}
{out}
{"-" * 48}

{"-" * 20} STDERR {"-" * 20}
{err}
{"-" * 48}

Exit Code: {exitcode}
Durration: {durration}"""

    workspace = os.path.dirname(os.path.realpath(__file__));
    datafile = os.path.join(workspace, 'content.txt')
    
    with open(datafile, 'w') as fp:
        fp.write(data_content)
    
    command_str = ' '.join([item if ' ' not in item else f'"{item}"' for item in command])
    message = f'<b>Command:</b> {command_str}<br/><b>Time duration:</b> {durration}<br><b>Exit code:</b> {exitcode}<br/><b>Open the attachments for more details</b><br>'
    
    content = {
        'html': html_mail(command_str, html_msg(message, exitcode == 0, bold_all = False)),
        'data': datafile
    }
    
    mail_content = build_email_content(SENDER, [response_to], f'Process completed {"failed" if exitcode != 0 else "successfully"} - ({command_str})', content = content)

    hostmail = MailService()
    result = True
    if hostmail.login(SENDER, PASSWORD):
        try:
            hostmail.send_mail(mail_content)
            print_color(f'Command \'{command_str}\' completed - Response was send to {response_to} successfully!', text_format.OKGREEN)
        except Exception as err:
            print_color(f'Some problem occur while sending email to {response_to}. Details as below', text_format.FAIL)
            result = False
    else:
        print_color('Cannot login to SMTP server', text_format.FAIL)
        result = False
        
    if os.path.exists(datafile):
        os.remove(datafile)
    return result

def main():
    if len(sys.argv) != 0:
        return runner(sys.argv[1:-1], sys.argv[-1])
    print_color('Command not found', text_format.FAIL)
    return False

if __name__ == "__main__":
    main()