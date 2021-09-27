def caesar(text, shift):
    #text = input("Enter the password: ")
    #shift = int(input("Input the shift(4 is funny): "))
    result = ""
    for i in range(len(text)): #transverses the plain text
        char = text[i]

    #Encrypt the uppercase text
        if(char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 25)
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    return result

#caesar("Zolani", 4)