# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50], [200, 300, 120, 80], [180, 220, 130, 170], [600, 250, 200, 90], [300, 180, 150, 70], [400, 320, 110, 100], [550, 270, 180, 60], [250, 190, 140, 120], [700, 350, 210, 110], [450, 230, 160, 95], [320, 280, 190, 85], [580, 260, 175, 75], [630, 300, 220, 130], [280, 210, 125, 140], [490, 330, 145, 105], [520, 340, 190, 125], [750, 400, 250, 150], [340, 270, 160, 115], [620, 310, 225, 135], [410, 290, 135, 90]]

# List to store the first significant expense of each trip
significant_expenses = []

#filter thresholds
ignore = 100

# Outer while loop to iterate through trips
i = 0
while i < len(travel_costs):
    first_significant = None
    #inner for loop to iterate expenses 
    for cost in travel_costs[i]:
        if cost < ignore:
            continue
        if cost > 200:
            first_significant = cost
            significant_expenses.append(first_significant) 
            break
       
    i += 1  
print('First Significant Expenses:', significant_expenses)