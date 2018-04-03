def parse_name(full_name):
	name_p = full_name.replace('<','')
	name_p = name_p.split('>')
	s = '\n\t\t"name": {\n\t '
	s = s + '\t\t"first":' + '"' + name_p[0] + '",\n '
	s = s + '\t\t\t"middle":' + '"' + name_p[1] + '",\n ' 
	s = s + '\t\t\t"last":' + '"' + name_p[2] + '"' + '\n \t\t}' 

	return s

		

def parse_location(location_string):
	
	location_string_p = location_string.replace('<','')
	location_string_p = location_string_p.split('>')
	l = '\n\t"location" : {\n '
	l = l + '\t"name" :' + '"' + location_string_p[0] + '",\n '
	l = l + '\t"coords": { \n'
	if location_string_p[1] == '':
		
		l = l + ' \t"long" :' + '""' + ',\n '
		l = l+ '\t"lat" :' +  '""'
	else:
		l = l + ' \t"long" :' + location_string_p[1] + ',\n '
        	l = l+ '\t"lat" :' + location_string_p[2]	
	
	return l

def return_id(profile_id):
	profile_id = '\n ' + '\t"id":' + '"' + profile_id + '"'
	return profile_id


def return_image_id(image_id):
        image_id = '\n ' + '"imageId":' + '"' + image_id + '"'
        return image_id


def main():
	
	query = "profile|73241232|<Aamir><Hussain><Khan>|<Mumbai><<72.872075><19.075606>>|73241232.jpg**followers|54543342|<Anil><><Kapoor>|<Delhi><<23.23><12.07>>|54543342.jpg@@|12311334|<Amit><><Bansal>|<Bangalore><<><>>|12311334.jpg"
  
   	query=query.replace('**followers','')
	query=query.replace('@@','')
	query_array= query.split('|')
   	query_array.pop(0)
        ql= len(query_array)
        #print query_array
 	parse_string = '{'
	
	count = 0
	f_array = query_array[4:]
	print '======================================================================'
	print f_array[0]
	while(count < 5):
		if count == 0:
			parse_string = parse_string + return_id(query_array[0]) + ','
		if count == 1:
			parse_string = parse_string + parse_name(query_array[1]) + ','
		if count == 2:
			parse_string = parse_string +  parse_location(query_array[2]) + '\n\t}\n} ,'
		if count == 3:
			parse_string = parse_string + return_image_id(query_array[3]) + ',\n'
		if count == 4:
			parse_string = parse_string + '"followers":[ '		
			fl = len(f_array)
			print '*****************'
			print fl
			fl = fl / 4
			print fl
			count_internal = 0
			i_pass = 0
			while(count_internal < fl):
				parse_string = parse_string + '{' +return_id(f_array[i_pass+0]) + ','
				parse_string = parse_string + return_image_id(f_array[i_pass+3]) + ',\n'		
				parse_string = parse_string + parse_name(f_array[i_pass+1]) + ','
				parse_string = parse_string + parse_location(f_array[i_pass+2]) + '\n\t}}\n},\n'
 				i_pass = i_pass + 4
				count_internal = count_internal +1
		count = count + 1			
	p_len = len(parse_string)
	parse_string=parse_string[:p_len-2]
	parse_string = parse_string + ']}'
	print parse_string	
if __name__== "__main__":
  main()


#c=parse_name('<Aamir><Hussain><Khan>')
#d=parse_location('<Mumbai><<72.872075><19.075606>>')
#e = return_id('123213123')
#f = return_image_id('1312321.jpg')
#print c + d + e + f
