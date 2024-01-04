# def input_num():
#     num_list = []
#     for i in range(4):
#         num = int(input(f"Enter Number{i+1}: "))
#         num_list.append(num)

#     return num_list

def avg(*num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    
    return sum / len(num_list)


# print(avg(input_num()))
print(avg(4, 5, 6, 7))