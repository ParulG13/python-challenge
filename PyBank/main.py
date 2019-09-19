import csv
import os

# input file
file_path = os.path.join("budget_data.csv")

#output file
output_file_path = "budget_data_analysis.txt"

#open file in write mode
outFile = open(output_file_path, "w+")

# function to write output in console and file
def printOutput(vLine):
  print(vLine)
  outFile.write(vLine)
  outFile.write("\n")

# read file
with open(file_path, 'r') as inputFile:
    input_read = csv.reader(inputFile, delimiter=',')
    # ignore the header
    csv_header = next(input_read)
    # print(f"CSV Header: {csv_header}")
    totalMonths = 0
    total = 0
    previous_value = 0
    change_d = {}

    #iterate through the given data row by row
    for row in input_read:
        # number of rows is total months
        totalMonths = totalMonths + 1
        #sum of all profit/loss is the total
        total = int(row[1]) + total

        current_value = int(row[1])
        # calculate each profit/loss change
        change_value = current_value - previous_value

        #dict will store change value and corresponding date
        change_d[change_value] = row[0]
        previous_value = current_value

    #get largest key for greatest increase
    greatest_inc = max(change_d.keys())
    greatest_inc_date = change_d.get(greatest_inc)
    #get smallest key for greatest decrease
    greatest_dec = min(change_d.keys())
    greatest_dec_date = change_d.get(greatest_dec)

    #to calculate total change sum all the changes
    #but not the first one, so remove the [0] key from dict
    changed_l = list(change_d.keys())
    del changed_l[0]
    average_change = round(sum(changed_l)/len(changed_l),2)



# display output
printOutput("Financial Analysis")
printOutput("----------------------------")
printOutput("Total Months: {}".format(totalMonths))
printOutput("Total: {}".format(total))
printOutput("Average  Change: ${}".format(average_change))
printOutput("Greatest Increase in Profits: {} (${})".format(greatest_inc_date, greatest_inc))
printOutput("Greatest Decrease in Profits: {} (${})".format(greatest_dec_date, greatest_dec))