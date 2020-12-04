stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org_list = org.split()
base = []
for i in org_list:
    if i not in stopwords:
        base.append(i[0].upper())
acro = "".join(base)
print(acro)
