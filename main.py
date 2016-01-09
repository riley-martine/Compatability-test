from __future__ import division
import csv
from email.mime.text import MIMEText
from datetime import date
import smtplib
from tabulate import tabulate

with open('spreadsheet.csv', 'rb') as f: #open spreadsheet.csv
    reader = csv.reader(f)
    all_data = list(reader) #put all the data in array all_data
table = []
start = 4 #start with person in row number 'start'
while start < len(all_data):
	table += [[start, all_data[start][96], all_data[start][2]]]
	start += 1

headers = ["Row", "Name", "Email"]

print tabulate(table, headers, tablefmt="pipe")

person1 = int(input('What is the row of the first person?: ')) #The row of person 1
person2 = int(input('What is the row of the second person?: ')) #the row of person 2 - person # does not matter

person1_row = all_data[person1] #put person1 row data in list person1_row
person1_email = person1_row[2]
person1_name = person1_row[96] 

person2_row = all_data[person2] #put person2 row data in list person2_row
person2_email = person2_row[2]
person2_name = person2_row[96]


bothlike = '' #define bothlike, a string of all commonalities that gets saved at the end
matchnum = 0 #define matchnum, the number of match points awarded
total_possible = 0 #define total_possible, the total number of match points available. 
person1_score = 0 #define p1_score, the score of p1
person2_score = 0 #same but for p2
bothlike += person1_name + '\n' + person1_row[3] + '\n\n' #add phone #s
bothlike += person2_name + '\n' + person2_row[3] + '\n\n'

bothlike += person1_name + ':\n' + person1_row[93] + ' spoon\n\n' #add what type of spoon each person is: eg. John \n Big spoon
bothlike += person2_name + ':\n' + person2_row[93] + ' spoon\n\n'


bothlike += 'Types of relationships ' + person1_name + ' would be interested in:\n' + person1_row[90] + '\n\n' #self explanatory

bothlike += 'Types of relationships ' + person2_name + ' would be interested in:\n' + person2_row[90] + '\n\n'

i_list_direct = [16, 17, 18, 63, 66, 69, 70, 71, 72, 73, 74, 75, 76, 77] #these are the questions that need to be directly compared
bothlike += 'Things both partners like: \n' #add section header to bothlike


for i in i_list_direct: #while the counter has not reached the end of the question list ^^
    total_possible += 1 #add one to the total possible points
    if person1_row[i] == person2_row[i] == 'Yes': #if both p1 and p2 say yes
        bothlike += all_data[0][i] + '\n' #add the first row's i'th column to bothlike
    if person1_row[i] == 'Yes':
    	person1_score += 1
    if person2_row[i] == 'Yes':
    	person2_score += 1
    if person1_row[i] == person2_row[i]: #if both people say the same thing, either yes, yes, or no, no
    	matchnum += 1 #add one to matchnum

bothlike += '\nPer person: \n' #add section header to person specific data
i_list_pairs_first = [12, 14, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 53, 55, 57, 59, 61, 64, 67, 91]
#^^ this bad boy is the list of the first item a in all of the question pairs (a, b) that need to be compared if p1(a)=p2(b) and p1(b)=p2(a)
total_score_helper = total_possible


for i in i_list_pairs_first:
	total_possible += 2 #add two to the total possible points, one for each check
	total_score_helper += 1
	if person1_row[i] == person2_row[i + 1]: #if person1 and person2 a and b are equal, either 00 or 11 (xnor)
		matchnum += 1 #add one to match number. 
	if person1_row[i + 1] == person2_row[i]: # if person1 b and person2 a are equal
		matchnum += 1 #add one to match number
	if person1_row[i] == person2_row[i + 1] == 'Yes': #if both yes
		bothlike += person1_name + ' would like ' + all_data[0][i].lower() + '.\n' #add what people would like
		bothlike += person2_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n'#by now you should understand this
	if person1_row[i + 1] == person2_row[i] == 'Yes':
		bothlike += person2_name + ' would like ' + all_data[0][i].lower() + '.\n'
		bothlike += person1_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n'
	if person1_row[i] == 'Yes':
		person1_score += 1
	if person2_row[i] == 'Yes':
		person2_score += 1

i_list_m4a = [77, 78, 79, 80] #list of all things males and only males would answer

for i in i_list_m4a: #for every number in that list
	if person1_row[i] == person2_row[i + 4] == 'Yes': #look at the spreadsheet to understand this, I'm not gonna try to explain
		bothlike += person1_name + ' would like ' + all_data[0][i].lower() + '.\n'
		bothlike += person2_name + ' would like ' + all_data[0][i + 4].lower() + '.\n\n' # the four only makes sense in context, I know I'm not supposed to use magic numbers but I did
		matchnum += 1
	if person2_row[i + 4] == person1_row[i] == 'Yes':
		bothlike += person2_name + ' would like ' + all_data[0][i].lower() + '.\n'
		bothlike += person1_name + ' would like ' + all_data[0][i + 4].lower() + '.\n\n'
		matchnum += 1
	if person1_row[i] != 'No':
		person1_score += 1
		total_score_helper += 1
		total_possible += 1
	if person2_row[i + 4] == 'No':
		total_possible += 1
	#	total_score_helper += 1
	if person1_row[i + 4] != 'No':
		person1_score += 1
		total_possible += 1
		total_score_helper += 1
	if person2_row[i] == 'No':
		total_possible += 1
	#	total_score_helper += 1


	
i_list_f4a = [86] #list of all things only females answer

for i in i_list_f4a: #for just that 86
	if person1_row[i] == person2_row[i + 1] == 'Yes': #if p1 says ya and p2 says ya
		bothlike += person1_name + ' would like ' + all_data[0][i].lower() + '.\n' #say that p1 likes
		bothlike += person2_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n' #say that p2 likes
		matchnum += 1 #add to matchnum
	if person2_row[i + 1] == person1_row[i] == 'Yes':
		bothlike += person2_name + ' would like ' + all_data[0][i].lower() + '.\n'
		bothlike += person1_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n\n'
		matchnum += 1
	if person1_row[i] != 'No':
		person1_score += 1
		total_possible += 1
		total_score_helper += 1

	if person2_row[i + 1] == 'No':
		total_possible += 1
	#	total_score_helper += 1

	if person1_row[i + 1] != 'No':
		person1_score += 1
		total_possible += 1
		total_score_helper += 1

	if person2_row[i] == 'No':
		total_possible += 1
	#	total_score_helper += 1



i_list_what = [49] #the first question in the set of four relating to whatment

if raw_input('Show whatment stats? (y/n): ').lower() == 'y':
	for i in i_list_what: #only once
		if person1_row[i] == person2_row[i + 1] == 'Yes':
		#Say if both p1 likes whating and p2 likes whatment
			bothlike += person1_name + ' would like ' + all_data[0][i].lower() + '.\n' 
			bothlike += person2_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n'
			bothlike += 'As the giver, ' + person1_name + ' would like the whatments: ' + person1_row[i + 2] + '\n\n'
			bothlike += 'As the receiver, ' + person2_name + ' would like the whatments: ' + person2_row[i + 3] + '\n\n'
		if person2_row[i + 1] == person1_row[i] == 'Yes':
			bothlike += person2_name + ' would like ' + all_data[0][i].lower() + '.\n'
			bothlike += person1_name + ' would like ' + all_data[0][i + 1].lower() + '.\n\n'
			bothlike += 'As the giver, ' + person2_name + ' would like the whatments: ' + person2_row[i + 2] + '\n\n'
			bothlike += 'As the receiver, ' + person1_name + ' would like the whatments: ' + person1_row[i + 3] + '\n\n'


if raw_input('Show people\'s top 5? (y/n): ').lower() == 'y':
	bothlike += person1_name  + ' is most interested in \n'  + person1_row[89] + '\n\n'
	bothlike += person2_name  + ' is most interested in \n'  + person2_row[89] + '\n\n'
    


otherscorecount = int(person1_row[10]) + int(person1_row[11]) - int(person2_row[10]) - int(person2_row[11])

if abs(otherscorecount) < 4:
	bothlike += person1_name + ' and ' + person2_name + ' have about the same otherscore.\n'
else:
	bothlike += person1_name + ' and ' + person2_name + ' have a slightly different otherscore.\n'

if otherscorecount >= 1:
	bothlike += person1_name + ' has a higher otherscore.\n\n'
if otherscorecount <= -1:
	bothlike += person2_name + ' has a higher otherscore.\n\n'


i_list_fives = [10, 11, 94]
total_possible += (5 * len(i_list_fives))

for i in i_list_fives:
	person1_score += int(person1_row[i])
	total_score_helper += 5
	person2_score += int(person2_row[i])
	matchnum += abs((5 - ((int(person1_row[i]) - int(person2_row[i])))))

babygrace = ''	
bothlike = bothlike.replace("my", "their").replace("i ", "they ").replace("your", "their").replace("you", "them").replace("we ", "they ").replace(" me", " them")

newnumber = int(((person1_score / total_score_helper) * 1000) + 5) / 1000.0
newnumber = ((newnumber * 100)) 
bothlike += person1_name + ' has ' + str(newnumber) + '% score\n'
babygrace += person1_name + ' has ' + str(newnumber) + '% score\n'
onlypersonone = person1_name + ' has ' + str(newnumber) + '% score\n'
newnumber = int(((person2_score / total_score_helper) * 1000) + 5) / 1000.0
newnumber = ((newnumber * 100)) 
bothlike += person2_name + ' has ' + str(newnumber) + '% score\n\n'
babygrace += person2_name + ' has ' + str(newnumber) + '% score\n\n'



newnum = int(((matchnum / total_possible) * 1000) + 5) / 1000.0
newnum = ((newnum * 100)) 
bothlike += str(newnum) + '% match, unadjusted\n'
babygrace += str(newnum) + '% match, unadjusted\n'
newnum = (newnum / 2) + 50
bothlike += str(newnum) + '% match, adjusted\n'
babygrace += str(newnum) + '% match, adjusted\n'




SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "***REMOVED***"
SMTP_PASSWORD = "NICE TRY PAL"

EMAIL_TO = ["ghs.central@gmail.com"]
#EMAIL_TO = [person1_email, person2_email]
EMAIL_FROM = "***REMOVED***"
EMAIL_SUBJECT = "score matching results : "

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

if raw_input('Just numbers? (y/n): ').lower() != 'n':
	DATA=onlypersonone
else:
	DATA=bothlike

def send_email():
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()

	
output = open('output', 'w')
output.write(DATA)