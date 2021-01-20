def are_valid_groups(st_nums, groups):
    count = 0
    for num in st_nums:
        for group in groups:
            for i in group:
                if num == i:
                    count = count + 1
                    break
                    
    if count == len(st_nums):
        return True
    return False