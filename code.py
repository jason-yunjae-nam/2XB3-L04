def are_valid_groups(num, groups):
    for n in range(len(num)):
        num[n] = str(num[n])
    check = 0
    i = 0
    while i < len(num):
        for j in range(len(groups)):
            if (len(groups[j])<2) or (len(groups[j])>3):
                return False
            check += groups[j].count(int(num[i]))
        if check!=1:
            return False
        i+=1
        check=0
    else:
        return True