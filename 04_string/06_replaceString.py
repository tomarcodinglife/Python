letter = ''' 
Hi <|Name|>, you are selected in 
on <|Dated|>'''

print(letter.replace("<|Name|>", "Sujit Tomar").replace("<|Dated|>", "05 April 2026"))