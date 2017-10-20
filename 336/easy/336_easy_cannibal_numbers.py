numbers = set(map(int, "1 2 3 4 5".split(' ')))
test_input = 5
result_list = set(filter(lambda x: x >= test_input, numbers))
numbers = numbers.difference(result_list)
for cannibal in sorted(numbers, reverse=True):
    final = cannibal
    inputs = set()
    for food in sorted(numbers):
        if food != cannibal:
            final += 1
            inputs.add(food)
        if final >= test_input:
            result_list.add(cannibal)
            numbers = numbers.difference(result_list)
            numbers = numbers.difference(inputs)
            break

print(len(result_list))
