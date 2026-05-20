tasks = []
while True :
    print ("What would you like to do?\n")
    print('1. Add task \n')
    print('2. View task \n')
    print('3. Delete task \n')
    print("4. Mark as done \n")
    print('5. Quit')
    while True:
        try:
            n= int(input("Pick a choice 1 ,2 ,3, 4 or 5: "))
            if n not in [1,2,3,4,5]:
                
                print("Please enter a valid answer: ")
            else:
                break
        except:
            print("Enter a number!")
    if n ==1 :
         while True:
            task=input("Enter a task (or 'done' to stop) : ")
            if task == 'done':
                break               
            tasks.append(task)
    elif n ==2 :
        for i, task in enumerate(tasks, 1):
            print(f"{i}, {task}")     
    elif n==3:
        for i, task in enumerate(tasks, 1):
            print(f"{i}, {task}")
        z = int(input("Which task would you like to delete?: "))
        tasks.pop(z-1)
    elif n==4:
        for i, task in enumerate(tasks, 1):
            print(f"{i}, {task}")
        z = int(input("Which task would you like to mark as done?: "))
        tasks[z-1] = tasks[z-1] + " ✅"
    else:
        break

