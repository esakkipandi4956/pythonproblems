for if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
unique_grade=sorted(set([score for name,score in student]))
second_lower_grade=unique_grade[1]
second_lower_student=[name for name,score in student if score==second_lower_grade]
second_lower_student.sort()
for student in second_lower_student:
    print(student)
