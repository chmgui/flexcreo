# flexlic01.py process flex license manager log files ...
#
# 
# 08/21/2022 - CMGUI

from datetime import datetime
import zoneinfo
#from zoneinfo import ZoneInfo
from datetime import timezone
from datetime import timedelta
import json
import tkinter
from tkinter import filedialog
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def detect_daemon1(filename1):
	# find out the daemon from the line Vendor daemon: ptc_d, Vendor daemon: SW_D
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	for line1 in lines1:
		if line1.find('Vendor daemon: ') != -1:
			return( line1[line1.rfind(':')+1:].strip() )
			break
	return(False)

def timezone_win_iana_mapping1(tz1):
	# this maps Windows time zone names to Unix/IANA time zone names used by Python Datetime
	timezone_win_iana1 = [
	{'Dateline Standard Time': 'Etc/GMT+12'} ,
	{'UTC-11': 'Etc/GMT+11'} ,
	{'Aleutian Standard Time': 'America/Adak'} ,
	{'Hawaiian Standard Time': 'Pacific/Honolulu'} ,
	{'Marquesas Standard Time': 'Pacific/Marquesas'} ,
	{'Alaskan Standard Time': 'America/Anchorage'} ,
	{'UTC-09': 'Etc/GMT+9'} ,
	{'Pacific Standard Time (Mexico)': 'America/Tijuana'} ,
	{'UTC-08': 'Etc/GMT+8'} ,
	{'Pacific Standard Time': 'America/Los_Angeles'} ,
	{'US Mountain Standard Time': 'America/Phoenix'} ,
	{'Mountain Standard Time (Mexico)': 'America/Chihuahua'} ,
	{'Mountain Standard Time': 'America/Denver'} ,
	{'Central America Standard Time': 'America/Guatemala'} ,
	{'Central Standard Time': 'America/Chicago'} ,
	{'Easter Island Standard Time': 'Pacific/Easter'} ,
	{'Central Standard Time (Mexico)': 'America/Mexico_City'} ,
	{'Canada Central Standard Time': 'America/Regina'} ,
	{'SA Pacific Standard Time': 'America/Bogota'} ,
	{'Eastern Standard Time (Mexico)': 'America/Cancun'} ,
	{'Eastern Standard Time': 'America/New_York'} ,
	{'Haiti Standard Time': 'America/Port-au-Prince'} ,
	{'Cuba Standard Time': 'America/Havana'} ,
	{'US Eastern Standard Time': 'America/Indiana/Indianapolis'} ,
	{'Turks And Caicos Standard Time': 'America/Grand_Turk'} ,
	{'Paraguay Standard Time': 'America/Asuncion'} ,
	{'Atlantic Standard Time': 'America/Halifax'} ,
	{'Venezuela Standard Time': 'America/Caracas'} ,
	{'Central Brazilian Standard Time': 'America/Cuiaba'} ,
	{'SA Western Standard Time': 'America/La_Paz'} ,
	{'Pacific SA Standard Time': 'America/Santiago'} ,
	{'Newfoundland Standard Time': 'America/St_Johns'} ,
	{'Tocantins Standard Time': 'America/Araguaina'} ,
	{'E. South America Standard Time': 'America/Sao_Paulo'} ,
	{'SA Eastern Standard Time': 'America/Cayenne'} ,
	{'Argentina Standard Time': 'America/Argentina/Buenos_Aires'} ,
	{'Greenland Standard Time': 'America/Godthab'} ,
	{'Montevideo Standard Time': 'America/Montevideo'} ,
	{'Magallanes Standard Time': 'America/Punta_Arenas'} ,
	{'Saint Pierre Standard Time': 'America/Miquelon'} ,
	{'Bahia Standard Time': 'America/Bahia'} ,
	{'UTC-02': 'Etc/GMT+2'} ,
	{'Mid-Atlantic Standard Time': 'Etc/GMT+2'} ,
	{'Azores Standard Time': 'Atlantic/Azores'} ,
	{'Cape Verde Standard Time': 'Atlantic/Cape_Verde'} ,
	{'UTC': 'Etc/UTC'} ,
	{'Morocco Standard Time': 'Africa/Casablanca'} ,
	{'GMT Standard Time': 'Europe/London'} ,
	{'Greenwich Standard Time': 'Atlantic/Reykjavik'} ,
	{'W. Europe Standard Time': 'Europe/Berlin'} ,
	{'Central Europe Standard Time': 'Europe/Budapest'} ,
	{'Romance Standard Time': 'Europe/Paris'} ,
	{'Sao Tome Standard Time': 'Africa/Sao_Tome'} ,
	{'Central European Standard Time': 'Europe/Warsaw'} ,
	{'W. Central Africa Standard Time': 'Africa/Lagos'} ,
	{'Jordan Standard Time': 'Asia/Amman'} ,
	{'GTB Standard Time': 'Europe/Bucharest'} ,
	{'Middle East Standard Time': 'Asia/Beirut'} ,
	{'Egypt Standard Time': 'Africa/Cairo'} ,
	{'E. Europe Standard Time': 'Europe/Chisinau'} ,
	{'Syria Standard Time': 'Asia/Damascus'} ,
	{'West Bank Standard Time': 'Asia/Hebron'} ,
	{'South Africa Standard Time': 'Africa/Johannesburg'} ,
	{'FLE Standard Time': 'Europe/Kiev'} ,
	{'Israel Standard Time': 'Asia/Jerusalem'} ,
	{'Kaliningrad Standard Time': 'Europe/Kaliningrad'} ,
	{'Sudan Standard Time': 'Africa/Khartoum'} ,
	{'Libya Standard Time': 'Africa/Tripoli'} ,
	{'Namibia Standard Time': 'Africa/Windhoek'} ,
	{'Arabic Standard Time': 'Asia/Baghdad'} ,
	{'Turkey Standard Time': 'Europe/Istanbul'} ,
	{'Arab Standard Time': 'Asia/Riyadh'} ,
	{'Belarus Standard Time': 'Europe/Minsk'} ,
	{'Russian Standard Time': 'Europe/Moscow'} ,
	{'E. Africa Standard Time': 'Africa/Nairobi'} ,
	{'Iran Standard Time': 'Asia/Tehran'} ,
	{'Arabian Standard Time': 'Asia/Dubai'} ,
	{'Astrakhan Standard Time': 'Europe/Astrakhan'} ,
	{'Azerbaijan Standard Time': 'Asia/Baku'} ,
	{'Russia Time Zone 3': 'Europe/Samara'} ,
	{'Mauritius Standard Time': 'Indian/Mauritius'} ,
	{'Saratov Standard Time': 'Europe/Saratov'} ,
	{'Georgian Standard Time': 'Asia/Tbilisi'} ,
	{'Caucasus Standard Time': 'Asia/Yerevan'} ,
	{'Afghanistan Standard Time': 'Asia/Kabul'} ,
	{'West Asia Standard Time': 'Asia/Tashkent'} ,
	{'Ekaterinburg Standard Time': 'Asia/Yekaterinburg'} ,
	{'Pakistan Standard Time': 'Asia/Karachi'} ,
	{'India Standard Time': 'Asia/Kolkata'} ,
	{'Sri Lanka Standard Time': 'Asia/Colombo'} ,
	{'Nepal Standard Time': 'Asia/Kathmandu'} ,
	{'Central Asia Standard Time': 'Asia/Almaty'} ,
	{'Bangladesh Standard Time': 'Asia/Dhaka'} ,
	{'Omsk Standard Time': 'Asia/Omsk'} ,
	{'Myanmar Standard Time': 'Asia/Yangon'} ,
	{'SE Asia Standard Time': 'Asia/Bangkok'} ,
	{'Altai Standard Time': 'Asia/Barnaul'} ,
	{'W. Mongolia Standard Time': 'Asia/Hovd'} ,
	{'North Asia Standard Time': 'Asia/Krasnoyarsk'} ,
	{'N. Central Asia Standard Time': 'Asia/Novosibirsk'} ,
	{'Tomsk Standard Time': 'Asia/Tomsk'} ,
	{'China Standard Time': 'Asia/Shanghai'} ,
	{'North Asia East Standard Time': 'Asia/Irkutsk'} ,
	{'Singapore Standard Time': 'Asia/Singapore'} ,
	{'W. Australia Standard Time': 'Australia/Perth'} ,
	{'Taipei Standard Time': 'Asia/Taipei'} ,
	{'Ulaanbaatar Standard Time': 'Asia/Ulaanbaatar'} ,
	{'North Korea Standard Time': 'Asia/Pyongyang'} ,
	{'Aus Central W. Standard Time': 'Australia/Eucla'} ,
	{'Transbaikal Standard Time': 'Asia/Chita'} ,
	{'Tokyo Standard Time': 'Asia/Tokyo'} ,
	{'Korea Standard Time': 'Asia/Seoul'} ,
	{'Yakutsk Standard Time': 'Asia/Yakutsk'} ,
	{'Cen. Australia Standard Time': 'Australia/Adelaide'} ,
	{'AUS Central Standard Time': 'Australia/Darwin'} ,
	{'E. Australia Standard Time': 'Australia/Brisbane'} ,
	{'AUS Eastern Standard Time': 'Australia/Sydney'} ,
	{'West Pacific Standard Time': 'Pacific/Port_Moresby'} ,
	{'Tasmania Standard Time': 'Australia/Hobart'} ,
	{'Vladivostok Standard Time': 'Asia/Vladivostok'} ,
	{'Lord Howe Standard Time': 'Australia/Lord_Howe'} ,
	{'Bougainville Standard Time': 'Pacific/Bougainville'} ,
	{'Russia Time Zone 10': 'Asia/Srednekolymsk'} ,
	{'Magadan Standard Time': 'Asia/Magadan'} ,
	{'Norfolk Standard Time': 'Pacific/Norfolk'} ,
	{'Sakhalin Standard Time': 'Asia/Sakhalin'} ,
	{'Central Pacific Standard Time': 'Pacific/Guadalcanal'} ,
	{'Russia Time Zone 11': 'Asia/Kamchatka'} ,
	{'New Zealand Standard Time': 'Pacific/Auckland'} ,
	{'UTC+12': 'Etc/GMT-12'} ,
	{'Fiji Standard Time': 'Pacific/Fiji'} ,
	{'Kamchatka Standard Time': 'Asia/Kamchatka'} ,
	{'Chatham Islands Standard Time': 'Pacific/Chatham'} ,
	{'UTC+13': 'Etc/GMT-13'} ,
	{'Tonga Standard Time': 'Pacific/Tongatapu'} ,
	{'Samoa Standard Time': 'Pacific/Apia'} ,
	{'Line Islands Standard Time': 'Pacific/Kiritimati'} ,
	]
	#print( "timezone_win_iana : ", timezone_win_iana)
	#res1 = [ x1 for x1 in timezone_win_iana1.keys() if x1 == tz1 ]
	#list2 = [ x1 for sub1 in list1 for x1 in sub1.items() ]
	#res1 = [ y1 for sub1 in timezone_win_iana1 for x1, y1 in sub1.items() if x1 == tz1 ]
	res1 = [ y1 for sub1 in timezone_win_iana1 for x1, y1 in sub1.items() if x1 == tz1 ]
	if res1:
		return res1[0].strip()
	else:
		# maps Daylight time, e.g., Pacific Daylight Time to be same as Pacific Standard Time
		if tz1.find('Daylight') != -1:
			tz1 = tz1.replace('Daylight','Standard')
			res1 = [ y1 for sub1 in timezone_win_iana1 for x1, y1 in sub1.items() if x1 == tz1 ]
			if res1:
				return res1[0].strip()
			else:
				return(False)
	return(False)


def detect_timezone_startdate1(filename1):
	# Returns the IANA Time Zone and the starting date of the log file
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	for line1 in lines1:
		if line1.find('-SLOG@) Start-Date: ') != -1 or line1.find('-SLOG@) Time:') != -1:
			tz1 = line1[line1.rfind(':')+3:].strip()
			if line1.find('-SLOG@) Start-Date:') != -1: 
				currentdate1 = line1[ line1.find('-SLOG@) Start-Date:') + 23:]
			elif line1.find('-SLOG@) Time:') != -1:
				currentdate1 = line1[ line1.find('-SLOG@) Time:') + 18:]
			if currentdate1.find(':') == -1:
				print("error at line 200: currentdate1.find(':') == -1")
			else:
				currentdate1 = currentdate1[:currentdate1.find(':')-3].strip()
			dt_obj = datetime.strptime(currentdate1 + ' 00:00:00', '%b %d %Y %H:%M:%S')
			origin_tz = zoneinfo.ZoneInfo(timezone_win_iana_mapping1(tz1))
			dt_obj = datetime( dt_obj.year, dt_obj.month, dt_obj.day, tzinfo=origin_tz)
			return timezone_win_iana_mapping1(tz1), dt_obj
			break
	return(False)

# def get_filenames1():
# 	currdir = os.getcwd()
# 	root1 = tkinter.Tk()
# 	root1.withdraw()
# 	#file_path1 = filedialog.askopenfilename()
# 	# note that tkinter.filedialog does not work. Need to have from tkinter import filedialog
# 	root1.filename =  filedialog.askopenfilenames(initialdir = os.getcwd(),title = "Select a log file or multiple log files",filetypes = (("log files","*.log"),("all files","*.*")))
# 	return(root1.filename)

def get_filename1():
	# Prompts user to select a log file via Windows Explorer browser
	currdir = os.getcwd()
	root1 = tkinter.Tk()
	root1.withdraw()
	#file_path1 = filedialog.askopenfilename()
	# note that tkinter.filedialog does not work. Need to have from tkinter import filedialog
	#root1.filename =  filedialog.askopenfilenames(initialdir = os.getcwd(),title = "Select a log file or multiple log files",filetypes = (("log files","*.log"),("all files","*.*")))
	root1.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select a log file",filetypes = (("log files","*.log"),("all files","*.*")))
	return(root1.filename)


def detect_features1(filename1):
	# Returns the license features in the log file, e.g., PROE_EssentialsIIM
	# The features are found in the lines starting from ... Server started on PA014 for:	275
	# and ending before the line EXTERNAL FILTERS are OFF
	# Just in case EXTERNAL FILTERS are OFF line is not found, we stop at the lines:
	# SLOG: Statistics Log Frequency is, SLOG: TS update poll interval is, etc.
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	features1 = []
	found1 = 0
	for i, line1 in enumerate(lines1):
		if line1.find(') Server started on ') != -1:
			features1.append(line1[line1.rfind(':') + 1:].strip())
			break
	if i >= len(lines1):
		return(False)
	else:
		for j in range(i+1,len(lines1)):
			line1 = lines1[j]
			if line1.find(') EXTERNAL FILTERS are OFF') != -1:
				found1 = 1
				break
			elif line1.find(') SLOG: Statistics Log Frequency is ') != -1:
				found1 = 2
				break
			elif line1.find(') SLOG: TS update poll interval is ') != -1:
				found1 = 2
				break
			elif line1.find(') SLOG: Activation borrow reclaim percentage is ') != -1:
				found1 = 2
				break
			else:
				temp1 = line1[ line1.find(')') + 1: ]
				temp1 = temp1.replace('\t', ' ')
				#print('temp1 = ', temp1)
				temp1 = temp1.split()
				features1.extend(temp1)
				#print('temp1 = ', temp1)
	if found1 != 0:
		if found1 == 2:
			for item1 in temp1:
				features1.remove(item1)
			# if there is no EXTERNAL FILTERS are OFF line and we reached 
			# SLOG: Statistics Log Frequency is, we remove the last line added 
			# to features1 because it is unlikely to contain license features
		return(features1)
	else:	
		return(False)

def select_features1(features1):
	# Prompts user to select one or more feature to analyze
	root1 = tkinter.Tk()
	root1.title("Select one or more feature")
	root1.geometry('320x200')
	listbox1 = tkinter.Listbox(root1, width=40, height=10, selectmode='multiple')
	listbox1.pack()
	for item in features1:
	    listbox1.insert('end', item)
	# Function for printing the
	# selected listbox value(s)
	def ok1():
	    # Traverse the tuple returned by
	    # curselection method and print
	    # corresponding value(s) in the listbox
	    # for i in listbox1.curselection():
	    #     temp1.append(listbox1.get(i))
	    #     print(listbox1.get(i))
	    root1.quit()
	    #root1.destroy()
	    return

	def on_closing1():
		# when user clicks on X to close the windows, ask if want to quit
	    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
	        root1.destroy()
	        exit()
	    return
	#show1 = tkinter.Label(root1, text = "Select one or more options", font = ("Helvtica", 10), padx = 10, pady = 10)
	#show1.pack() 
	button1 = tkinter.Button(root1, text="OK", command=ok1)
	button1.pack()
	# below handles the event of user clicking on X to close the Tk window
	root1.protocol("WM_DELETE_WINDOW", on_closing1)
	root1.mainloop()
	temp1 = []
	for i in listbox1.curselection():
	    temp1.append(listbox1.get(i))
	#     print(listbox1.get(i))
	# print(temp1)
	root1.quit()
	root1.destroy()
	return temp1

def get_lastdate1(filename1,tz1):
	# get the last date in the log file. First get date from a line nearest to end of log file
	# containing date info. After that, check if there is a decrease in the time at the 
	# beginning of line from previous line. If yes, add one day to date.
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	for j, line1 in enumerate(lines1[::-1]):
		if line1.find('-SLOG@) Start-Date:') != -1 or line1.find('-SLOG@) Time:') != -1:
			if line1.find('-SLOG@) Start-Date:') != -1: 
				currentdate1 = line1[ line1.find('-SLOG@) Start-Date:') + 23:]
			elif line1.find('-SLOG@) Time:') != -1:
				currentdate1 = line1[ line1.find('-SLOG@) Time:') + 18:]
			if currentdate1.find(':') == -1:
				print("error at line 300: currentdate1.find(':') == -1")
			else:
				currentdate1 = currentdate1[:currentdate1.find(':')-3].strip()
			dt_obj = datetime.strptime(currentdate1 + ' 00:00:00', '%b %d %Y %H:%M:%S')
			origin_tz = zoneinfo.ZoneInfo(tz1)
			dt_obj = datetime( dt_obj.year, dt_obj.month, dt_obj.day, tzinfo=origin_tz)
			break
	hrprev1 = 0
	for line1 in lines1[-j:]:
		#print(line1)
		if line1.find(':') != -1 and line1.find('(') != -1:
			t1 = line1[:line1.find('(')].strip().split(':')
			hr1 = t1[0]
			if hr1.isdigit():
				hr1 = int(hr1)
				if hr1 < 24:
					if hr1 < hrprev1:
						if dt_obj:
							dt_obj = dt_obj + timedelta(hours=24)
				hrprev1 = hr1
	if dt_obj:
		return dt_obj
	else:
		return False

# def create_in_list1(filename1):
#     with open(filename1, 'r') as f1:
#         lines1 = f1.readlines()
#     list1 = []
#     for line1 in lines1:
#         #if line1.find('(ptc_d) OUT: "') != -1 or line1.find('(ptc_d) IN: "') != -1:
#         if line1.find('(ptc_d) IN: "') != -1:
#             #list2 = [ line1, False ]
#             #list1.append(list2)
#             list1.append(line1)
#     return list1

def create_in_list1(list2):
	# Returns a list containing only the the lines with ') IN; ', i.e., returning of
	# license to license server. list2 is the list with datetime added to beginning of
	# each line, i.e., the list returned by create_datetime_list1(filename1)
	# This in_list is used by the find_in_time1 function.
	in_list2 = []
	for line1 in list2:
	    #if line1.find('(ptc_d) OUT: "') != -1 or line1.find('(ptc_d) IN: "') != -1:
	    if line1[1].find(') IN: "') != -1:
	        #list2 = [ line1, False ]
	        #list1.append(list2)
	        in_list2.append([line1[0],line1[1]])
	return in_list2

# def find_in_time1(in_list1, feat1, user1):
# 	if in_list1:
# 		for line1 in in_list1:
# 			if line1.find(' IN: "' + feat1 + '" ' + user1) != -1:
# 				in_list1.pop(line1)
# 				if line1.find('(INACTIVE)') != -1:
# 					#temp1 = line1[:line1.find('(SW_D)')-1].strip()
# 					return line1[:line1.find('(')-1].strip(), True, line1
# 				else:
# 					return line1[:line1.find('(')-1].strip(), False, line1
# 	return None, False, None  

def find_in_time1(in_list1, feat1, user1):
	# Returns the IN time (time license was returned) for a given feature and user (an OUT),
	# whether the license was returned because of INACTIVE (only applies to PTC), and
	# the line itself. Search the in_list1 (a list of all the IN lines) and pops (remove)
	# the line from in_list1 which matches the feature and user of the the OUT line.
	# Because the in_list1 is in chronological order, this will work.
	if in_list1:
		for i, line1 in enumerate(in_list1):
			if line1[1].find(' IN: "' + feat1 + '" ' + user1) != -1:
				in_list1.pop(i)
				if line1[1].find('(INACTIVE)') != -1:
					#temp1 = line1[:line1.find('(SW_D)')-1].strip()
					return line1[0], True, line1[1]
				else:
					return line1[0], False, line1[1]
	return None, False, None  

def get_time_in_line1(line1):
	# get the time at the beginning of line and return it in array t1[hr, min, sec]
	t1 = []
	if line1.find(':') != -1 and line1.find('(') != -1:
			t1 = line1[:line1.find('(')].strip().split(':')
			if len(t1) == 3:
				if t1[0].isdigit() and t1[1].isdigit() and t1[2].isdigit():
					t1[0] = int(t1[0])
					t1[1] = int(t1[1])
					t1[2] = int(t1[2])
					if t1[0] < 24 and t1[1] < 60 and t1[2] < 60:
						#print(t1)
						#input("?")
						return t1
					else:
						return False
				else:
					return False
	return False


def create_datetime_list1(filename1):
	# create a list with the datetime added to the beginning of line.
	# The time at the beginning of each line in the log file only shows the hr:mm:ss and 
	# we won't know the date.  
	# We get the date from these two lines: -SLOG@) Start-Date: and -SLOG@) Time:
	# The line containing TIMESTAMP 3/3/2022 may not be useful because the Date Format
	# of the Windows machine hosting the license server will affect the date format of this 
	# line.  Hopefully the "Start-Date: Sun May 01 2022 ..." and -SLOG@) Time: Mon May 02 2022 
	# lines won't be affected by Windows Date Format of the license server.
	# We also check if the time is lesser than the previous line. If so, we add 24 hours to 
	# the date.
	list1 = []
	t1 = []
	tz, dt_obj = detect_timezone_startdate1(filename1)
	dt_obj2 = dt_obj
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	hrprev1 = 0
	for line1 in lines1:
		t1 = get_time_in_line1(line1)
		#print(t1)
		#input("?")
		if t1 and dt_obj:
			if line1.find('-SLOG@) Start-Date: ') != -1 or line1.find('-SLOG@) Time:') != -1:
				#tz1 = line1[line1.rfind(':')+3:].strip()
				if line1.find('-SLOG@) Start-Date:') != -1: 
					currentdate1 = line1[ line1.find('-SLOG@) Start-Date:') + 23:]
				elif line1.find('-SLOG@) Time:') != -1:
					currentdate1 = line1[ line1.find('-SLOG@) Time:') + 18:]
				if currentdate1.find(':') == -1:
					print("ERROR at line 384: currentdate1.find(':') == -1")
				else:
					currentdate1 = currentdate1[:currentdate1.find(':')-3].strip()
					dt_obj = datetime.strptime(currentdate1 + ' 00:00:00', '%b %d %Y %H:%M:%S')
					origin_tz = zoneinfo.ZoneInfo(tz1)
					dt_obj = datetime( dt_obj.year, dt_obj.month, dt_obj.day, tzinfo=origin_tz)

			elif t1[0] < hrprev1:
				#print(line1)
				#input("?")
				#pass
				dt_obj += timedelta(hours=24)
			#print("hrprev1 t1[0] = ", hrprev1, t1[0], dt_obj)
			hrprev1 = t1[0]
			dt_obj2 = dt_obj + timedelta(hours=t1[0], minutes=t1[1], seconds=t1[2])
			#print("hrprev1 t1[0] = ", hrprev1, t1[0], dt_obj)
			#input("?")
			#print(dt_obj)
			list1.append([dt_obj2, line1])
	return list1


def process_list1(list1, daemon1, features_sel1):
	# This is the main function to process the list1 (lines of the log file with datetime added).
	# It returns the license_use1 list which matches each license OUT with an IN.
	# The denied_use1 list contains all the lines with license DENIED:
	# daemon1 is not used for the time being
	# features_sel1 is list containing all the license features selected by user for analysis
	license_use1 = []
	#license_denied1 = []
	#feature_use1 = []
	denied_use1 = []
	count1 = 0
	in_list1 = create_in_list1(list1)
	for line1 in list1:
		feature1 = line1[1][ line1[1].find('"')+1:line1[1].rfind('"')].strip()
		if feature1 in features_sel1:
			if line1[1].find(') OUT: ') != -1:
				user1 = line1[1][line1[1].rfind('"')+2:].strip()
				in_time1, inactive1, in_time_line1 = find_in_time1(in_list1,feature1,user1)
				# print(in_time1, inactive1, in_time_line1)
				# input("?")
				# If there is no in_time1, i.e., no IN matching the OUT (license not returned),
				# we use the last date time of the log file as the IN time if it is not 
				# more than 24 hours from the OUT time, else we use OUT time + 24 hours.
				if in_time1 is None:
					if (list1[len(list1)-1][0] - line1[0]).total_seconds()/3600 < 24:  
						in_time1 =  list1[len(list1)-1][0] 
					else:
						in_time1 = line1[0] + timedelta(hours=24)
				count1 += 1
				templist1 = [ feature1, 
				line1[0],
				in_time1,
				#int(line1[0].timestamp()), 
				#int(in_time1.timestamp()), 
				inactive1, user1,
				line1[1], in_time_line1, filename1, 
				count1
				]
				license_use1.append( templist1 )
				#print(templist1)
			elif line1[1].find(') DENIED: "') != -1:
				user1 = line1[1][line1[1].rfind('"')+2:line1[1].find(' ',line1[1].rfind('"')+2)].strip()    
				errorno1 = line1[1][line1[1].rfind('(')+1:line1[1].rfind('))')]  
				templist1 = [ feature1, int(line1[0].timestamp()), user1,
				errorno1, line1[1], filename1]
				denied_use1.append( templist1 )
	return license_use1, denied_use1

def sort1(sub1):
    sub1.sort(key = lambda x: x[0])
    return sub1

def feature_use_coord1(license_use1, feature1):
	# Returns the coordinates for plotting the graph via usage_plot function
	# From the license_use1 (OUT, IN) list, we use the OUT time as a x point and 
	# we look at previous x points and check if any of them has IN time earlier than the 
	# OUT time of the current x. If yes, we create a new x point for the IN time 
	# (which is earlier than OUT of current x) with y value equals to previous y value 
	# (running y total yprev1) minus 1.  Then we increment the running y total yprev1 
	# by 1 and assign it to the current y point.
	# We make a real copy of license_use1 (license_use2 = list2[:]) so that we 
	# can remove the line where IN is earlier than current OUT from the license_use2 
	# list so that the line will not be processed anymore.
	yprev1 = 0
	coord1 = []
	list2 = []
	# we remove all sublists from the list of lists except for feature1
	list2 = [ sublist2 for sublist2 in license_use1 if feature1 == sublist2[0] ]
	license_use2 = list2[:]
	# print(list2)
	# input("?")
	for line1 in list2:
		i = 0
		while True:
			line2 = license_use2[i]
			if line1[-1] == line2[-1]:
				break
			if line2[2] < line1[1]:
				yprev1 -= 1
				coord1.append([line2[2],yprev1])
				#feature_use2.pop
				#how to pop when we don't have index?
				license_use2.remove(line2)
			else:
				i += 1
		yprev1 += 1 
		coord1.append( [line1[1],yprev1] )
	# this for the last element in list2
	if list2:
		yprev1 -= 1
		coord1.append( [list2[-1][2],yprev1] )
	if coord1:
		coord1 = sort1(coord1)
	return coord1


def usage_graph1(coord1, feature1):
	# Plots the graph from the coord1 list
	# We use the "step" graph with where='post'
	# post: The Y-value remains constant to the right of the data point.  
	# For example the value y[i] remains constant between x[i] and x[i+1].
	# The single star * unpacks the sequence/collection into positional arguments
	# so zip(*coord1) returns all the x points to the tuple x, and 
	# all the y points to y1 tuple.
	x1, y1 = (zip(*coord1))
	x1 = list(x1)
	y1 = list(y1)
	plt.title(feature1 + " Usage from ")
	#plt.step(x1,y1,where='mid')
	plt.step(x1,y1,where='post')
	#plt.bar(x1,y1)plt.subplots_adjust(bottom=0.2)
	plt.xticks(rotation=25)
	ax=plt.gca()
	#xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
	xfmt = mdates.DateFormatter('%m-%d')
	ax.xaxis.set_major_formatter(xfmt)
	plt.show()







def process_file1(filename1, daemon1, tz1, features_sel1):
	# This is not being used now!
	in_list1 = create_in_list1(filename1)
	feature_use1 = []
	denied_use1 = []
	tz, dt_obj = detect_timezone_startdate1(filename1)
	with open(filename1, 'r') as f1:
		lines1 = f1.readlines()
	hrprev1 = 0
	for line1 in lines1:
		if line1.find('-SLOG@) Start-Date:') != -1 or line1.find('-SLOG@) Time:') != -1:
			if line1.find('-SLOG@) Start-Date:') != -1: 
				currentdate1 = line1[ line1.find('-SLOG@) Start-Date:') + 23:]
			elif line1.find('-SLOG@) Time:') != -1:
				currentdate1 = line1[ line1.find('-SLOG@) Time:') + 18:]
			if currentdate1.find(':') == -1:
				print("error at line 300: currentdate1.find(':') == -1")
			else:
				currentdate1 = currentdate1[:currentdate1.find(':')-3].strip()
			dt_obj = datetime.strptime(currentdate1 + ' 00:00:00', '%b %d %Y %H:%M:%S')
			origin_tz = zoneinfo.ZoneInfo(tz1)
			dt_obj = datetime( dt_obj.year, dt_obj.month, dt_obj.day, tzinfo=origin_tz)
		elif line1.find(':') != -1 and line1.find('(') != -1:
			t1 = line1[:line1.find('(')].strip().split(':')
			hr1 = t1[0]
			if hr1.isdigit():
				hr1 = int(hr1)
				if hr1 < 24:
					if hr1 < hrprev1:
						if dt_obj:
							dt_obj = dt_obj + timedelta(hours=24)
				hrprev1 = hr1
		elif line1.find(') OUT: ') != -1:
			feature1 = line1[ line1.find('"')+1:line1.rfind('"')].strip()
			if feature1 in features_sel1:
				time1 = line1[ 0:line1.find('(')-1]
				if dt_obj:
					t1 = time1.split(':')
					out_datetime1 = dt_obj + timedelta(seconds=int(t1[2]), minutes=int(t1[1]), hours=int(t1[0]))
					user1 = line1[line1.rfind('"')+2:].strip()
					#in_time1, inactive1, in_time_line1 = find_in_time1(lines1[i-1:],feature1,user1,out_in_list1)
					in_time1, inactive1, in_time_line1 = find_in_time1(in_list1,feature1,user1)
					if in_time1 is None:
						if (last_time1 - out_datetime1).total_seconds()/3600 < 24:  
							in_datetime1 = last_time1
						else:
							in_datetime1 = out_datetime1 + timedelta(hours=24)
					else:
						t1 = in_time1.split(':')
						in_datetime1 = dt_obj + timedelta(seconds=int(t1[2]), minutes=int(t1[1]), hours=int(t1[0]))
						if in_datetime1 < out_datetime1:
							in_datetime1 = dt_obj + timedelta(seconds=int(t1[2]), minutes=int(t1[1]), hours=int(t1[0])+24)
						else:
							in_datetime1 = dt_obj + timedelta(seconds=int(t1[2]), minutes=int(t1[1]), hours=int(t1[0]))

				else:
					print("Error: no currentdate1 dt_obj when we come to a OUT line")
					pass
		elif line1.find('(SW_D) DENIED: "') != -1:
			pass













#filenames1 = []
#filenames1 = get_filenames1()
filename1 = get_filename1()
# print(filename1)
features1 = []
#for filename1 in filenames1:
# print(filename1)
#exit()
features_sel1 = []
daemon1 = detect_daemon1(filename1)
# print(daemon1)
if daemon1:
	pass
	# print("Vendor daemon detected: ", daemon1)

tz1, dt_obj = detect_timezone_startdate1(filename1)
#print(tz1, dt_obj)
if tz1:
	pass
	# print("Timezone: ", tz1)
	# print(type(tz1))


# tz1 = timezone_win_iana_mapping1('Pacific Standard Time')
# print(tz1)
# print("type(tz1)", type(tz1))
# print("len(tz1", len(tz1))
# print("len('Pacific Standard Time')",len('Pacific Standard Time'))
# tz1 = timezone_win_iana_mapping1(tz1)
# print(tz1)
# tz1 = timezone_win_iana_mapping1('Pacific Daylight Time')
# print(tz1)

# print(detect_features1(filename1))
features1 = detect_features1(filename1)

while not features_sel1:
	features_sel1 = select_features1(features1)
# if not features_sel1:
# 	features_sel1 = select_features1(features1)
# print(features_sel1)

# print(get_lastdate1(filename1,tz1))

#line1 = '17:57:44 (ptc_d) IN: "PROE_EssentialsIIM" stan@MV121-Stan'
#print(get_time_in_line1(line1))

list1 = create_datetime_list1(filename1)

#print(list1)
# with open(filename1 + "out.txt", 'w') as f1:
# 	for line1 in list1:
# 		f1.write(line1[0].strftime('%m:%d:%Y %H:%M:%S %Z') + ', ' + line1[1])
license_use1 = []
denied_use1 = []
license_use1, denied_use1 = process_list1(list1, daemon1, features_sel1)

#print(feature_use1)
# print(denied_use1)
# print(len(denied_use1))
# for line1 in feature_use1:
# 	print(line1)

# in_list1 = create_in_list1(list1)
# print(len(in_list1))

coord1 = []
for feature1 in features_sel1:
	# print(feature1)
	coord1 = feature_use_coord1(license_use1,feature1)
	# print(coord1)
	if coord1:
		usage_graph1(coord1, feature1)

count1 = 0
for line1 in license_use1:
	if (line1[2] - line1[1]).total_seconds() / 3600 > 12:
		count1 += 1
print(count1)
