letter = ''' 
Hi <|Name|>, you are selected in 
on <|Dated|>'''

# print(letter.replace("<|Name|>", "Sujit Tomar").replace("<|Dated|>", "05 April 2026"))

# Hi Sujit Tomar, you are selected in on 05 April 2026

letter1 = '''
Hi <|Name|>, You are selected in Google compnay on behalf of 
<|Date|> Interview. 
'''

print(letter1.replace("<|Name|>", "Sujit Tomar").replace("<|Date|>", "20 Jan 2026"))
print(letter1.replace("<|Name|>", "Sujit").replace("<|Date|>", "05 April 2026"))

Narration = '''Hi my self <|Name|>, i am from <|Address|> \n Thank You.'''
print(Narration.replace("<|Name|>", "Sujit Kumar Singh").replace("<|Address|>", "Bihar"))
