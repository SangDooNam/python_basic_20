"""Your challenge consists of writing 2 modules:

encrypt.py, which takes two inputs (a plain text and a key) and returns the ciphertext corresponding to the given plain text.

decrypt.py, that takes two inputs (a ciphertext and a key) and returns the plain text corresponding to the given ciphertext."""



# plaintxt = input("Enter any text or password you want to encrypt: ")
# shift = int(input("Insert the number of positions by which you'd like to shift the characters for encryption.: "))

# shifted_txt = ""

# for i in plaintxt:
    
#     position = ord(i)
    
#     shifted = (ord(i) + shift - ord('a')) % 26 + ord('a')

#     shifted_txt += chr(shifted)

# print(shifted_txt)

# decrypted_txt = ""

# for i in shifted_txt:
    
#     position = ord(i)
    
#     decrypted = (ord(i) - shift - ord('a')) % 26 + ord('a')
    
#     decrypted_txt += chr(decrypted)
    
# print(decrypted_txt)



def encrypt(text, shift):
    encrypted_text = ""
    for element in text:
        if element.isalpha():
            
            element_upper = element.isupper()
            
            element = element.lower()
            
            position = ord(element)
            
            position = (position + shift - ord('a')) % 26 + ord('a')
            
            new_element = chr(position)
            
            if element_upper:
                new_element = new_element.upper()
                
            encrypted_text += new_element
            
        else:
            encrypted_text += element
            
    return encrypted_text
    
def decrypt(encrypted_text, shift):
    
    return encrypt(encrypted_text, -shift)


while True:
    
    prompt = input("Do you want to encrypt or decrypt ((e):encrypt /(d):decrypt /(q)quit): ")
    
    if prompt == "q":
        break
    
    if prompt not in ["e", "d" ]:
        
        print("Invalid choice. Please try again.")
        
        continue
    
    text = input("Enter any text you want to encrypt or decrypt :")
    shift = input("Enter a shift value : ")
    
    try: 
        shift = int(shift)
        
    except ValueError:
        
        print('Please enter an integer.')
        
    if prompt == "e":
        
        result = encrypt(text, shift)
        
        print (f'The encrypted text is {result}')
        
    if prompt == "d":
        
        result = decrypt(text, shift)
        
        print (f'The decrypted text is {result}')
            
            
    