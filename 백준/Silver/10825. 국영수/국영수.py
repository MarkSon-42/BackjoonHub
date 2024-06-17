N = int(input())
students = []

for _ in range(N):
    student = input().split()
    students.append((student[0], int(student[1]), int(student[2]), int(student[3])))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])