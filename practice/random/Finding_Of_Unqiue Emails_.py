def numuniqueEmails(emails):
    unique_emails = set()

    for email in emails:
        local_name, domain_name = email.split('@')
        # Rule 1 + Rule 2
        local_rule = local_name.split('+')[0].replace('.','')
        unique_emails.add(local_rule + '@' + domain_name)

    return len(unique_emails)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
count = numuniqueEmails(emails)
print("Number of unqiue Email Addresses", count)