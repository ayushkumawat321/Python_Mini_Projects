def length():
    units = {
        "m":1,
        "km":1000,
        "cm":0.01,
        "mm":0.001,
        "mi":1609.35,
        "ft":0.3048,
        "in":0.0254
    }
    value = float(input("Enter value: "))
    from_unit = input("From unit (m,km,cm,mm,mi,ft,in): ")
    to_unit =  input("To unit (m,km,cm,mm,mi,ft,in): ")
    meter = value * units[from_unit]
    result = meter / units[to_unit]
    print(f"{value} {from_unit} --> {result} {to_unit}")

def weight():
    units = {
        "kg":1,
        "g" :0.001,
        "mg":0.000001,
        "lb":0.453592,
        "oz":0.0283495
    }
    value = float(input("Enter value: "))
    from_unit = input("From unit (kg,g,mg.lb.oz): ")
    to_unit =  input("To unit (kg,g,mg.lb.oz): ")
    kg = value * units[from_unit]
    result = kg / units[to_unit]
    print(f"{value} {from_unit} --> {result} {to_unit}")

def temp():
    value = float(input("Enter value: "))
    from_unit = input("From unit (F,C,K): ")
    to_unit =  input("To unit (F,C,K): ")
    # convert to celsius
    match from_unit:
        case "F":
            celsius = (value - 32) * (5/9)
        case "K":
            celsius = value - 273.15
        case "C":
            celsius = value
        case _:
            print("Invalid choice !")
    #convert from celsius
    match to_unit:
        case "F":
            result = (celsius * 9/5) + 32
        case "K":
            result = celsius + 273.15
        case "C":
            result = celsius
        case _:
            print("Invalid choice !")

    print(f"{value} {from_unit} --> {result} {to_unit}")


while True:
    print("---------------------------------------------------")
    print("UNIT CONVERTER :-")
    print("---------------------------------------------------")
    print("1.Length")
    print("2.Weight")
    print("3.Temperature")
    print("4.Exit")
    choice = int(input("Enter Your Choice : "))
    print("---------------------------------------------------")
    if(choice==1):
        length()
    elif(choice==2):
        weight()
    elif(choice==3):
        temp()
    elif(choice==4):
        print("Exiting......")
        break
    else:
        print("Invalid Choice !!!")
    