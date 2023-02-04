from dotenv import load_dotenv

import os
import requests
import time

load_dotenv()

links =[]
left =[]
completed =[]

# take input link that is needed to be shortend
def shortURL(link, name=''):
	API_KEY = os.getenv('CUTTLY_API_KEY')
	BASE_URL = 'https://cutt.ly/api/api.php' # url of the api for link shortning

	payload ={}
	if name == '':
		payload ={'key': API_KEY,'short': link}
	else:
		payload ={'key': API_KEY,'short': link, 'name': name}

	request =requests.get(BASE_URL, params=payload)
	data =request.json()

	try:
		shortLink =data['url']['shortLink']
		print(shortLink)
		completed.append(shortLink)

	except:
		status =data['url']['status']
		print('Error Status: ', status)
		left.append(link)

def singleLinkShort():
	print('\nEnter the link.')
	link =input('> ')
	print('\nShortLink: ',end='')
	shortURL(link)

def multipleLinkShort():
	print ('\nDue to free plan. We are limited to convert 3 links/min.\n'\
	'So please be patient. The output file will be generated at input file location.\n')
	
	print('Note: The link should be space seperated.')
	print('Please provide the location of text file with links.')
	
	inputFileLocation =input('> ')

	links =[]
	left =[]
	completed =[]

	with open(inputFileLocation, 'r') as f:
		for line in f:
			if line.strip():
				line =line.split('\n')[0]
				links.append(line)

	print("\nEst Time = ", int(len(links)/3), "min")
	for index, link in enumerate(links):
		if (index!=0 and index%3==0):
			time.sleep(60)
		print(index+1, '/', len(links), ': ', end ='')
		shortURL(link)

	with open('output.txt', 'a') as f:
		f.write("Links: \n")
		f.write(str(links))
		f.write('\n')

		f.write("Completed: \n")
		f.write(str(completed))
		f.write('\n')

		f.write("Left: \n")
		f.write(str(left))
		f.write('\n\n')

def menu():
	print('\nUrl Shortner Powered by Cuttly\n\n'\
	'1. Single Link \n2. Multiple Link \n3.Type \'q\' to Quit\n')

	choice =int(input('> '))
	return choice

def task(choice):
	if (choice==1):
		singleLinkShort()
	elif (choice==2):
		multipleLinkShort()

def run():
	while(True):
		try:
			task(menu())
		except:
			break
		
if __name__ == '__main__':
	run()