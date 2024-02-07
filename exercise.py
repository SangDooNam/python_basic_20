

text = input('Enter any word or text: ')


reserved = [None] * len(text)


for index, element in enumerate(text):
    
    reserved[-(index + 1)] = element
    

if element.isupper():
    
    reserved[-(index +1 )] = reserved[-(index +1 )].upper()
    
else:
    reserved[-(index +1 )] = reserved[-(index +1 )].lower()
    
reserved = "".join(reserved)

print(reserved)