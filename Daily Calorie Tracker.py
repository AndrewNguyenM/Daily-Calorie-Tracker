#Andrew Nguyen
#Daily Calories Tracker

def BMI():

    gender = input("Enter your gender from birth: (M or F) ")

    def save_to_file(AMR):
        with open('daily_calories_tracker.txt', 'a') as file:
            file.write(f'{AMR:.2f}')

    def calculate_AMR(BMR, activity_level):
        activity_factors = {
            "Sedentary": 1.2,
            "Lightly active": 1.375,
            "Moderately active": 1.55,
            "Active": 1.725,
            "Very active": 1.9
        }
        return BMR * activity_factors[activity_level]

    def get_activity_level():
        while True:
            AMR_level = input("\nEnter you Activity Level:\n"
                              + "Sedentary (little or no exercise)\n"
                              + "Lightly active (exercise 1–3 days/week)\n"
                              + "Moderately active (exercise 3–5 days/week)\n"
                              + "Active (exercise 6–7 days/week)\n"
                              + "Very active (hard exercise 6–7 days/week)\n")
            if AMR_level in ["Sedentary", "Lightly active", "Moderately active", "Active", "Very active"]:
                return AMR_level
            else:
                print("Invalid activity level. Please enter one of the given options.")

    def women():
        height_female = float(input("Enter your height in total centimeters: "))
        weight_female = float(input("Enter you weight in kg: "))
        age_female = int(input("Enter your age: "))
        female_BMR = 655 + (9.6 * weight_female) + (1.85 * height_female) - (4.67 * age_female)
        print(f'Your BMR is {female_BMR} calories per day')
        AMR = calculate_AMR(female_BMR, get_activity_level())
        print(f'Your AMR is {AMR:.2f} calories per day')
        save_to_file(AMR)

    def men():
        height_male = float(input("Enter your height in total centimeters: "))
        weight_male = float(input("Enter you weight in kg: "))
        age_male = int(input("Enter your age: "))
        man_BMR = 66 + (13.7 * weight_male) + (5 * height_male) - (6.8 * age_male)
        print(f'Your BMR is {man_BMR} calories per day')
        AMR = calculate_AMR(man_BMR, get_activity_level())
        print(f'Your AMR is {AMR:.2f} calories per day')
        save_to_file(AMR)

    if gender == "M" or gender == 'm':
        men()
    elif gender == "F" or gender == "f" :
        women()
    else:
        print("Enter a valid gender")

def food_tracker():
    def read_numbers_from_file(file_name):
        numbers = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = float(line)  
                    numbers.append(number)
                except ValueError:
                    print(f"Could not convert '{line}' to a number.")
        return numbers

    def subtract_calories(file_name):
        amr_values = read_numbers_from_file(file_name)
        try:
            consumed_calories = int(input("Enter the number of calories consumed from food: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        remaining_calories = [amr - consumed_calories for amr in amr_values]
        return remaining_calories

    def update_file_with_new_values(file_name, values):
        with open(file_name, 'w') as file:
            for value in values:
                file.write(f'{value:.2f}\n')

    remaining_calories = subtract_calories('daily_calories_tracker.txt')
    if remaining_calories is not None:
        print("Remaining calories after subtracting consumed food:")
        for calories in remaining_calories:
            print(f"{calories:.2f}")

        # Update the file with the new values
        update_file_with_new_values('daily_calories_tracker.txt', remaining_calories)

app = input('Hello are you a new or returning user? ')
if app == "New" or app == "new":
    BMI()
elif app == 'returning' or app == 'Returning':
    food_tracker()
else:
    print("Please enter 'New' or 'Returning' to proceed.")


