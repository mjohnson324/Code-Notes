def sum_of_multiples(limit, multiples):
    sum = 0
    used_nums = []
    for num in multiples:
        current_num = num
        while current_num < limit:
            if not_already_used(current_num, used_nums):
                sum += current_num
            current_num += num
        used_nums.append(num)
    return sum

def not_already_used(num, used_nums):
    for n in used_nums:
        if num % n == 0:
            return False
    return True