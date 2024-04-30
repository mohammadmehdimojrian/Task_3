from itertools import permutations

persons=['a', 'b', 'c', 'd']
person_dic={'a':[],'b':[],'c':[],'d':[]}
person_lst=[]
chooser=[]
count=1
for pr in permutations(persons):
    A,B,C,D =pr
    p_A = (A != 'c')
    p_B = (B == 'b')
    p_C = (C != 'b')
    p_D = (D != 'b')

    if p_A and p_B and p_C and p_D:
        print(f"Ehtemal dozd budan dar halat {count} az chap be rast: ")
        print(f'{A}, {B}, {C}, {D}')
        person_lst.append([D,C,B,A])
        count+=1
for i in person_lst:
    for j in i:
        person_dic[j].append(i.index(j))

for item in person_dic:
    person_dic[item]=sum(person_dic[item])
mx=max(person_dic.values())
person_tuple=tuple(person_dic.items())
for (a,b) in person_tuple:
    if b==mx:
        print(f"jenab dozd:{a}")
        exit()

#جان هرکسی که دوست دارین دفعه بعد تمرین آدمیانه تری بدین 