'''
This notebook takes a csv file with names in the first column, and email addresses in the remaining columns.

Each person has at least one email address. Many have more than one. The email addresses are not ordered.

This notebook orders the email addresses by the priority 1. any email address containing "northwestern.edu", 2. address containing "nm.org", 3. address containing "luriechildrens.org", and 4. any other email addresses will be added unsorted at the end.

The code assumes that a person would only have one email address with each domain name.

The code also removes duplicate email addresses.

The notebook outputs a new csv file.
'''

input_file = "email_addresses.csv"
output_file = "preferredEmails2.csv"

preferred_emails = ["northwestern.edu", "nm.org", 
                    "luriechildrens.org", "sralab.org"]

with open(input_file, "r") as f:
    input_data = {line.split(",")[0]:line.rstrip("\n").split(",")[1:] for line in f.readlines()}

final_dict = {}
for name, email_list in input_data.items():
    emails = [i for i in email_list if i != ""]
    ordered_emails = []
    other_emails = [e for e in emails if e.split("@")[1] not in preferred_emails]
    for p in preferred_emails:
        for e in emails:
            if e.split("@")[1] == p:
                ordered_emails.append(e)
    if len(other_emails) >= 1:
        ordered_emails = ordered_emails + other_emails
    noDups = []
    [noDups.append(item) for item in ordered_emails if item not in noDups]
    final_dict[name] = noDups
    
with open(output_file, "w") as f:
    for name, email in final_dict.items():
        f.write(f"{name},{','.join(email)}\n")