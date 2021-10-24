import os
import csv

# Setting path for the csv budget data
pybankcsv  = os.path.join("Resources", "budget_data.csv")

#Let's create lists in order to store data

profit = []
monthly_changes = []
date = []

#Placing required variables

count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#Let's open the csv budget data file

with open(pybankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Let's use count to count the number of months in the dataset
        count = count +1

        #It will be needed when collecting the greatest increase and decrease in profits
        date.append(row[0])

        #Let's append the profit information and calculate the total profit
        profit.append(row[1])
        total_profit = total_profit - int(row[1])

        #Let's calculate the average change in profits from month to month followed by calculating the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Let's store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #Let's calculate the average change in profits
        average_change_profits = (total_change_profits/count)

        #Let's find the max and in change in profits and corresponding dates to these changes
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    print("----------------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
    print("----------------------------------------------------------------")


with open('financial_analysis.txt', 'w') as text:
    text.write("--------------------------------------------------------------\n")
    text.write(" Financial Analysis" + "\n")
    text.write("---------------------------------------------------------------\n\n")
    text.write("     Total Months: " + str(count) + "\n")
    text.write("     Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("     Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("     Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("     Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.wrtie("--------------------------------------------------------------\n")