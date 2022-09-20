emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
final_list=[]
copy_final=0
for i in emails:
    local, at, domain = i.rpartition('@')
    sep = '+'
    stripped = local.split(sep, 1)[0]
    string = stripped.replace(".", "")
    final = string+at+domain

    if copy_final==0:
        copy_final = final
        final_list.append(final)
    elif copy_final!=final:
        final_list.append(final)
print(*final_list)









