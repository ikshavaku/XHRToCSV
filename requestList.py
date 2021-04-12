import os
import json
import shutil
import csv

def generateReport(fileName):
	with open(fileName,encoding="utf8") as f:
		data=json.load(f)
	requestList=[x['request'] for x in data['log']['entries'] if x['_resourceType']=='xhr']
	responsList=[x['response'] for x in data['log']['entries'] if x['_resourceType']=='xhr']
	timeList= [x['time'] for x in data['log']['entries'] if x['_resourceType']=='xhr']
#	print(requestList,responsList)
	return (requestList,responsList,timeList)

if __name__ == '__main__':
	listOfFiles = os.listdir(os.getcwd())
	if not os.path.exists("Reports"):
		os.mkdir('Reports')
	pair=[['Method','URL','Status','Status Text','Time(ms)']]
	requestList,responsList = None,None
	for eachfile in listOfFiles:
		if eachfile.endswith('.har') :
			try :
				requestList,responsList,timeList = generateReport(eachfile)
			except:
				print(eachfile+" : File not proper..processing other files")
				continue
			print(eachfile+" : File processed successfully")
			for i in range(len(requestList)):
				pair.append([requestList[i]['method'],requestList[i]['url'],responsList[i]['status'],responsList[i]['statusText'],str(timeList[i])])
	with open('report.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(pair)
	if(os.path.exists(os.getcwd()+'\\Reports'+'\\Report.csv')):
		os.remove(os.getcwd()+'\\Reports'+'\\Report.csv')
	shutil.move(os.getcwd()+'\\'+'Report.csv',os.getcwd()+'\\Reports\\'+'Report.csv')

#,'?'.join(requestList[i]['url'].split('?')[1:]) if len(requestList[i]['url'].split('?'))>=2 else ''