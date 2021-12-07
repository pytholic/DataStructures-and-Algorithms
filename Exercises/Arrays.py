
list_exp = [['January', '2200'],
['February', '2350'], 
['March', '2600'], 
['April', '2130'], 
['May', '2190']]

#######################################################

feb_exp = int(list_exp[1][1])
jan_exp = int(list_exp[0][1])
diff = feb_exp - jan_exp
print(f"Extra amount is {diff}$")

#######################################################


#######################################################

total_1 = int(list_exp[0][1]) + int(list_exp[1][1]) + int(list_exp[2][1])
print(f"Total for first three month is {total_1}$")

int_list = [int(i[1]) for i in list_exp[0:len(list_exp)]]
total_2 = sum(int_list[0:3])
print(f"Total for first three month is {total_2}$")

#######################################################


#######################################################

i = 2000
if i in int_list:
    #print(int_list.index(i))
    print(f"You spend 2000$ in {list_exp[int_list.index(i)][0]}.")
else:
    print("You did not sepnd 2000$ in any month.")

#######################################################


#######################################################

june_exp = 1980
list_exp.append(["June", f"{june_exp}"])
print(list_exp)

#######################################################


#######################################################

refund = 200
corrected_amount = int(list_exp[3][1]) + refund
#print(corrected_amount)
list_exp[3][1] = corrected_amount
print(list_exp)

#######################################################
