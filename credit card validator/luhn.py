card_no = "5610591081018250"
odd_sum = 0
even_sum = 0
double_list = []
number = list(card_no)

for (idx, val) in enumerate(number):
    if idx % 2: # this is an odd number
        odd_sum += int(val)
    else:
        double_list.append(int(val) * 2)

# converting double list into a string
double_string = ""
for x in double_list:
    double_string += str(x)

# converting the string back into a list
double_list = list(double_string)

for x in double_list:
    even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('Valid card!')
else: 
    print('Invalid card')
