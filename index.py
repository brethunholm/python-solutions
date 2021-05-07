

#slicing strings\

msg ='Bre is cool'
# print(msg[0])
# print(msg[2:10])

# String exercise 

str = 'Welcome to Python 101: Strings'
str1=str[18]+' '+str[:8]+str[25:29]+str[7:11]+str[8]+str[12]+str[2]+str[1]+str[-5]



# print(str1.title())
# print(str1[::-1].title())

# Multiline Strings
sentence="""Hi my name is
Bre and I love Luke so much. And
also Archie!"""

# print(sentence)
# print(sentence.find('Bre'))
# print(msg.replace('Bre', 'Luke'))


# print('Bre' not in msg)

## String formatting 
name='bre'
color='PINK'
str2= '['+name+'] loves the color ' + color + '!'
# print(str2)

str2=f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(str2)


# User Input

name= input('What is your name?:')
age=input('What is your age?:')
# print('Good Morning ' + name + '! You are '+ age +' years old.')


# Calculator 

num1= input('Enter a digit: ')
num2= input('Enter a second number:')
answer= float(num1)+float(num2)
# print(answer)

# User Input - Exercise
# Distance converter km to miles 

name=input('Please enter your name:')
km =input('Enter the number of kilometers you wish to convert to miles: ')
miles= float(km)/1.609
# print(f'Hi {name.title()}! {km}km is equivalent to  {round(miles, 1)} miles')

# Lists
groceries=['eggs','milk','cheese','lettuce']


# find length len(groceries)
# index of specific item groceries.index('item')

groceries.sort(reverse=True)


nums= [1,2,6,8,24,57,33]
# print(min(nums))
# print(max(nums))


# to add to list 
groceries.append('fruit')
groceries.insert(1,'bread')
groceries[3]='broccoli'

# to remove item from list
groceries.remove('bread')
# remove but keep in memory use .pop
# clear list groceries.clear()

# remove completely ie not just an empty list use -> del groceries 

# making a copy of a list
new_groceries = groceries[:]
# or
new_new_groceries = list(groceries)
# print(groceries)
# print(new_new_groceries)

# List exercise Lemonade Stand

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []


new_day= input('Enter number of lemonades sold for new day: ')
sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2
best_day = max(sales) * 1.5
worst_day= min(sales) * 1.5
total = sum(sales)

# print('best', best_day)
# print('worst', worst_day)
# print('total', total)

# Splitting and Joint 
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print('Welcome to Python 101: Split and Join')

print(msg.split())