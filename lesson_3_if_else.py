number= 2
number2=3
#result=number == number2
#print(result)

#result=number!= number2
#print(result)

result=number > number2
print(result)
result=number < number2
print(result)
result=number >= number2
print(result)
result=number <= number2
print(result)
#Это сравнение!

num_1=int(input("Enter number:" ))
print("cool", num_1)
print("Your number's type is",type(num_1))

result=num_1 > 0
#print(result,"Is positive?")

positive="Your number is positive"
negative="YOUR NUMBER IS NEGATIVE."



#if num_1 > 0:
    #print(positive)
#else:
   # print(negative)
#print("See you")

#"if,else"if,elif,"if,elif,else"


if num_1 > 100:
    print("Oh your number cool")
elif 0 < number < 100:
    print("BRO your number between 0 and 100")
else:
    print("else")

#and
result = 5 > 4 and 7 > 1  #True
result = 4 > 5 and 1 > 7   #False

main_ort= 180
math= 135

result= main_ort >= 150 and math >= 100
print("Поступил?", result)

#or

has_money = True
main_ort = 1
result = main_ort >= 150 or has_money

#or,and

money= True
ort= 150
test=10

result=ort >= 150 and (test >= 7 or money)
print(result)
