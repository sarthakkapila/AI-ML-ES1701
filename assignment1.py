# Q1: Split this string

s = "Hi there Class!"
result = s.split()
print("answer for Q1")
print(result)

# Q2: Use .format() to print the following string:

planet = "Earth"
diameter = 12742
print("answer for Q2")
print("The diameter of {} is {} kilometers.".format(planet, diameter))

# Q3: Use indexing to grab the word "hello"

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
word = lst[3][1][2][0]
print("answer for Q3")
print(word)

# Q4: Grab the word "hello" from nested dictionary

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
word = d['k1'][3]['tricky'][3]['target'][3]
print("answer for Q4")
print(word)

# Q5: Function to grab email website domain

def get_domain(email):
    return email.split('@')[1]

# Example usage
email = "user@domain.com"
print("answer for Q5")
print(get_domain(email))

# Q6: Basic function to check if 'dog' is contained in the input string

def contains_dog(input_str):
    return 'dog' in input_str.lower()

# Example usage
print("answer for Q6")
print(contains_dog("There is a Dog in the park"))

# Q7: Function to count occurrences of the word "dog" in a string

def count_dog_occurrences(input_str):
    return input_str.lower().count('dog')

# Example usage
print("answer for Q7")
print(count_dog_occurrences("Dog is a loyal animal. I love my dog."))

# Q8: Use lambda expressions and the filter() function to filter out words not starting with 's'

seq = ['soup','dog','salad','cat','great']
filtered_seq = list(filter(lambda word: word[0].lower() == 's', seq))
print("answer for Q8")
print(filtered_seq)

# Q9: Function to determine Challan based on speed and birthday

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

# Example usage
print("answer for Q9")
print(caught_speeding(81, True))
print(caught_speeding(81, False))


# Q10: Concatenate two lists index-wise

list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]
result = [a + b for a, b in zip(list1, list2)]
print("answer for Q10")
print(result)

# Q11: Concatenate two lists in the specified order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [a + b for a in list1 for b in list2]
print("answer for Q11")
print(result)

# Q12: Add item 7000 after 6000 in the Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print("answer for Q12")
print(list1)

# Q13: Remove all occurrences of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [item for item in list1 if item != 20]
print("answer for Q13")
print(list1)

# Q14: Check if value 200 exists in a dictionary

d1 = {'a': 100, 'b': 200, 'c': 300}
print("answer for Q14")
print(200 in d1.values())

# Q15: Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms

n = 5
series_sum = sum(int('2' * i) for i in range(1, n + 1))
print("answer for Q15")
print(series_sum)