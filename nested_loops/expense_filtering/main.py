# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

#initialize outer-loop index for trips
i = 0
#iterate over each trip
while i < len(travel_costs):
    #start a fresh list for the current trip (row)
    trip_expenses = []
    #initialize the inner-loop index for individual expenses
    j = 0
    #iterates through each expense in trip i
    while j < len(travel_costs[i]):
        #if expense is less than 100 it appends the string 'Cheap' otherwise appends the original numeric expense value
        if travel_costs[i][j] <= 100:
            trip_expenses.append('Cheap')
        else:
            trip_expenses.append(travel_costs[i][j])
        #moves to the next expense
        j += 1
    #after all expenses in trip i are processed, append the list trip_expenses to processed_expenses 
    processed_expenses.append(trip_expenses)
    #iterates through next trip
    i += 1
            
# output
print('Processed Travel Expenses:', processed_expenses)