#*************************encode*************************
#Adds 0 at first of a string to make it's length 8 chars(returns string)
def change_length(text):
    lengthDiff = 8 - len(text)
    for i in range(0, lengthDiff):
        text = "0" + text
    return text

#Converts a string to list of ascii codes(returns list of strings)
def str_to_ascii(text):
    temp = ''.join(str(ord(c)) + " " for c in text)
    return temp.split(" ")[0:-1]

#Converts a list of base10 numbers(ascii codes) to a base2 string
def to_base_2(text):
    temp = ""
    for char in text:
        temp += change_length(str(bin(int(char))[2:]))
    return temp

#Converts a string to base2 string
def text_to_base_2(text):
    return to_base_2(str_to_ascii(text))

#Gets a key and encodes plain text
def encode(text, key):
    temp = ""
    text = text_to_base_2(text)
    for i in range(0, len(text)):
        #print(str(bool(int(text[i]))) + ", " + str(bool(int(key[i]))))
        #print(bool(text[i]) != bool(key[i]))
        temp += str(int(bool(int(text[i])) != bool(int(key[i]))))
    return temp

#*************************decode*************************
#Converts a base2 string to list of base10 strings(ascii codes)
def to_base_10(text):
    temp = []
    for i in range(0, len(text)-7, 8):
        temp.append(str(int(text[i:i+8], 2)))
    return temp

#Converts a list of string ascii codes to text(returns string)
def ascii_to_text(text):
    temp = ""
    for code in text:
        temp += chr(int(code))
    return temp

#Converts base2 string to string
def base_10_to_text(text):
    return ascii_to_text(to_base_10(text))    

#Gets a key and decodes cipher
def decode(code, key):
    temp = ""
    for i in range(0, len(code)):
        temp += str(int(bool(int(code[i])) != bool(int(key[i]))))
    temp = base_10_to_text(temp)
    return temp

#**************************main**************************
def main():
    flag = int(input("Enter 1 to encode and 2 to decode:"))
    if(flag == 1):
        text = input("Enter plain text:")
        key = input("Enter " + str(len(text_to_base_2(text))) + " base2 digits as key:")
        print("cipher : " + encode(text, key))
    elif(flag == 2):
        text = input("Enter cipher:")
        key = input("Enter " + str(len(text)) + " base2 digits as key:")
        print("plain text : " + decode(text, key))

if __name__ == '__main__' :
    main()