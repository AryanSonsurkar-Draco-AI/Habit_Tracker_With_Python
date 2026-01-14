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
    pass

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

if __name__=="__main__":
    main()