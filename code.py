def are_valid_groups(studentnumbers, groups):
    counts = 0
    for i in range(len(groups)):
        for j in range(len(studentnumbers)):
            counts += groups[i].count(studentnumbers[j])
    if counts == 0:
        return False
    else:
        return True