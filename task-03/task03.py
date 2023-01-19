# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
def check_balance(mystr):
    mylist = []
    isbalanced='yes'
    for item in mystr:
        if item in open_list:
            mylist.append(item)
        elif item in close_list:
            if len(mylist) == 0 :
                 isbalanced='No'
                 return isbalanced
            if open_list[close_list.index(item)] == mylist[len(mylist)-1]:
                mylist.pop()
            else:
                isbalanced='No'
                return isbalanced
    if len(mylist) != 0:
        isbalanced='No'
        return isbalanced
    return isbalanced

string = input()
print(check_balance(string))





