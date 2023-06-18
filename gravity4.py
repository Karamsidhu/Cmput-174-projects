import string

alphabet = list(string.ascii_letters)
alphabet_l = list(string.ascii_lowercase)
alphabet_u = list(string.ascii_uppercase) 

def decrypt_caesar(text: str, shift: int) -> str:
    """
    Decipher a text (Caesar cipher).
    """
    
    new = []    
    data = []
    
    for letter in text:         #was not appending space before. also use .split!
        if letter == " ":
            data.append(letter)
        else:
            data.append(letter)     
            
            
            
# 
# Decrypter
#

    for letter in data:
        if letter not in alphabet: #special characters
            new.append(letter)
            
        elif letter in alphabet_u: 
            for text in range(len(alphabet_u)): #loop if in upper case.
                if letter == alphabet_u[text]:
                    var = text
                    new.append(alphabet_u[(int(var)-int(shift))%len(alphabet_u)]) # (shift % alphabet) and append
                    
        else:
            for text in range(len(alphabet_l)): #same thing for lower case.
                if letter == alphabet_l[text]:
                    var = text
                    new.append(alphabet_l[(int(var)-int(shift))%len(alphabet_l)])            
    
    final = "" 
    for letter in new:
        final = final + str(letter)  # connactonate list to a string
            
    return final


def decrypt_atbash(text: str) -> str:
    """
    Decipher a text (Atbash cipher).
    """
    
    new = []
    data = []

    for letter in text:
        if letter == " ":
            data.append(letter)
        else:
            data.append(letter)       
            
#            
# Decrypter           
#           


    for letter in data:
        if letter not in alphabet: # special character
            new.append(letter)
            
        else:
            for text in range(len(alphabet_u)): # case for upper
                if letter == alphabet_u[text]:
                    new.append(alphabet_u[(text*-1)-1])
                    
                elif letter == alphabet_l[text]: # case for lower ( *-1 then -1 for range.)
                    new.append(alphabet_l[(text*-1)-1])
                
    
    final = ""
    for letter in new:
        final = final + str(letter)                 
    
    return final


def decrypt_a1z26(text: str) -> str:
    """
    Decipher a text (A1Z26 cipher).
    """
    end = []
    new = []
    
    domain = []
    x = 0
    while x < 26: # can also do range(1,26)
        x += 1
        domain.append(str(x))
        
        

    if text[len(text)-1:len(text)] in domain:    #if there is a ending number [split whole]
        sentence_length = len(text)
    else:
        sentence_length = -1                     #var is len(text) - 1 now.
        last_store = text[len(text)-1:len(text)] #else split all cep't last
    
    
    false = text[0:sentence_length].split(" ") 
    for word in false:
        end.append(word.split("-"))
    
    
    
    #
    # Decrypter
    #
        
    for seqeunce in end:
        new.append(" ") #space between each word.
        for word in seqeunce:
            if word[0:1] in alphabet: # case for words - just append
                new.append(word)
                
            elif word[0:1] in domain: # in [1:26]
                new.append(alphabet_u[int(word)-1]) # - 1 for correct index range @ alphabet_u
    
    
    final = ""
    for letter in new[1:len(new)]: # start at 1, because a space is appened.
        final = final + str(letter)
      
    if sentence_length == -1: # if there is punctuation
        final = final + last_store
    
    return final


def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    shift = input("Enter how many to shift: ") 
    
    ceaser = decrypt_caesar(text, shift)
    atbash = decrypt_atbash(text)
    A1Z26 = decrypt_a1z26(text)
    
    print("Ceaser cipher:", ceaser, end="\n")
    print("Atbash cipher:", atbash, end="\n")
    
    print("combined: 1) Caesar; 2) Atbash cipher:", decrypt_atbash(ceaser), end="\n")
    print("combined: 1) Atbash; 2) Ceasar cipher:", decrypt_caesar(atbash, shift), end="\n")
    
    print("A1Z26 cipher:", A1Z26, end="\n")
    
    print("combined: 1) A1Z26; 2) Ceaser cipher:", decrypt_caesar(A1Z26, shift), end="\n")
    print("combined: 1) A1Z26; 2) Ceaser cipher:", decrypt_atbash(A1Z26), end="\n")
    
    print("combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher:", decrypt_caesar(decrypt_atbash(A1Z26), shift), end="\n")
    print("combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher:", decrypt_atbash(decrypt_caesar(A1Z26, shift)), end="\n")
    
    


main()