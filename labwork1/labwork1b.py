def input_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


def input_courses():
    courses = []

    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print("\nCourse", i + 1)

        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)

    return courses


def list_students(students):
    print("\n--- STUDENTS ---")

    for student in students:
        print(
            student["id"],
            "|",
            student["name"],
            "|",
            student["dob"]
        )


def list_courses(courses):
    print("\n--- COURSES ---")

    for course in courses:
        print(
            course["id"],
            "|",
            course["name"]
        )


def input_marks(students, courses):
    print("\n--- ENTER MARKS ---")

    course_id = input("Enter course ID: ")

    # Find the course
    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found")
        return

    print("Enter marks for", course["name"])

    for student in students:
        mark = float(
            input("Enter mark for " + student["name"] + ": ")
        )

        if "marks" not in student:
            student["marks"] = {}

        student["marks"][course_id] = mark


def show_marks(students, courses):
    course_id = input("\nEnter course ID: ")

    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found")
        return

    print("\n--- MARKS FOR", course["name"], "---")

    for student in students:
        mark = "No mark"

        if "marks" in student:
            if course_id in student["marks"]:
                mark = student["marks"][course_id]

        print(student["id"], "|", student["name"], "|", mark)


# Main program

students = input_students()

courses = input_courses()

list_students(students)

list_courses(courses)

input_marks(students, courses)

show_marks(students, courses)