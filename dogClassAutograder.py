import dogClass as dg


doc = 'dogs.txt'
file = open(doc)
line = file.readline()

#Part 1 Check
dogsList = []
totalCorrect = 0
totalAttempts = 0
while (line):
    d, a, o, m, day, y = line.split(" ")
    try:
        appt = (int(m), int(day), int(y))
        dog = dg.Dog(d, int(a), o, appt)
        dogsList.append(dog)
    except:
        print("Dog class implemented incorrectly.")
        
    line = file.readline()
file.close()
totalCorrect += 10
totalAttempts += 10

try:
    test1 = dg.findAppointments(dogsList, 4)
    test2 = dg.findAppointments(dogsList, 12)
    test3 = dg.findAppointments(dogsList, 9)
    test4 = dg.findAppointments(dogsList, 5)
    test5 = dg.findAppointments(dogsList, 1)
except:
    print("findAppointments() implemented incorrectly")
    print("Unable to calculate grade.")
    exit()
    


#Part 3 Check
if len(test1)== 3:
    totalCorrect+=1
else:
    print("Incorrect list length for month 4.")

if len(test2) == 1:
    totalCorrect+=1
else:
    print("Incorrect list length for month 12.")
if len(test3) == 2:
    totalCorrect+=1
else:
    print("Incorrect list length for month 9.")
if len(test4) == 0:
    totalCorrect+=1
else:
    print("Incorrect list length for month 5.")
if len(test5) == 1:
    totalCorrect+=1
else:
    print("Incorrect list length for month 1.")

comp = type(())
c = type(test1[0])
if type(test1[0]) == comp:
    totalCorrect +=1
else:
    print("Tuple not stored in findAppointment() list.")
if len(test1[0]) == 2:
    totalCorrect +=1
else:
    print("Incorrect size of tuple in findAppoints() list.")
totalAttempts +=7

#Part 2 check
comp1 = [('Rubble', '04/04/23'), ('Clifford', '04/14/23'), ('Snoopy', '04/08/23')]
for i, dog in enumerate(test1):
    if test1[i][0] == comp1[i][0]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for dog "  + comp1[i][0])
    
    if test1[i][1] == comp1[i][1]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for "  + comp1[i][1])
    totalAttempts+= 2

comp2 = [('Max', '12/25/22')]
for i, dog in enumerate(test2):
    if test2[i][0] == comp2[i][0]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for dog "  + comp2[i][0])
    
    if test2[i][1] == comp2[i][1]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for "  + comp2[i][1])
    totalAttempts+= 2

comp3 = [('Toto', '09/21/22'), ('Bolt', '09/30/22')]
for i, dog in enumerate(test3):
    if test3[i][0] == comp3[i][0]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for dog "  + comp3[i][0])
    
    if test3[i][1] == comp3[i][1]:
        totalCorrect+= 1
    else:
        print("Incorrect entry for "  + comp3[i][1])
    totalAttempts+= 2


print("Final grade is: " + str(totalCorrect/totalAttempts * 100) + "%")