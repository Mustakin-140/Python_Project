import  random
import  array

#maximum length of password needed
#this can be changed to suit your password length
MAX_LEN = 12

#declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation

DIGITS = ['0','1','2','3','4','5','6','7','8','9']
LOWERCASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPERCASE = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
#combines all the characters arrays to form one array
COMBINED_LIST = DIGITS + LOWERCASE + UPPERCASE + SYMBOLS

#randomly select at least one character from character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE)
rand_lower = random.choice(LOWERCASE)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
# now that we are sure we have at least one character from each
# set of characters, we fill with the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

# convert temporary password into array and shuffle to
# prevent it from having a consistent pattern
# where the beginning of the password is predictable
    temp_pass_list = array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
    password = password + x

print(password)