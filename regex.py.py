import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*5646
800-555-4321
900-555-4321
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
bat
cat
oat
pat
'''
# \d\d\d.\d\d\d.\d\d\d\d for phone numbers
# \d\d\d[-.]\d\d\d[-.]\d\d\d for phone numbers precise
# [89]00[-.]\d\d\d[-.]\d\d\d for phone numbers startinf from 8 and 9
# [a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net) for matching emails
# M(r|s|rs)\.?\s[a-zA-Z]\w* for names
# https?://(www\.)?\w+\.(com|gov)
sentence = 'Start a sentence and then bring it to an end'

emails='''
charlesharris@bogusemail.com
charle.sharris@bogusemail.edu
charlesharris123@se-mail.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#for match in matches:
 #   print(match)
    
pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')


#with open('data.txt','r',encoding='utf-8') as f:
    #contents = f.read()

matches = pattern.finditer(urls)

for match in matches:
    print(match)
    
