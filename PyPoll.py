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

# Create a variable and assign the path to extract from Election Results.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a variable and assign the path to save analysis to Election Analysis.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
    # Read the Election Results file.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
