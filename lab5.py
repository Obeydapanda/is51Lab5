

"""
The program is trying to translate a sentence captured as user input
First read the text.txt file
Use each line in the text.txt file to create a list of strings
Dictionary the list
Read file into memory, then close the file

create a function for translating which involved splitting 
the uer input into an array of strings
 once we have the array of strings representing the user's input
 we loop through each wood and find the key matching the word and return
 back the value tied back to the dictionnary

 print out translated sentence 
"""
"""
main():
    set dictionary = translate()
    translate(sentence, dictionary)

translate():
    words = for each of the word in the sentence
    for each words, translate the word
    print tranlated sentence to the user


create_dictionary():
    read in text.txt
    create list = each line in file
    close
    create a dict off the list
    return the dict

main()
"""

def main():
    sentence = "enjoy the execellent band tonight"
    dictionary = create_dictionary("text.txt")
    translate(sentence,dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()

    # print("words", words)
    translation = {}
    for word in words: # "tonight,2nite"
        [k, v] = word.split(",")
        translation[k] = v
    print (translation)
    return translation
 
def translate(sentence, dictionary):
     print ("From translate", sentence)
     words = sentence.split() # ["enjoy" , "the" "excellent", "band" , "tonight"]
     for word in words:
        print(dictionary.get(word,word), " ", end ="")

main()
