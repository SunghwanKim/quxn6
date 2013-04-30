sample_str = "[Thu Oct 04 12:11:22 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico"

def get_error(input_str) :
	cnt_len = 1
	path_and_errname = []
	beg_of_pth = 0
	beg_of_err = 0

	if (input_str.find("[error]",0,len(input_str))):
		## get startpoint of path in str
		for find_pth_beg in input_str[::-1] :		
			if(find_pth_beg == ':')	:
				break
			cnt_len = cnt_len +1
		beg_of_pth = len(input_str)-cnt_len
		
		## save the path
		path_and_errname.append(input_str[beg_of_pth+2:])
		
		## get startpoint of error name in str	
		for find_err_beg in input_str[beg_of_pth::-1]	:# print input_str[:beg_of_pth].rfind("]",1)	
			if(find_err_beg == "]")	:
				break
			cnt_len = cnt_len +1
		beg_of_err = len(input_str)-cnt_len

		## save the error name
		path_and_errname.append(input_str[beg_of_err+2:beg_of_pth])
	
	return path_and_errname

print get_error(sample_str)