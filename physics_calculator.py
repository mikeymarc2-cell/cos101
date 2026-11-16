def speed():
    distance = float(input("Enter the distance (in meters): "))
    time = float(input("Enter the time (in seconds): "))
    speed = distance / time
    print(f"The speed is {speed} m/s")


def acceleration():
    initial_velocity = float(input("Enter the initial velocity (in m/s): "))
    final_velocity = float(input("Enter the final velocity (in m/s): "))
    time = float(input("Enter the time (in seconds): "))
    acceleration = (final_velocity - initial_velocity) / time
    print(f"The acceleration is {acceleration} m/s²")


def force():
    mass = float(input("Enter the mass (in kg): "))
    acceleration = float(input("Enter the acceleration (in m/s²): "))
    force = mass * acceleration
    print(f"The force is {force} N")


def work_done():
    force = float(input("Enter the force (in N): "))
    distance = float(input("Enter the distance (in meters): "))
    work = force * distance
    print(f"The work done is {work} J")


def kinetic_energy():
    mass = float(input("Enter the mass (in kg): "))
    velocity = float(input("Enter the velocity (in m/s): "))
    kinetic_energy = 0.5 * mass * velocity ** 2
    print(f"The kinetic energy is {kinetic_energy} J")


while True:
    print("Physics Calculator")

    formula = ["1. Speed", "2. Acceleration", "3. Force",
               "4. Work Done", "5. Kinetic Energy"]

    for form in formula:
        print(form)

    entry = input("Enter a quantity: ")

    if entry == "1":
        speed()

    elif entry == "2":
        acceleration()

    elif entry == "3":
        force()

    elif entry == "4":
        work_done()

    elif entry == "5":
        kinetic_energy()

    else:
        print("Input a valid quantity")

    again = input("Do you want to calculate something else? (yes or no): ")

    if again.lower() == "yes":
        continue

    else:
        print("Thank you")
        break
