S=str(input('Introduceți șirul de caractere:  '))
#a)numarul de aparitii a caracterului A în șirul S
a=0
for i in range(0,len(S)):
    x=ord(S[i])
    if x==65:
        a+=1
print(a,'  numarul de aparitii a caracterului A în șirul S')
#b)sirul obtinut prin substituirea caracterului 'A' prin caracterul '*'
S1=''
for i in S:
    if ord(i)==65:
        S1+='*'
    if ord(i)!=65:
        S1+=chr(ord(i))
print(S1,' sirul obtinut prin substituirea caracterului A prin caracterul *')
#c)şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’
S2=''
for i in S:
    if ord(i)==66:
        S2+=''
    if ord(i)!=66:
        S2+=chr(ord(i))
print(S2, ' şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului B')
#d)numărul de apariţii ale silabei MA în şirul S
MA=0
for i in S:
    MA=S.count('MA')
print(MA, ' numărul de apariţii ale silabei MA în şirul S')
#e)şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA
S3=''
for i in S:
    S3=S.replace('MA', 'TA')
print(S3, ' şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA')
#f)şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO
S4=''
for i in S:
    S4=S.replace('TO', '')
print(S4,' şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO')
#g)scrierea inversă a şirului S
S5=''
S5=S[::-1]
print(S5, ' scrierea inversă a şirului S')