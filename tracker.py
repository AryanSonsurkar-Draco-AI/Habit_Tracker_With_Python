import json
import os
def add_habit():
    habit = input("Enter Habit: \n").strip()
    if not os.path.exists("habits.json"):
        data={}
    else:
        with open("habits.json","r") as file:
            data = json.load(file)
    
    if habit in data:
        print("This is already in habits list.")
        return
    
    data[habit] = {
        "streak": 0,
        "done_today": False
    }

    with open("habits.json","w") as file:
        json.dump(data,file,indent=4)
    print("habit added successfully!!!")
        
def mark_done():
    if not os.path.exists("habits.json"):
        print("No habits found!")
        return
    
    with open("habits.json","r")as file:
        data = json.load(file)

    habit = input("Enter habit name: ").strip()
    if habit not in data:
        print("Habit not found!")

    if data[habit]["done_today"]:
        print("Habit already marked  done today!")
        return
    
    data[habit]["done_today"] = True
    data[habit]["streak"] += 1

    with open("habits.json","w")as file:
        json.dump(data,file,indent=1)
    print("Habit marked done!!!")

def check_status():
    if not os.path.exists("habits.json"):
        print("No habits found!")

    with open("habits.json","r")as file:
        data = json.load(file)

    print("\nHabit Status: ")
    for habit, info in data.items():
        status = "Done" if info["done_today"] else "Not Done!!!"
        print(f"{habit} | Streak: {info['streak']} | {status}")

def main():
    print("------------------------------")
    print("Welcome to Habit Tracker (CLI)")
    print("------------------------------")
    
    while True:
        print("1.Add Habit")
        print("2.Mark done")
        print("3.check status")
        print("4.Exit")
        choice=input("Enter your choice: ")

        if choice=="4":
            print("Good Bye!!!")
            break
        
        elif choice=="1":
            add_habit()

        elif choice=="2":
            mark_done()

        elif choice=="3":
            check_status()

        else:
            print("Invalid Choice")
            continue

if __name__=="__main__":
    main()