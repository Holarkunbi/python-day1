print ((lambda *args:sum(args))(12,8,12))
print((lambda **kwargs : sum(kwargs.values()))(n=12, a=50, t=100))

#checking if a number is an even number
even_number = lambda number:number%2==0
print(even_number(121))


# filter() with lambda() 
score = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
student_name = {"first_name":"adeleye", "middle_name":"olakunle","last_name": "ola"}

print(student_name.get("middle_namee"))
print(student_name["last_name"])


for value in student_name.values():
    print(value)

# student = filter(lambda values: values==student_name.keys ,student_name)
# print(dict(student))

final_score= filter(lambda x: x<50 , score)

print(list(final_score)) 
