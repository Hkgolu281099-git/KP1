class Hospital:
    def __init__(self):
        self.patients = {}      # Dictionary
        self.appointments = []  # List
        self.discharged = set() # Set

    # Patient Registration
    def register_patient(self, pid, name, age, gender, contact):
        self.patients[pid] = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Contact": contact,
            "Medical_Record": []
        }
        print("Patient registered successfully.")


    # Appointment Booking
    def book_appointment(self, pid, doctor, date):
        appointment = (pid, doctor, date)  # Tuple
        self.appointments.append(appointment)
        print("Appointment booked.")

    # Add Medical Record
    def add_medical_record(self, pid, diagnosis, medicine):
        record = {"Diagnosis": diagnosis, "Medicine": medicine}
        self.patients[pid]["Medical_Record"].append(record)
        print("Medical record added.")

    # Discharge Patient
    def discharge_patient(self, pid):
        self.discharged.add(pid)
        print("Patient discharged successfully.")

    # Search Patient History
    def search_patient(self, pid):
        if pid in self.patients:
            print("\nPatient Details:")
            for key, value in self.patients[pid].items():
                print(f"{key}: {value}")
        else:
            print("Patient not found.")


# Main Program
hospital = Hospital()

while True:
    print("\n--- Hospital Patient Management System ---")
    print("1. Register Patient")
    print("2. Book Appointment")
    print("3. Add Medical Record")
    print("4. Discharge Patient")
    print("5. Search Patient")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Patient ID: ")
        name = input("Name: ")
        age = input("Age: ")
        gender = input("Gender: ")
        contact = input("Contact: ")
        hospital.register_patient(pid, name, age, gender, contact)

    elif choice == "2":
        pid = input("Patient ID: ")
        doctor = input("Doctor Name: ")
        date = input("Appointment Date: ")
        hospital.book_appointment(pid, doctor, date)

    elif choice == "3":
        pid = input("Patient ID: ")
        diagnosis = input("Diagnosis: ")
        medicine = input("Medicine: ")
        hospital.add_medical_record(pid, diagnosis, medicine)

    elif choice == "4":
        pid = input("Patient ID: ")
        hospital.discharge_patient(pid)

    elif choice == "5":
        pid = input("Patient ID: ")
        hospital.search_patient(pid)

    elif choice == "6":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")


