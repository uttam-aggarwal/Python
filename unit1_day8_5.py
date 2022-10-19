'''A university wants to create new official mail id's for their students. They decided to generate mail id's in the format as "name of the student + birth year@mail.com". Assume this task is assigned to you by the university, and now you have to generate the mail id's for the students in mentioned format.
Constraints:
1995 <= birth year <= 2005
Sample Test case:
robert →→→→ First line of input contains the name of the student
2001 →→→→ Second line of the input contains the Birth year of the student robert2001@mail.com> (Output as required)'''
a=input()
b=input()
print(a+b, "@mail.com",sep="")