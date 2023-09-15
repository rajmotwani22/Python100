# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#print(student_heights)

#Write your code below this row 👇
a=0
for i in student_heights:
    a=a+i
#print(a)
k=0
for j in student_heights:
    k+=1
print(round(a/k))

