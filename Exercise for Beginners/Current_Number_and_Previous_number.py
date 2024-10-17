print("Printing current and previous number and their sum is a range(15)")
previous_num = 0
# Loop from 1 to 20
for i in range(1, 20):
    a_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum: ",a_sum)
    # modify previous number 
    # set it to the current number
    previous_num = i