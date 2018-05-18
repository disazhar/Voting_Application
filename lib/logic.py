candidates = input("How many candidates do we have?\n")
candidates = int(candidates)
print("OK! So we have " + str(candidates) + " votable candidates.")
print("Specify their names!\n")


for candidates_number in range(candidates): 
    print(int(candidates_number)) '''to help me visualize what i'm doing'''


overall = candidates
print(list(range(overall)))
complete_list = range(overall)
print(complete_list) '''to help me visualize what i'm doing'''

for candidate_name in range(complete_list):
    print("Write candidates names.\n")