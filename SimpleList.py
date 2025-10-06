acronyms = ['NASA', 'FBI', 'CIA', 'NSA']
print(acronyms[0])

acronyms.append('UNICEF')
print(acronyms)

acronyms.remove('FBI')
print(acronyms)

for agency in acronyms:
    print(agency)