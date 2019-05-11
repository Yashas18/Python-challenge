import os
import csv

# using relative path
budget_data = "Resources/budget_data.csv"

# reading the csv and converting the csv into a list
with open(budget_data, newline="") as csvfile:
    budgetDataCSV = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    budgetDataList = [row for row in budgetDataCSV]


# calculate all the parameters
totalNoMonths=len(budgetDataList)

sumValue=0
# diffvector is the vector of differences; has one element less than budget data
diffVector = []
for i in range(0 ,totalNoMonths):
    sumValue += float(budgetDataList[i][1])
    if i>0:
        diffVector.append(float(budgetDataList[i][1])-float(budgetDataList[i-1][1]))
    

averageChange= sum(diffVector)/len(diffVector)

greatestIncreaseProfit=max(diffVector)
greatestIncreaseProfitIndex=diffVector.index(max(diffVector))
greatestIncreaseProfitMonth=budgetDataList[greatestIncreaseProfitIndex+1][0]

greatestDecreaseProfit=min(diffVector)
greatestDecreaseProfitIndex=diffVector.index(min(diffVector))
greatestDecreaseProfitMonth=budgetDataList[greatestDecreaseProfitIndex+1][0]

# print the output
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", totalNoMonths,sep='')
print("Total: $", int(sumValue), sep='')
print("Average  Change: $", round(averageChange,2), sep='')
print("Greatest Increase in Profits: ", greatestIncreaseProfitMonth, " ($",int(greatestIncreaseProfit),")", sep='')
print("Greatest Decrease in Profits: ", greatestDecreaseProfitMonth, " ($",int(greatestDecreaseProfit),")", sep='')


# create a text file with the output in the same folder as the code
LineA = "Financial Analysis"
LineB = "----------------------------"
Line1 = "Total Months: " + str(totalNoMonths)
Line2 = "Total: $" + str(int(sumValue))
Line3 = "Average  Change: $" + str(round(averageChange,2))
Line4 = "Greatest Increase in Profits: " + greatestIncreaseProfitMonth + " ($" + str(int(greatestIncreaseProfit)) + ")"
Line5 = "Greatest Decrease in Profits: " + greatestDecreaseProfitMonth + " ($" + str(int(greatestDecreaseProfit)) + ")"

budgetDataTxt=open("BudgetDataAnalysisOoutput.txt","w")
budgetDataTxt.write("%s\n%s\n%s\n%s\n%s\n%s\n%s" % (LineA, LineB, Line1, Line2, Line3, Line4, Line5))
budgetDataTxt.close