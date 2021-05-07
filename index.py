

#slicing strings\

msg ='Bre is cool'
# print(msg[0])
# print(msg[2:10])

# String exercise 

str = 'Welcome to Python 101: Strings'
str1=str[18]+' '+str[:8]+str[25:29]+str[7:11]+str[8]+str[12]+str[2]+str[1]+str[-5]



print(str1.title())
print(str1[::-1].title())

# Multiline Strings
sentence="""Hi my name is
Bre and I love Luke so much. And
also Archie!"""

print(sentence)
print(sentence.find('Bre'))
print(msg.replace('Bre', 'Luke'))


print('Bre' not in msg)

## String formatting 
name='bre'
color='PINK'
str2= '['+name+'] loves the color ' + color + '!'
print(str2)

str2=f'[{name.capitalize()}] loves the color {color.lower()}!'
print(str2)