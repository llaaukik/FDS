


sentence = input("Enter string: ")

longest = max(sentence.split(), key=len) #key custom function that transforms each element before comparison.

print("Longest word is: ", longest)
print("And its length is: ", len(longest))


# b) To determines the frequency of occurrence of particular character in the string

# using naive method to get count of each element in string
all_freq = {}

for i in sentence:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in sentence is :\n "
      + str(all_freq))




# c) To check whether given string is palindrome or not

text=input("enter string:")
print("Given string is "+text)
rev=reversed(text)
if list(text)==list(rev):
    print("its a palindrome")
else:
    print("its not a palindrome")



# d) To display index of first appearance of the substring


sub_str1 =str(input("Enter string:"))
print("index of first appearance of the substring "+sub_str1+" is")
print(sentence.find(sub_str1))

#check if Substring found or not.
if(sentence.find(sub_str1)==-1):
    print("Substring Not Found")
else:
    print("Substring found")




#  e) To count the occurrences of each word in a given string.

print("Following are the count the frequency of each word in a given string")
def freq(sentence):
    # break the string into list of words
    sentence = sentence.split() # splite divide a string into a list of substring
    str2 = []

    # loop till string values present in list str
    for i in sentence:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    for i in range(0, len(str2)):
        # count the frequency of each word(present in str2) in sentence and print
        print('count of frequency', str2[i], 'is :', sentence.count(str2[i]))


#OUTPUT
#PS C:\Users\Aditya\OneDrive\Desktop\oop> python -u "c:\Users\Aditya\OneDrive\Desktop\26-Aaditya kulkarni\practical2.py"
#Enter string: Welcome to department of computer engineering
#Longest word is:  engineering
#And its length is:  11
#Count of all characters in sentence is :
# {'W': 1, 'e': 8, 'l': 1, 'c': 2, 'o': 4, 'm': 3, ' ': 5, 't': 4, 'd': 1, 'p': 2, 'a': 1, 'r': 3, 'n': 4, 'f': 1, 'u': 1, 'g': 2, 'i': 2}
#enter string:madam
#Given string is madam
#its a palindrome
#Enter string:come
#index of first appearance of the substring come is
#3
#Substring found
#Following are the count the frequency of each word in a given string
