class text_format:
    HEADER = ['\033[95m', '']
    OKBLUE = ['\033[94m', '']
    OKCYAN = ['\033[96m', '']
    OKGREEN = ['\033[92m', '']
    WARNING = ['\033[93m', 'Warning: ']
    FAIL = ['\033[91m', 'Failed: ']
    ENDC = ['\033[0m', '']
    BOLD = ['\033[1m', '']
    UNDERLINE = ['\033[4m', '']
    NORMAL = ['','']
    DEBUG = ['\033[91m', '[DEBUG]: ']
    YELLOW = ['\033[93m', '']
    RED = ['\033[91m', '']
    EXCEPTION = ['\033[91m', '[Exception]: ']
    
def print_color(message, option = text_format.NORMAL, end = '\n'):
    print(f'{option[0]}{option[1]}{message} {text_format.ENDC[0]}', end = end)
    
def print_indent(messages, level = 1, option = text_format.NORMAL, end = '\n'):
    if type(messages) == str:
        messages = messages.split('\n')
    
    for message in messages:
        print('\t' * level, end = '')
        print_color(message, option, end = end)