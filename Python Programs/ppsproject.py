# Initialize an empty dictionary to store student records
'''student_records = {}

# Function to add a new student record
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    student_records[student_id] = {'Name': name, 'Grade': grade}
    print(f"Student {name} with ID {student_id} added to records.")

# Function to display all studen
def display_records():
    if not student_records:
        print("No student records found.")
    else:
        print("Student Records:")
        for student_id, data in student_records.items():
            print(f"ID: {student_id}, Name: {data['Name']}, Grade: {data['Grade']}")

# Function to search for a student record
def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in student_records:
        print(f"Student ID: {student_id}, Name: {student_records[student_id]['Name']}, Grade: {student_records[student_id]['Grade']}")
    else:
        print("Student not found in records.")

# Main loop for the student record system
while True:
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. Display Records")
    print("3. Search Student")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_records()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Exiting Student Record System. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")'''

import turtle

# Draw a function
def draw_rose():
    rt = turtle.Turtle()
    rt.hideturtle()
    rt.pensize(10)
    rt.speed(0)
    rt.fillcolor("orange red")
    rt.begin_fill()
    rt.rt(40)
    rt.circle(20, 90)
    rt.fd(40)
    rt.circle(10, 115)
    rt.circle(-100, 40)
    rt.circle(80, 70)
    rt.circle(5, 160)
    x, y = rt.pos()
    pen = 10
    for i in range(4):
        rt.pensize(pen-(2*i))
        rt.circle(-100, 7)
    rt.up()
    rt.goto(x, y)
    rt.down()
    rt.pensize(10)
    rt.rt(38)
    rt.circle(200, 45)
    rt.rt(135)
    rt.fd(40)
    rt.circle(-10, 45)
    rt.circle(-50, 40)
    rt.circle(10, 40)
    rt.fd(40)
    rt.circle(-10, 140)
    rt.fd(30)
    rt.end_fill()
    rt.up()
    rt.seth(90)
    rt.fd(70)
    rt.down()
    rt.lt(20)
    rt.begin_fill()
    rt.circle(-40, 100)
    rt.circle(20, 40)
    rt.circle(-50, 80)
    rt.rt(60)
    rt.fd(10)
    rt.back(10)
    rt.seth(70)
    rt.circle(-40, 90)
    rt.circle(10, 15)
    rt.fd(20)
    rt.circle(-40, 100)
    rt.circle(-10, 20)
    rt.fd(30)
    x, y = rt.pos()
    rt.fd(120)
    x1, y1 = rt.pos()
    rt.rt(72)
    rt.circle(-100, 40)
    rt.circle(80, 65)
    rt.end_fill()
    rt.up()
    rt.goto(x+5, y)
    rt.down()
    rt.seth(-10)
    rt.begin_fill()
    rt.circle(-100, 40)
    rt.circle(-20, 120)
    rt.circle(40, 70)
    rt.circle(-50, 142)
    rt.end_fill()
    rt.up()
    rt.goto(x1, y1)
    rt.down()
    rt.seth(40)
    rt.circle(50, 60)
    rt.circle(-50, 40)
    rt.lt(10)
    rt.circle(50, 95)
    x, y = rt.pos()
    r = 20
    for i in range(3):
        rt.pensize(pen-5*i)
        rt.circle((r-5*i), 180)
    rt.pensize(pen)
    rt.up()
    rt.goto(x, y)
    rt.down()
    rt.seth(160)
    rt.circle(50, 120)
    rt.circle(100, 60)
    rt.circle(-20, 40)
    x, y = rt.pos()
    rt.up()
    rt.goto(x+20, y-45)
    rt.down()
    rt.seth(-90)
    rt.pensize(5)
    rt.seth(-90)
    rt.fillcolor("green")
    rt.begin_fill()
    rt.circle(-50, 45)
    rt.seth(-90)
    rt.fd(40)
    rt.circle(200, 30)
    x, y = rt.pos()
    rt.circle(-200, 30)
    rt.seth(180)
    rt.fd(10)
    rt.rt(90)
    rt.circle(200, 30)
    rt.circle(-200, 30)
    rt.fd(40)
    rt.lt(45)
    rt.circle(-50, 50)
    rt.seth(45)
    rt.fd(20)
    rt.end_fill()
    rt.up()
    rt.goto(x, y)
    rt.down()
    rt.seth(10)
    rt.pensize(10)
    rt.fd(20)
    x, y = rt.pos()
    rt.pensize(5)
    rt.seth(90)
    rt.begin_fill()
    rt.circle(-50, 45)
    for i in range(9):
        rt.lt(10)
        rt.fd(10)
        rt.rt(170)
        rt.fd(10)
        rt.lt(165)
        rt.circle(-50, 10)
    rt.circle(-50, 20)
    rt.rt(150)
    rt.circle(50, 20)
    rt.up()
    rt.goto(x, y)
    rt.down()
    rt.seth(-30)
    rt.circle(50, 45)
    for i in range(9):
        rt.rt(10)
        rt.fd(10)
        rt.lt(170)
        rt.fd(10)
        rt.rt(165)
        rt.circle(50, 10)
    rt.end_fill()
    rt.lt(150)
    pen = 5

    for i in range(10):
        rt.pensize(pen+i)
        rt.fd(10)

    return rt


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("pink")

    # Draw
    draw_rose()

    # Print
    turtle.penup()
    turtle.goto(0, -280)
    turtle.color("red")
    turtle.write("HAPPY ROSE DAY BHUMIKA <3", align="center", font=("Arial", 24, "bold"))

    screen.mainloop()


if __name__ == "__main__":
    main()
