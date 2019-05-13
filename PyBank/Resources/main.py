import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
  
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    previous = None

    for row in csvreader:
        print(row)
        
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
    
        revenue_change = int(row[1]) - prev_revenue
       
        prev_revenue = int(row[1])
    
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

        revenue_changes.append(int(row[1]))

    
    revenue_avg = sum(revenue_changes) / len(revenue_changes)


print ("Financia Analysis")
print ("----------------------------")
print (f"Total Months: {int(total_months)}")
print (f"Total: {int(total_revenue)}")
print (f"Average Change: {int(total_revenue / (total_months - 1))}")
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")




