#File: chaoes.py
#a simple program

def main():
    print("this is a problem")
    x = eval(input("Enter a number between 0 to 1"))
    for i in range(10):
        x = 3.9*x*(1-x)
        print(x)





main()
