mass2 = int(input("enter mass: "))
mass1 = 1

def vel(u1,u2):
    v_cm = (mass1*u1+mass2*u2)/(mass1+mass2)
    u1 = 2*v_cm-u1
    u2 = 2*v_cm-u2
    return u1,u2

u1 = 0
u2 = -1000
count = 0
while(u1 > u2):
    count += 1
    l =vel(u1,u2)
    u1 = l[0]
    u2 = l[1]
    if u1<0:
        count +=1
        u1 = -u1
    else:
        break
print(count)
