<<<<<<< HEAD
def are_valid_groups(studentnumbers, groups):
    counts = 0
    for i in range(len(groups)):
        for j in range(len(studentnumbers)):
            counts += groups[i].count(studentnumbers[j])
    if counts == 0:
        return False
    else:
        return True
=======
def are_valid_groups(num, groups):
    counter = 0
    i = 0
    while i < len(num):
        for j in range(len(groups)):
            counter += groups[j].count(num[i])
        if counter == 0:
            return False
        i+=1
        counter=0
    else:
        return True
>>>>>>> c5e96d5ecbe5fbeae9a5a9c0e8a4316a4084c335
