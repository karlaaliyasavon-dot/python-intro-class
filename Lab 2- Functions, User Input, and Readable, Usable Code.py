heart_rate_samples = {
"J. Alvarez": [72, 75, 78],
"M. Chen": [80, 82],
"R. Okafor": [65, 68, 70, 66],
"S. Patel": [90, 95, 92, 88, 91],
"T. Nguyen": [77, 79],
"L. Kowalski": [68, 70, 69],
"D. Osei": [98, 101, 95, 99],
"A. Whitfield": [74, 76, 75, 73],
}

my_patient_list= list(heart_rate_samples)

def get_all_stats(patient_number):
    patient_name = my_patient_list[patient_number]
    return heart_rate_samples[patient_name]

def get_specific_stats(patient_number, *indexes):
    patient_name = my_patient_list[patient_number]
    patient_data = heart_rate_samples[patient_name]

    return [patient_data[i] for i in indexes]

def get_patient_number_by_name(name):
    name= name.lower().strip()
    for i, patient in enumerate(my_patient_list):
        if patient.lower() == name:
            return i
    raise ValueError("Patient not found")

def get_patients_in_range(low, high):
    """Return all patients who have at least one value in the given range."""
    results = []
    for name, stats in heart_rate_samples.items():
        if any(low <= value <= high for value in stats):
            results.append(name)
    return results

def get_specific_stats_by_value(chosen_number, *values):
    patient_data = get_specific_stats(chosen_number, *values)
    return [v for v in patient_data if v in values]

while True:
    print("Patient Numbers:")
    for i, name in (enumerate(my_patient_list)):
        print(i)

    patient_number = int(input("Enter a Patient number: "))

    choice = input("Type 'all' for all the stats or 'specific' for a specific stats: ")

    if choice == "all":
            patient_name = my_patient_list[patient_number]
            stats = get_all_stats(patient_number)
            print("Patient Name", patient_name)
            print("Heart rate data", stats)

            again = input("Would you like to view more stats? (y/n):")
            if again == "y":
                continue

            if again == "n":
                break


    elif choice == "specific":

            print("Choose a range:")
            print("1. 65-70")
            print("2. 72-80")
            print("3. 82-90")
            print("4. 91-101")

            ranges = {
            "1": (65, 70),
            "2": (72, 80),
            "3": (82, 90),
            "4": (91, 101),
             }

            range_choice = input("Choose a range number: ")


            if range_choice in ranges:
                low, high = ranges[range_choice]
                matching_patients = get_patients_in_range(low, high)
                print("Patients in this range")
                for i, name in enumerate(matching_patients): print(f"{i}. {name}")



                patient_name = input("Enter a patient's name from this list: ")
                patient_number = get_patient_number_by_name(patient_name)
                stats = get_all_stats(patient_number)

                print("Patient Name", patient_name)
                print("Heart rate data", stats)

                again = input("Press 'Enter' to search again or 'n' to finish: ").lower()
                if again == "n":
                    break






























