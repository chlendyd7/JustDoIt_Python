url = "http://naver.com"
my_str = url.replace("http://","")
my_str=my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
 
