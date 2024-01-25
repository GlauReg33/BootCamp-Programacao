turno = input('Em qual turno você estuda? M para matutino, V para vespertino ou N para noturno: ')

if turno =='M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor invalido!')