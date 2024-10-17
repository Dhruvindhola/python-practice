print("Printing current and previous number and their sum is a range(15)")
previous_num = 0

for i in range(1, 15):
    a_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum: ",a_sum)
    
    previous_num = i