#!/usr/bin/env python3
# -- coding: utf-8 --

import sys
import csv
import os
import json

import pandas as pd
import numpy as np

csv.field_size_limit(500 * 1024 * 1024)


def pre_process():

	all = []
	with open('./lda_3_dis.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		i=0
		messages=[]
		for line in reader:
			if i<1:
				i+=1   #这里的作用是把第一行去掉
			else:
				messages.append(line)   #读取第二列以后的数据
	    # print messages
		csvfile.close()
	    # print(messages)

		for message in messages:
			if len(message) and "@" in message[2]:
				# message[2].split()
				# To = message[3].split(',')
				# message[3] = To[0]
				# print(message[3])
				tmp = message[-1].split(",")
				# print(type(tmp))
				message[-1] = tmp[0][1:]
				# print(tmp[0][1:])
				all.append(message)

	
	new_all = []
	all_item = all
	# print("111",all_item[1:30])
	for t in all_item:
		try:
			t[-1] = int(t[-1])
			if int(t[-1]) == 0:
				t[-1] = "0"
				new_all.append(t)

			elif int(t[-1]) == 1:
				t[-1] = "1"
				new_all.append(t)

			elif int(t[-1]) == 2:
				t[-1] = "2"
				new_all.append(t)

			elif int(t[-1]) == 3:
				
				t[-1] = "3"
				new_all.append(t)

			elif int(t[-1]) == 4:
				
				t[-1] = "4"
				new_all.append(t)

			elif int(t[-1]) == 5:
				
				t[-1] = "5"
				new_all.append(t)

			# elif int(t[-1]) == 6:
				
			# 	t[-1] = "6"
			# 	new_all.append(t)


			# elif int(t[-1]) == 7:
				
			# 	t[-1] = "7"
			# 	new_all.append(t)

			# elif int(t[-1]) == 8:
				
			# 	t[-1] = "8"
			# 	new_all.append(t)

			# elif int(t[-1]) == 9:
				
			# 	t[-1] = "9"
			# 	new_all.append(t)

			# elif int(t[-1]) == 10:
				
			# 	t[-1] = "10"
			# 	new_all.append(t)

			# elif int(t[-1]) == 11:
				
			# 	t[-1] = "11"
			# 	new_all.append(t)

			# elif int(t[-1]) == 12:
				
			# 	t[-1] = "12"
			# 	new_all.append(t)

			# elif int(t[-1]) == 13:
				
			# 	t[-1] = "13"
			# 	new_all.append(t)
			# elif int(t[-1]) == 14:
				
			# 	t[-1] = "14"
			# 	new_all.append(t)

			# elif int(t[-1]) == 15:
				
			# 	t[-1] = "15"
			# 	new_all.append(t)

			# elif int(t[-1]) == 16:
				
			# 	t[-1] = "16"
			# 	new_all.append(t)

			# elif int(t[-1]) == 17:
				
			# 	t[-1] = "17"
			# 	new_all.append(t)
			# elif int(t[-1]) == 18:
				
			# 	t[-1] = "18"
			# 	new_all.append(t)
			# elif int(t[-1]) == 19:
				
			# 	t[-1] = "19"
			# 	new_all.append(t)

			# elif int(t[-1]) == 20:
				
			# 	t[-1] = "20"
			# 	new_all.append(t)

			# elif int(t[-1]) == 21:
				
			# 	t[-1] = "21"
			# 	new_all.append(t)
			# elif int(t[-1]) == 22:
				
			# 	t[-1] = "22"
			# 	new_all.append(t)

			# elif int(t[-1]) == 23:
				
			# 	t[-1] = "23"
			# 	new_all.append(t)

			# elif int(t[-1]) == 24:
				
			# 	t[-1] = "24"
			# 	new_all.append(t)
		except:
			pass

	# for item in new_all:
	# print("222",new_all[2:30])
	return new_all
    
def generate_episodes(text):
	e0=[]
	e1=[]
	e2=[]
	e3=[]
	e4=[]
	e5=[]
	# e6=[]
	# e7=[]
	# e8=[]
	# e9=[]
	# e10=[]
	# e11=[]
	# e12=[]
	# e13=[]
	# e14=[]
	# e15=[]
	# e16=[]
	# e17=[]
	# e18=[]
	# e19=[]
	# e20=[]
	# e21=[]
	# e22=[]
	# e23=[]
	# e24=[]
	for t in text:
		# print(int(t[-1]))	
		lda = t[-1].split(",")
		# print(lda)
		if int(lda[0]) == 0:
			From = "From_"+t[2]
			To = "To_"+t[3]
			e0.append(From)
			e0.append(To)

		elif int(lda[0]) == 1:
			From = "From_"+t[2]
			To = "To_"+t[3]
			e1.append(From)
			e1.append(To)

		elif int(lda[0]) == 2:
			From = "From_"+t[2]
			To = "To_"+t[3]
			e2.append(From)
			e2.append(To)

		elif int(lda[0]) == 3:
			From = "From_"+t[2]
			To = "To_"+t[3]
			e3.append(From)
			e3.append(To)

		elif int(lda[0]) == 4:
			From = "From_"+t[2]
			To = "To_"+t[3]
			e4.append(From)
			e4.append(To)

		elif int(lda[0]) == 5:

			From = "From_"+t[2]
			To = "To_"+t[3]
			e5.append(From)
			e5.append(To)

		# elif int(lda[0]) == 6:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e6.append(From)
		# 	e6.append(To)
		# elif int(lda[0]) == 7:
		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e7.append(From)
		# 	e7.append(To)

		# elif int(lda[0]) == 8:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e8.append(From)
		# 	e8.append(To)

		# elif int(lda[0]) == 9:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e9.append(From)
		# 	e9.append(To)
		# elif int(lda[0]) == 10:
		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e10.append(From)
		# 	e10.append(To)

		# elif int(lda[0]) == 11:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)
		# elif int(lda[0]) == 12:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 13:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)		

		# elif int(lda[0]) == 14:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)

		# elif int(lda[0]) == 15:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 16:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 17:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)		

		# elif int(lda[0]) == 18:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 19:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 20:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 21:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 22:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 23:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)	

		# elif int(lda[0]) == 24:

		# 	From = "From_"+t[2]
		# 	To = "To_"+t[3]
		# 	e11.append(From)
		# 	e11.append(To)											


	tmp = []
	tmp.append(e0)
	tmp.append(e1)
	tmp.append(e2)
	tmp.append(e3)
	tmp.append(e4)
	tmp.append(e5)
	# tmp.append(e6)
	# tmp.append(e7)
	# tmp.append(e8)
	# tmp.append(e9)
	# tmp.append(e10)
	# tmp.append(e11)
	# tmp.append(e12)
	# tmp.append(e13)
	# tmp.append(e14)
	# tmp.append(e15)
	# tmp.append(e16)
	# tmp.append(e17)
	# tmp.append(e18)
	# tmp.append(e19)
	# tmp.append(e20)
	# tmp.append(e21)
	# tmp.append(e22)
	# tmp.append(e23)
	# tmp.append(e24)
	# print(tmp)
	all = []
	lda = ["0",
	"1",
	"2",
	"3",
	"4",
	"5"
	# "6",
	# "7",
	# "8",
	# "9",
	# "10",
	# "11",
	# "12",
	# "13",
	# "14",
	# "15",
	# "16",
	# "17"
	# "18",
	# "19",
	# "20",
	# "21",
	# "22",
	# "23",
	# "24"
	]
	for x in range(14):
		j = {
			"type": "episode",
			"name": lda[x],
			"description": "",
			"episode": x+1,
			# "date": "2012-05-05 23:50:11",
			"slug": "",
			"links": tmp[x]
		}
		all.append(j)
	# all = json.dumps(all)

	# print(all)
	return all








def generate_json(text):
	# all_From = ["jeff.dasovich@enron.com",]
	all = []
	for t in text:
		# if t[0][:7] == "2001-04":
			
			t1 = {
				"From" : t[1],
				"To" : t[2],
				"time" : t[0][:7],
                # "day": t[0][8:10],
                # "hour": t[0][11:13],
				"theme" : t[-1]
			}
			all.append(t1)
		# print(t1)
	# print("333",all[3:30])

	return all


def generate_Node(text):
	# all_From = ["vince.kaminski@enron.com","enron.announcements@enron.com","jeff.dasovich@enron.com","kay.mann@enron.com","owner-eveningmba@haas.berkeley.edu","exchangeinfo@nymex.com","eric.bass@enron.com","evelyn.metoyer@enron.com","office.chairman@enron.com","susan.mara@enron.com","eric.bass@enron.com","leslie.hansen@enron.com","robin.rodrigue@enron.com","joseph.alamo@enron.com","kerri.thompson@enron.com","jeffrey.shankman@enron.com","kate.symes@enron.com","sara.shackleton@enron.com","james.steffes@enron.com","karen.denne@enron.com"]
	# all_to =["vkaminski@aol.com","vkamins@enron.com","all.worldwide@enron.com","all.houston@enron.com","james.steffes@enron.com","suzanne_nimocks@mckinsey.com","eveningmba@haas.berkeley.edu","paul.kaufman@enron.com","nancy.sellers@robertmondavi.com","karen.denne@enron.com","shirley.crenshaw@enron.com","susan.mara@enron.com","sara.shackleton@enron.com","houston.report@enron.com","nmann@erac.com","shanna.husser@enron.com","all_ena_egm_eim@enron.com","kate.symes@enron.com","joseph.alamo@enron.com","jeff.dasovich@enron.com","all.states@enron.com","richard.shapiro@enron.com","jason.bass2@compaq.com","tana.jones@enron.com","ben.jacoby@enron.com","kathleen.carnahan@enron.com","gabriel.monroy@enron.com","jennifer.burns@enron.com","evelyn.metoyer@enron.com","mark.taylor@enron.com","kerri.thompson@enron.com","carlos.sole@enron.com","cameron@perfect.com"]
	From = []
	To = []
	Time = []
	Topic = []
	Day = []
	Hour = []
	for t in text:
		# print(t)
		# if t["From"] in all_From:
		# 	if t["To"] in all_to:
		From.append(t["From"])
		To.append(t["To"])
		Time.append(t["time"])
		# Day.append(t["day"])
		# Hour.append(t["hour"])
		Topic.append(t["theme"])
	Node = []
	From_set = list(set(From))
	To_set = list(set(To))
	Time_set = list(set(Time))
	# Day_set = list(set(Day))
	# Hour_set = list(set(Hour))
	Topic_set = list(set(Topic))

	# Ip_set1 = ["50.63.202.69","88.221.214.57","35.185.1.153"]
	# Ip_set2 = ["50.63.202.69","188.125.72.165","35.185.1.153","63.131.135.125","52.41.61.31","68.142.185.67","172.22.225.239"]
    
	for f in From_set:
		f1 = {
	        "disp": "From_"+f,
	        "name": "From_"+f
		}
		Node.append(f1)

	for to in To_set:
		to1 = {
	        "disp": "To_"+to,
	        "name": "To_"+to		
		}
		Node.append(to1)

	for time in Time_set:
		time1 = {
	        "disp": "Date_"+time,
	        "name": "Date_"+time		
		}
		Node.append(time1)	


	# for day in Day_set:
	# 	day1 = {
	#         "disp": "Day_"+day,
	#         "name": "Day_"+day	
	# 	}
	# 	# print(topic1)
	# 	Node.append(day1)	   	


	# for hour in Hour_set:
	# 	hours = {
	#         "disp": "Hour_"+hour,
	#         "name": "Hour_"+hour	
	# 	}
	# 	Node.append(hours)	

	for topic in Topic_set:
		topic1 = {
	        "disp": "Topic_"+topic,
	        "name": "Topic_"+topic	
		}
		# print(topic1)
		Node.append(topic1)		

	print(text)
	t = list(set(text[0]))
	# print(Node[1:30])
	return Node


def generate_flows(text):
	result = []
	text1 = []
	# all_From = ["vince.kaminski@enron.com","enron.announcements@enron.com","jeff.dasovich@enron.com","kay.mann@enron.com","owner-eveningmba@haas.berkeley.edu","exchangeinfo@nymex.com","eric.bass@enron.com","evelyn.metoyer@enron.com","susan.mara@enron.com","eric.bass@enron.com","leslie.hansen@enron.com","robin.rodrigue@enron.com","joseph.alamo@enron.com","kerri.thompson@enron.com","jeffrey.shankman@enron.com","kate.symes@enron.com","sara.shackleton@enron.com","james.steffes@enron.com","karen.denne@enron.com"]
	# all_to =["vkaminski@aol.com","vkamins@enron.com","all.worldwide@enron.com","all.houston@enron.com","james.steffes@enron.com","suzanne_nimocks@mckinsey.com","eveningmba@haas.berkeley.edu","paul.kaufman@enron.com","nancy.sellers@robertmondavi.com","karen.denne@enron.com","shirley.crenshaw@enron.com","susan.mara@enron.com","sara.shackleton@enron.com","houston.report@enron.com","nmann@erac.com","shanna.husser@enron.com","all_ena_egm_eim@enron.com","kate.symes@enron.com","joseph.alamo@enron.com","jeff.dasovich@enron.com","all.states@enron.com","richard.shapiro@enron.com","jason.bass2@compaq.com","tana.jones@enron.com","ben.jacoby@enron.com","kathleen.carnahan@enron.com","gabriel.monroy@enron.com","jennifer.burns@enron.com","evelyn.metoyer@enron.com","mark.taylor@enron.com","kerri.thompson@enron.com","carlos.sole@enron.com","cameron@perfect.com"]
		
	for tex in text:
		# if tex["From"] in all_From:
		# 	if tex["To"] in all_to:
		# 
		tmp = (tex["From"],tex["To"],tex["time"],tex["theme"])
		text1.append(tmp)

	# print(text1)
	
	text_set = list(set(text1))	

	# print(text_set)
	count = [0 for i in range(len(text_set))]
	for i in text1:
		count[text_set.index(i)] += 1
	for t in text_set: 
		index = text_set.index(t)
		num = count[index]
		new_text = t + (num,)
		# print(new_tup)
		result.append(new_text)

	flow = []
	# print("23232323",result[1:40])
	for r in result:
		tmp = []
		print(r)
		# domain = r[0].split("@")[1]
		# domain1 = r[1].split("@")[1]
		# Ip_set1 = ["50.63.202.69","88.221.214.57","35.185.1.153","63.131.135.125","52.41.61.31"]
		# Ip_set2 = ["50.63.202.69","188.125.72.165","35.185.1.153","63.131.135.125","52.41.61.31","68.142.185.67","172.22.225.239"]


		tmp.append("From_"+r[0])

		# if domain == "enron.com":
		# 	tmp.append("From_ip_"+Ip_set1[0])
		# elif domain == "nymex.com":
		# 	tmp.append("From_ip_"+Ip_set1[1])
		# elif domain == "haas.berkeley.edu":
		# 	tmp.append("From_ip_"+Ip_set1[2])
		# elif domain == "erac.com":
		# 	tmp.append("From_ip_"+Ip_set1[3])
		# elif domain == "robertmondavi.com":
		# 	tmp.append("From_ip_"+Ip_set1[4])


		tmp.append("Date_"+r[2])

		tmp.append("Topic_"+r[3])
		# tmp.append("Day_"+r[4])
		# tmp.append("Hour_"+r[5])
		# if domain1 == "enron.com":
		# 	tmp.append("To_ip_"+Ip_set2[0])
		# elif domain1 == "aol.com":
		# 	tmp.append("To_ip_"+Ip_set2[1])
		# elif domain1 == "haas.berkeley.edu":
		# 	tmp.append("To_ip_"+Ip_set2[2])
		# elif domain1 == "erac.com":
		# 	tmp.append("To_ip_"+Ip_set2[3])
		# elif domain1 == "robertmondavi.com":
		# 	tmp.append("To_ip_"+Ip_set2[4])		
		# elif domain1 == "perfect.com":
		# 	tmp.append("To_ip_"+Ip_set2[5])	
		# elif domain1 == "compaq.com":
		# 	tmp.append("To_ip_"+Ip_set2[6])			

		tmp.append("To_"+r[1])


		tmp1 = {
			"thru": tmp,
			"value": r[4]
	    }
		flow.append(tmp1)

	# print(flow)
	print("1111111111",flow[1:50])
	return flow



if __name__=="__main__":
	text = pre_process()
	
	all_json = generate_json(text)
	Nodes = generate_Node(all_json)
	Flows = generate_flows(all_json)
	# print(Nodes[1:5])
	# print(Flows[1:5])

	# all_themes =  generate_themes(text)
	# all_episodes = generate_episodes(text)
	# all_perspectives = generate_perspectives(text)
	# all = {
	# 	"episodes": all_episodes,
	# 	"themes": all_themes,
	# 	"perspectives": all_perspectives
	# }
	# print(all_episodes)

	with open('titanic-data3.json', 'w') as json_file:
		json_file.write(json.dumps(Nodes))
		json_file.write(json.dumps(Flows))
	# # 	# return data
		print("all over")

	# print(all_perspectives)
