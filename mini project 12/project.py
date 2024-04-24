import random
import array

max_len = 12

digits = ['0','1','2','3','4','5','6','7','8','9']

Lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z']

Upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                'P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',
            ':','"','<','>','?','/','[',']','~','`','\\','\'',';','=']


combined_list = digits+Lower_case+Upper_case+symbols

rand_digits = random.choice(digits)
rand_lower = random.choice(Lower_case)
rand_upper = random.choice(Upper_case)
rand_symbols = random.choice(symbols)


tmp = rand_digits + rand_lower + rand_upper + rand_symbols

for i in range(max_len-4):
    tmp = tmp + random.choice(combined_list)
    
    tmp_list = array.array('u',tmp)
    random.shuffle(tmp_list)
    
password =""
for x in tmp_list:
    password = password +x
    
print(password)