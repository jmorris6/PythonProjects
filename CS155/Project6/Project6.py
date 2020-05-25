import string
def CheckWord(password):
    rule1, rule2, rule3, rule4 = True, True, True, True
    if(len(password) < 10):
        rule1 == False
    uppercase, lowercase, punctuation, numerical = 0, 0, 0, 0
    for character in password:
        if(character.isupper() == True):
            uppercase += 1
        elif(character.islower() == True):
            lowercase += 1
        elif(character.isnumeric() == True):
            numerical += 1
        else:
            for punct in string.punctuation:
                if punct == character:
                    punctuation += 1
                    break
    if(uppercase < 1) or (lowercase < 1):
        rule2 == False
    if punctuation < 2:
        rule3 = False
    if numerical < 2:
        rule4 = False
    return rule1, rule2, rule3, rule4
def RecordResult(password, rule1, rule2, rule3, rule4):
    with open("P6out.txt", "a+") as results:
        results.write("****************\n")
        results.write(password + "\n")
        if rule1 == False:
            results.write("\nrule 1 failed: must have > 10 characters")
        if rule2 == False:
            results.write("\nrule 2 failed: must have a mix of upper and lower case letters")
        if rule3 == False:
            results.write("\nrule 3 failed: must have at least two punctuation characters")
        if rule4 == False:
            results.write("\nrule 4 failed: must have at least two numeric chartacters")
        if ((rule1 == True) and (rule2 == True) and (rule3 == True) and (rule4 == True)):
            results.write("\nMeets all requirements")
        results.write("\n****************")

with open("P6in.txt", "r") as passwords:
    password = passwords.readline()
    while(password != ""):
        password = password[:-1]
        rule1, rule2, rule3, rule4 = CheckWord(password)
        RecordResult(password, rule1, rule2, rule3, rule4)
        password = passwords.readline()
