# Final Deliverables / Pseudocode
    #1) Total number of votes cast
    #2) A complete list of candidates who received votes
    #3) Total number of votes each candidate received
    #4) Percentage of votes each candidate won
    #5) The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add dependencies
import csv
import os

# Assign a variable to load a file from an indirect path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to an indirect path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



# 1. Initialize a total vote counter.
total_votes = 0




# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)



    # Print (Iterate) each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)


