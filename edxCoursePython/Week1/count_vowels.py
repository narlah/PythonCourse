# s = "azcbobobegghakl"
# vowels = (s.count('a') + s.count('e') + s.count('i') + s.count('o')+ s.count('u'))
# print "Number of vowels: "+ str(vowels)

# s = "azcbobobegghakl"
# upper_index = 0
# number_of_bobs = 0
# while upper_index < len(s)-1:
#     bob_index = s.find('bob', upper_index)
#     if bob_index != -1:
#         number_of_bobs += 1
#         upper_index = bob_index + 1
#     else:
#         break
# print "Number of times bob occurs is: " + str(number_of_bobs)


def item_order(order):
    salads = order.count("salad")
    hamburgers = order.count("hamburger")
    waters = order.count("water")
    return "salad:"+ str(salads)+ " hamburger:"+ str(hamburgers)+ " water:"+ str(waters)


order = "salad water hamburger salad hamburger"
print item_order(order)