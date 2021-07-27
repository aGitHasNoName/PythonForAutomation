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

def csvToDict(filename):
    '''turns a csv file to a dict with the first item as key and other items as list'''
    with open(filename, "r") as f:
        a_dict = {line.split(",")[0]:line.rstrip("\n").split(",")[1:] for line in f.readlines()}
    return a_dict
        
def removeDups(a_list):
    '''removes duplicates from a list while keeping the order'''
    noDups = []
    [noDups.append(item) for item in a_list if item not in noDups]
    return noDups

def dictToFile(a_dict, filename):
    '''writes a dictionary with a list as the value to a file'''
    with open(filename, "w") as f:
        for k, v in a_dict.items():
            f.write(f"{k},{','.join(v)}\n")

def main():
    input_data = csvToDict(input_file)
    final_dict = {}
    for name, email_list in input_data.items():
        emails = [i for i in email_list if i != ""]
        other_emails = [e for e in emails if e.split("@")[1] not in preferred_emails]
        ordered_emails = []
        for p in preferred_emails:
            for e in emails:
                if e.split("@")[1] == p:
                    ordered_emails.append(e)
        if len(other_emails) >= 1:
            ordered_emails = ordered_emails + other_emails
        final_dict[name] = removeDups(ordered_emails) 
    dictToFile(final_dict, output_file)
            
if __name__ == "__main__":
    main()