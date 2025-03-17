import qrcode
import yagmail
import webbrowser
from datetime import datetime
import random
from PIL import Image
import os

class information:

    def report_missing_person(self):
        name = input("Enter the name of the missing person: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender (Male/Female): ")
        last_seen = input("Enter last seen location: ")

        while True:
            contact = input("Enter contact number (10 digits): ").strip()
            if not(contact.isdigit() and len(contact) == 10):
                print(" Invalid contact number! Please enter a 10-digit number: ")
            else:
                break

        while True:
            date_input = input("Enter date (DD-MM-YYYY): ").strip()
            try:
                valid_date = datetime.strptime(date_input, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date! Please enter in the format DD-MM-YYYY.")

        while True:
            time_input = input("Enter time (HH:MM in 24-hour format): ").strip()

            try:
                valid_time = datetime.strptime(time_input, "%H:%M")
                break
            except ValueError:
                print("Invalid time! Please enter in the format HH:MM (24-hour format).")
    
        while True:
            image_path = input("Enter the image file name (e.g., person.jpg): ").strip()
            if os.path.exists(image_path):  # Check if file exists
                print("Image added successfully!")
                break
            else:
                print("Error: Image not found! Please enter a valid file name.")

        # Report Data
        report = f"""
        ----------------------------------------
                    MISSING REPORT  
        ----------------------------------------
        Name : {name}
        Age : {age}
        Gender : {gender}
        Contact Number : {contact}
        Last Location : {last_seen}
        Missing Date : {date_input}
        Missing Time : {time_input}
        Status = "Missing"
        Image Path : {image_path}
        ----------------------------------------
        """

        otp = self.send_email_alert(name)
        with open(f"Missing_People\\{name}.txt","w") as file:
            file.write(report + "\n")
        with open("list_of_names.txt","a") as file:
            file.write(name + " - " + str(otp) + "\n")
        

    
    def send_email_alert(self,name):

        receiver_email = input("Enter the recipient's email (e.g., police@example.com): ")
        subject = f'Missing Person Alert: {name}'
        otp = random.randint(1000, 9999)
        body = f"Hello {receiver_email.split('@')[0]},\n\nYour verification code is: {otp}\n\nWhen this person is found, you will need this OTP to change their status from 'Missing' to 'Found'.\nPlease do not share this code with anyone for security reasons.\n\nRegards,\nMissing Persons Alert System"

        sender_email = "pariii2104@gmail.com"  # Change this to your email
        sender_password = "ddue bzwi lpfg vktm"  # Use an App Password for security

        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(to=receiver_email, subject=subject, contents=body)
        
        print("Email alert sent successfully!")
        return otp


    
    def display_missing_persons(self):
        with open("list_of_names.txt","r") as file:
            r = file.readlines()
        j = []
        for i in r:
            j.append(i.split("-")[0].strip())
        for name in j:
            print(name)



    def search_missing_person(self):
        search_name = input("\nEnter the name of the missing person: ")

        with open("list_of_names.txt","r") as file:
            f = file.read()

        if search_name in f:
            with open(f"Missing_People\\{search_name}.txt","r") as file:
                r = file.readlines()
            for i in r:
                if i.startswith("        Image Path"):
                    image_path = i.split(":")[-1].strip()  # Extract image path
                    try:
                        img = Image.open(image_path)  # Open the image
                        img.show()  # Display the image
                    except FileNotFoundError:
                        print("⚠️ Error: Image file not found!")
                    except Exception as e:
                        print(f"⚠️ Error: Unable to open image. {e}")
                    return  # Exit function after displaying the image
                else:
                    print(i)
            
        else:
            print("Missing report not found!")

        

    def update_missing_status(self):
        name = input("Enter the name of the person to update status: ")

        with open("list_of_names.txt","r") as file:
            r = file.readlines()
        j = []
        for i in r:
            j.append(i.split("-")[0].strip())
            
        if name in j:
            with open(f"Missing_People\\{name}.txt","r+") as file:
                f = file.readlines()
                f.remove(f[-1])
                print("What would you like to update?")
                print("1. Update Status (Found/Missing)")
                print("2. Update Last Seen Location")
                print("3. Update Both")
                choice = int(input("Enter your choice (1/2/3): "))

                if choice == 1:
                    ind = j.index(name)
                    otp = int(r[ind].split("-")[-1].strip())
                    o = int(input("Enter otp: "))
                    if(o == otp):
                        new_status = input("Enter new status (Found/Missing): ").strip()
                        f[11] = f'        Status = "{new_status}"\n'
                        if new_status.lower() == "found":
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date & time
                            f.append(f'        Found Timestamp : "{timestamp}"\n')
                            r.remove(name +" - "+str( otp)+"\n")
                            with open("list_of_names.txt", "w") as f1:
                                f1.writelines(r)

                            with open("found_people.txt", "a") as f2:
                                f2.write(name+"\n")

                            print(f"{name} has been marked as 'Found' and moved to found_people.txt!")
                    else:
                        print("Wrong otp!")

                elif choice == 2:
                    new_location = input("Enter last seen location: ").strip()
                    f[8] = f'        Last Seen Location : "{new_location}"\n'
                    while True:
                        date_input = input("Enter last seen date (DD-MM-YYYY): ").strip()
                        try:
                            valid_date = datetime.strptime(date_input, "%d-%m-%Y")
                            break
                        except ValueError:
                            print("Invalid date! Please enter in the format DD-MM-YYYY.")

                    while True:
                        time_input = input("Enter last seen time (HH:MM in 24-hour format): ").strip()

                        try:
                            valid_time = datetime.strptime(time_input, "%H:%M")
                            break
                        except ValueError:
                            print("Invalid time! Please enter in the format HH:MM (24-hour format).")
                    f.append(f'        Last Seen Date : "{date_input}"\n')
                    f.append(f'        Last Seen Time : "{time_input}"\n')

                elif choice == 3:
                    ind = j.index(name)
                    otp = int(r[ind].split("-")[-1].strip())
                    o = int(input("Enter otp: "))
                    if(o == otp):
                        new_status = input("Enter new status (Found/Missing): ").strip()
                        new_location = input("Enter last seen location: ").strip()
                        f[11] = f'        Status : "{new_status}"\n'
                        f[8] = f'        Last Seen Location : "{new_location}"\n'
                        while True:
                            date_input = input("Enter last seen date (DD-MM-YYYY): ").strip()
                            try:
                                valid_date = datetime.strptime(date_input, "%d-%m-%Y")
                                break
                            except ValueError:
                                print("Invalid date! Please enter in the format DD-MM-YYYY.")

                        while True:
                            time_input = input("Enter last seen time (HH:MM in 24-hour format): ").strip()

                            try:
                                valid_time = datetime.strptime(time_input, "%H:%M")
                                break
                            except ValueError:
                                print("Invalid time! Please enter in the format HH:MM (24-hour format).")
                        f.append(f'        Last Seen Date : "{date_input}"\n')
                        f.append(f'        Last Seen Time : "{time_input}"\n')
                        if new_status.lower() == "found":
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date & time
                            f.append(f'        Found Timestamp : "{timestamp}"\n')
                            r.remove(name +" - "+str( otp)+"\n")
                            with open("list_of_names.txt", "w") as f1:
                                f1.writelines(r)

                            with open("found_people.txt", "a") as f2:
                                f2.write(name + "\n")

                            print(f"{name} has been marked as 'Found' and moved to found_people.txt!")
                    else:
                        print("Wrong otp!")

                else:
                    print("Invalid choice. Enter valid choise!")

                f.append("        ----------------------------------------")
                file.seek(0)
                file.writelines(f)
        else:
            print("Missing report not found!")


    
    def view_last_seen_location(self):
        with open("list_of_names.txt","r") as file:
            r = file.read()

        search_name = input("Enter the name of the missing person: ")

        if search_name in r:
            with open(f"Missing_People\\{search_name}.txt","r") as file:
                f = file.readlines()
                location = f[8].split(":")[-1].replace(" ", "+")  # Format location for URL
                google_maps_url = f"https://www.google.com/maps/search/?api=1&query={location}"
                webbrowser.open(google_maps_url)
                print("Opening last seen location on Google Maps...\n")
                return

        print("Person not found!")



    def generate_qr_code(self):
        with open("list_of_names.txt","r") as file:
            r = file.read()

        search_name = input("Enter the name of the missing person: ")

        if search_name in r:
            with open(f"Missing_People\\{search_name}.txt","r") as file:
                f = file.readlines()
                age = f[5].split(":")[-1].strip()
                ls = f[8].split(":")[-1].strip()
                s = f[11].split(":")[-1].strip()
                c = f[7].split(":")[-1].strip()
                

                qr_data = f"Name: {search_name}\nAge: {age}\nLast Seen: {ls}\nStatus: {s}\nContect: {c}"
                qr = qrcode.make(qr_data)
                qr_filename = f"{search_name.replace(" ","_")}_QR.png"
                qr.save(qr_filename)
                print(f"QR Code generated successfully! Saved as '{qr_filename}'.")
                return

        print("Person not found!")



i = information()



while True:
    print("===============================")
    print("Track them")
    print("1️. Report Missing Person")
    print("2️. Display Missing Persons")
    print("3️. Search for a Missing Person")
    print("4️. Update Missing Person's Status")
    print("5️. Generate QR Code for Missing Person")
    print("6️. View Last Seen Location on Map")
    print("7. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        i.report_missing_person()
    elif choice == "2":
        i.display_missing_persons()
    elif choice == "3":
        i.search_missing_person()
    elif choice == "4":
        i.update_missing_status()
    elif choice == "5":
        i.generate_qr_code()
    elif choice == "6":
        i.view_last_seen_location()
    elif choice == "7":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("\n Invalid choice! Please enter a number between 1 and 7.\n")
