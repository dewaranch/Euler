"""Euler17
If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?
"""

"""Strategy: get three things.
1. all possible words.
2. lengths of words.
3. # of times each word occurs.
then, multiply!
"""
#one thing you can't get around is writing out length of words.
def Euler14():

    #holder for letters
    total_letters=0
    #number lengths
    ones=       [0,3,3,5,4,4,3,5,5,4]
    teens=      [3,6,6,8,8,7,7,9,8,8]
    tens=       [0,0,6,6,5,5,5,7,6,6]
    hundred=7
    thousand=8
    len_and=3
    
    for i in range(1,1001):
        ist=str(i)
        one_p=999
        ten_p=999
        hun_p=999

        #doing exception for 1000
        if len(ist)==4:
            total_letters=total_letters+thousand + len_and

        #getting places
        one_p= int(ist[-1])
        if i >9:
            ten_p=int(ist[-2])
        if i>99:
            hun_p=int(ist[-3])

        #teen exception.
        if ten_p==1:
            total_letters=total_letters + teens[one_p]
            if hun_p!=999:
                total_letters=total_letters + hundred + ones[hun_p] + len_and
        else:
            if ten_p==999:#ones
                total_letters=total_letters + ones[one_p]
            if hun_p==999 and ten_p !=999:#tens
                total_letters=total_letters + tens[ten_p] + ones[one_p]
            if hun_p != 999 and len(ist)!=4:#hundreds (exclude 1000)
                if one_p==0 and ten_p==0: #exception with no and.
                    total_letters=total_letters + ones[hun_p] + tens[ten_p] + ones[one_p] + hundred
                else:
                    total_letters=total_letters + ones[hun_p] + tens[ten_p] + ones[one_p] + hundred + len_and
        
    print(total_letters)
Euler14()
