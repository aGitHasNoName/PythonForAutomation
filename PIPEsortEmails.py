'''
This notebook takes a csv file with names in the first column, and email addresses in the remaining columns.

Each person has at least one email address. Many have more than one. The email addresses are not ordered.

This notebook orders the email addresses by the priority 1. any email address containing "northwestern.edu", 2. address containing "nm.org", 3. address containing "luriechildrens.org", and 4. any other email addresses will be added unsorted at the end.

The code assumes that a person would only have one email address with each domain name.

The code also removes duplicate email addresses.

The notebook outputs a new csv file.

sys.argv[1] is the input file (or path to it)
sys.argv[2] is the output file (or path to it)
'''

import sys

input_data = {line.split(",")[0]:line.rstrip("\n").split(",")[1:] for line in sys.stdin}

preferred_emails = ["northwestern.edu", "nm.org", 
                    "luriechildrens.org", "sralab.org"]

        
def removeDups(a_list):
    '''removes duplicates from a list while keeping the order'''
    noDups = []
    [noDups.append(item) for item in a_list if item not in noDups]
    return noDups

def dictToFile(a_dict):
    '''writes a dictionary with a list as the value to a file'''
    for k, v in a_dict.items():
        sys.stdout.write(f"{k},{','.join(v)}\n")

def main():
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
    dictToFile(final_dict)
            
if __name__ == "__main__":
    main()