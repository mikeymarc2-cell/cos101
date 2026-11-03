# 1. Speed
distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed =", speed, "m/s")


# 2. Acceleration
initial_velocity = float(input("\nEnter initial velocity (m/s): "))
final_velocity = float(input("Enter final velocity (m/s): "))
time = float(input("Enter time (s): "))
acceleration = (final_velocity - initial_velocity) / time
print("Acceleration =", acceleration, "m/s²")


# 3. Force
mass = float(input("\nEnter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
force = mass * acceleration
print("Force =", force, "N")


# 4. Work Done
force = float(input("\nEnter force (N): "))
distance = float(input("Enter distance (m): "))
work_done = force * distance
print("Work Done =", work_done, "J")


# 5. Kinetic Energy
mass = float(input("\nEnter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
kinetic_energy = 0.5 * mass * velocity ** 2
print("Kinetic Energy =", kinetic_energy, "J")
