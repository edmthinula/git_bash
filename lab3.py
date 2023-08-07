#getting user input
user_marks = input("Enter marks : ")
marks = int(user_marks)
# cheking user input valide or not 
if marks < 100:
    if marks > 0: 
        # cheking grade of user inputed marks
        if marks < 40 :
            print("F")
            print("fail")
        elif marks < 55:
            print("s")
            print("ordinary pass")
        elif marks < 65:
            print("c")
            print("credit pass")
        elif marks < 75:
            print("B")
            print("good pass")
        else:
            print("A")
            print ("very good pass")
    else:
        print ("invalide marks")
else:
    print ("invalide marks")



