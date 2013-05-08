from __future__ import print_function
import re

def get_line(input_str) :
	path_and_errname = []
	beg_of_pth = 0
	beg_of_err = 0

	if ("[error]" in input_str)	:
		## get startpoint of path in string
		beg_of_pth = input_str.rfind(": /")
		
		## save the path
		path_and_errname.append(input_str[beg_of_pth+2:])
		
		## get startpoint of error name in string
		beg_of_err = input_str[:beg_of_pth].rfind("]")	

		## save the error name
		path_and_errname.append(input_str[beg_of_err+2:beg_of_pth])

		return path_and_errname

# line = "[Mon Oct 08 18:18:57 2012] [error] [client 127.0.0.1] File does not exist: /Library/WebServer/Documents/testa.jpg, referer: http://88.191.128.200/lb_compiled_js.html"


def get_report()	:
	## get report from log file
	## return list1

	## define data type and function
	## list1[dict1, dict2]
	## dict1{key:event name(string), value : count of events(int)}
	## dict2{key:event name(string), value : list2[path1, path2....(string) ]}
	

	summary_report = dict()
	detail_report = dict()
	report = [summary_report, detail_report]

	try :
		log_file = open('error_log')

		for line in log_file:
			tmp = get_line(line)
			
			if(tmp != None)	:	
				path = tmp[0]
				eventname = tmp[1]

				if(eventname in detail_report)	:
					# path overap check
					if(path not in detail_report[eventname]) :						
						detail_report[eventname].append(path) 		# add eventname
					summary_report[eventname] = summary_report[eventname] + 1 	# event counter
					
				else	:
					detail_report[eventname] = [path]				# init key and add eventname
					summary_report[eventname] = 1 						# init count
		return report	

	except IOError:
		print ("File IO Error")
	#	throwError(102,detail)

def print_report(log):
	print ("[summary report]\n")
	for counter in log[0] :
		print (counter, ":", log[0][counter])

	print ("\n\n[detail report]")
	for path in log[1]	:
		print ("\n", path)
		for each_path in log[1][path]	:
			tmp_log = each_path.strip("\n")
			tmp_re = re.search(r'\w+\.(jpg|png|gif)',tmp_log)
			if(tmp_re == None):
				print(tmp_log)


def file_report(log):
	f = open('./rep.txt', 'w')

	f.write("[summary report]\n")
	for counter in log[0] :
		f.write (counter+ ":" + str(log[0][counter]) +"\n")

	f.write("\n\n[detail report]")
	for path in log[1]	:
		f.write("\n" + path)
		for each_path in log[1][path]	:
			tmp_log = each_path
			tmp_re = re.search(r'\w+.(jpg|gif|png)',tmp_log)
			if(tmp_re == None):
				f.write(tmp_log)
	f.close

report = get_report()
print_report(report)
file_report(report)
