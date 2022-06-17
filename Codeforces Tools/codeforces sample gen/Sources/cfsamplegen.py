import requests, json
import os, sys, time
import pdfkit 
import threading
# import lxml.html

if(len(sys.argv) <= 1):
	sys.exit("Contest ID not found")

contest_id = sys.argv[1]

url = 'https://codeforces.com/api/contest.standings?contestId=' + str(contest_id) + '&from=1&count=1'

#the idea is call the codeforces api and recieve the json data of score board
#this data include the info abt contest and score board, we dont card abt score board
#but at this tools, we dont care about the ranking of user handle
response_data = requests.post(url)
response_data_json = json.loads(response_data.text)

if(response_data_json['status'] != 'OK'):
	sys.exit(response_data_json['comment'])

contest_name = response_data_json['result']['contest']['name'].strip().replace('\n', '').replace('\r', '')

#split contest problems index from result
problems_index_list = [problem['index'] for problem in response_data_json['result']['problems']]

print("Contest name: " + contest_name)
print("Started time: " + time.ctime(response_data_json['result']['contest']['startTimeSeconds']))
print("Problems list: " + str(problems_index_list))

#change the default contest directory
contest_directory = f'/mnt/e/Coding/Contest/CodeForces/{contest_name}'
# contest_directory_w = f'E:/Coding/Contest/CodeForces/{contest_name}'

if(os.path.exists(contest_directory) == True and not '-f' in sys.argv):
	os.system("subl.exe \"E:" + contest_directory[6:len(contest_directory)] + "\"")
	exit(0)

try: os.mkdir(contest_directory)
except: pass

template_signature = """/*
 * Author : DoTran
 * Created: %s
**/

""" %time.ctime(time.time())

# if you need to create script file with template
# create a cpp template file and change the path to the template file
# or delete the next 4 lines if u dont need to create a script file with template
template_path = "/mnt/e/Template/CPP Template/CPTemplate.cpp"

str_template = ""

with open(template_path, 'r') as template_ostream:
	str_template = template_ostream.read()

# generate the in/out file at contest directory
os.system("echo >\"" + contest_directory + "/inp.txt\"")
os.system("echo >\"" + contest_directory + "/out.txt\"")

# open contest folder with sublime text - change if you use a nother code editor or delete
# if you dont want to use
os.system("subl.exe \"E:" + contest_directory[6:len(contest_directory)] + "\"")

def parse_problem(contest_id, problem):
	pdf_path = f'{contest_directory}/{problem}.pdf'
	cpp_path = f'{contest_directory}/{problem}.cpp'
	
	with open(cpp_path, 'w') as problem_file:
		problem_file.write(template_signature)
		problem_file.write(str_template)

	# print('[DEBUG] ', f'https://codeforces.com/contest/{contest_id}/problem/{problem}')
	try: pass
		pdfkit.from_url(f'https://codeforces.com/contest/{contest_id}/problem/{problem}', pdf_path)
	except Exception as err: 
		print(f'[ERROR][{contest_id}][{problem}]: ', err)

# sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
for problem in problems_index_list:
	threading.Thread(target = parse_problem, args = (contest_id, problem, )).start()

pdfkit.from_url(f'https://codeforces.com/contest/{contest_id}/problems', f'{contest_directory}/problems.pdf')
