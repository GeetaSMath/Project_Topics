import re
domainlist=['m.google.com',
            'm.docs.google.com',
            'www.someisotericdomain.innersite.mall.co.uk',
            'www.puruniversity.department.mit.ac.us',
            'www.somestrangeurl.shops.relevantdomain.net',
            'www.exampple.info']
print(domainlist)
#to check domain names
for i in domainlist:
    print(i)

for i in domainlist:
    res=re.findall(r'(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',i)
    print(i, "|", res[0])