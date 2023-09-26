print("On This Calculator Version You Can Add, Subtract, Divide, Multiply, Find The Area Of a Shape, Find The Volume of a 3D Shape, And Check Formulae. More Options To Come Out In Later Updates...")

variable1= input("Password:")
while variable1=="apple":

    question1=input("What Type Of Mathematical Calculation Would You Like Me To Figure Out? E.g Addition ---> ")
        #Basic (Operations)
    if question1 == "addition" or question1 =="add" or question1 =="+":
            num1 = float (input("What is your first number? "))
            num2 = float (input("What is your second number? "))
            print(num1+num2)
    if question1 == "subtraction" or question1 == "sub" or question1 == "-":
            num1 = int(input("What is your first number? "))
            num2 = int(input("What is your second number? "))
            print(num1-num2)
    if question1 == "multiplication" or question1 == "multiply" or question1 == "times" or question1 == "x" or question1 == "*":
            num1 = int(input("What is your first number? "))
            num2 = int(input("What is your second number? "))
            print (num1*num2)
    if question1 == "division" or question1 == "divide" or question1== "/":
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        print(num1/num2)
        #Area
    if question1 == "area":
        question2=input("Of What(2D) Shape? ")
        if question2 == "square":
            num1 = int(input("What is your base? "))
            print(num1*4,"cm²")
        if question2 == "rectangle":
            num1 = int(input("What is your base? "))
            num2 = int(input("What is your height? "))
            print(num1*num2,"cm²")
        if question2 == "triangle":
            num1 = int(input("What is your base? "))
            num2 = int(input("What is your height? "))
            print(num1*num2/2,"cm²")
        if question2 == "circle":
            num1 = int(input("What is your radius? "))
            print(3.1415926535*num1**2,"cm²")
        if question2 == "trapezoid":
            num1 = int(input("What is your base length? "))
            num2 = int(input("What is your base width? "))
            num3 = int(input("What is your height? "))
            print(1/2*(num1+num2)*num3,"cm²")                                       
        #Volume            
    if question1 == "volume":
        question3=input("Of What(3D) Shape? ")
        if question3 == "cube":
            num1 = int(input("What is your length? "))
            print(num1**3,"cm³")
        if question3 == "cuboid":
            num1 = int(input("What is your width? "))
            num2 = int(input("What is your length? "))
            num3 = int(input("What is your height? "))
            print(num1*num2*num3,"cm³")
        if question3 == "cylinder":
            num1 = int(input("What is your radius? "))
            num2 = int(input("What is your height? "))
            print(3.1415926535*num1**2*num2,"cm³")
        if question3 == "sphere":
            num1 = int(input("What is your radius? "))
            print(4/3*3.1415926535*num1**3,"cm³")
        if question3 == "cone":
            num1 = int(input("What is your radius? "))
            num2 = int(input("What is your height? "))
            print(3.1415926535*num1**2*num2/3,"cm³")
        if question3 == "pyramid":
            num1 = int(input("What is your base length? "))
            num2 = int(input("What is your base width? "))
            num3 = int(input("What is your height? "))
            print(num1*num2*num3/3,"cm³")
        #Formulae        
    if question1 == "formulae" or question1 == "formulas" or question1 =="formula":
        question4 = input("For What Named Equation? ")
        if question4 == "linear line" or question4 =="a linear line":
            print("The Formula for a Linear Line is y=mx+c")
        if question4 == "pythagoras theorem" or question4 == "pythagoras' theorem" or question4 == "pythagoras":
            print("a²+b²=c²")
        if question4 == "energy":
            print("E=mc² (Energy=Mass x The Speed Of Light²)")
        if question4 == "quadratic" or question4 =="quadratic formula":
            print("x=−b±√b²-4ac/2a")
        if question4 == "compound interest":
            print("A=P(1 + r/n)^nt A=final Amount P=Initial Principal Balance R=Interest Rate N=Number Of Compounding Periods Per Unit of Time T=Time In Decimal Years; e.g., 6 Months Is Calculated As 0.5 Years")
        if question4 =="voltage" or question4 == "volts":
            print("V=IR")
        #Easter Eggs
    if question1 == "gaster":
        print("It's rude to talk about someone who's listening...")
    if question1 == "Gaster":
        print("have you ever thought of a world where everything is exactly the same...")
    if question1 =="W.D Gaster":
        print("an umbrella...?")
        print("but its not raining.")
    if question1 =="W.D gaster":
        print("I can't imagine what Doctor Gaster must be going through. Being forced to watch over a world in which you don't exist... Thinking about that terrifies me.")
    if question1 =="help":
        print("You Called For Help")
        print("...")
        print("But Nobody Came.")
    if question1 =="wd":
        print("WD{Redacted}")
                      
            
            






else:
    print("DENIED")
   
    
