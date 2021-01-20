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
