print("""This script is for coding and decoding messages.
This cypher has an offset of 10 which means we switch all the letters by 10.
"oui y husuylut yj!" is the first one we will decode""" )


alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
# message = "oui y husuylut yj!"
# translated_message = ""
# for letter in message:
#     if not letter in punctuation:
#         letter_value = alphabet.find(letter)
#         translated_message += alphabet[(letter_value + 10) % 26]
#     else:
#         translated_message += letter
# print("Result is: " + translated_message)

# print("""Now we code the message "yes I received it!" with the same offset""")
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# punctuation = ".,?'! "
# message = "yes i received it!"
# code_message = ""

# for letter in message:
#     if not letter in punctuation:
#         letter_value = alphabet.find(letter)
#         code_message += alphabet[(letter_value -10) % 26]
#     else:
#         code_message += letter
# print("Result is: " + code_message)


def decoder(message, offset):
    translated_message = ""
    
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
print("Result is: " + decoder("oui y husuylut yj!", 10))


print("""Now we code the message "yes I received it!" with the same offset""")

def coder(message, offset):
    coded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            coded_message += alphabet[(letter_value - offset) % 26]
        else:
            coded_message += letter
    return coded_message    
print("Result is: " +  coder("yes i received it!", 10))

# print("This is a function that decodes with any offset in case we do not know it")
# message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# for number in range(1, 26):
#     print("offset"+str(number))
#     print("\t"+ decoder(message, number)+"\n")

print("""This function decodes a message when the Cypher is a keyword.
Here we use KW friends to decode "dfc aruw fsti gr vjtwhr wznj?""")
def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    # print(keyword_final)
    return translated_message
    

message = "dfc aruw fsti gr vjtwhr wznj?"
keyword = "friends"

print("Result is: " + vigenere_decoder(message, keyword))
    