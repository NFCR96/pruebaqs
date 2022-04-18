import streamlit as st

st.title('Bienvenido a Sexuapp')


def main():
    name = input("What is your name? ")
    correct = 0
    incorrect = 0
    ans = int(input("What is 4 + 5? "))
    val = add(4, 5)
    if(ans == val):
        correct + 1
    else:
        incorrect + 1
    ans2 = int(input("What is 20 * 6? "))
    val2 = mult(20, 6)
    if(ans2 == val2):
        correct + 1
    else:
        incorrect + 1
    ans3 = int(input("What is 14 - 10? "))
    val3 = sub(14, 10)
    if(ans3 == val3):
        correct + 1
    else:
        incorrect + 1
    ans4 = int(input("What is 30 / 5? "))
    val4 = div(30, 5)
    if(ans4 == val4):
        correct + 1
    else:
        incorrect + 1
    ans5 = int(input("What is 29 + 2? "))
    val5 = add(29, 2)
    if(ans5 == val5):
        correct + 1
    else:
        incorrect + 1
    ans6 = int(input("What is 50 - 10? "))
    val6= sub(50, 10)
    if(ans6 == val6):
        correct + 1
    else:
        incorrect + 1
    ans7 = int(input("What is 5 * 11? "))
    val7 = mult(5, 11)
    if(ans7 == val7):
        correct + 1
    else:
        incorrect + 1
    ans8 = int(input("What is 9 / 3? "))
    val8 = div(9, 3)
    if(ans8 == val8):
        correct + 1
    else:
        incorrect + 1
    ans9 = int(input("What is 90 - 5? "))
    val9 = sub(90, 5)
    if(ans9 == val9):
        correct + 1
    else:
        incorrect + 1
    ans10 = int(input("What is 412 + 5? "))
    val10 = add(412, 5)
    if(ans10 == val10):
        correct + 1
    else:
        incorrect + 1
    print()
    print("Thanks, " + str(name) + "!")
    print()
    print("Correct " + str(correct))
    print()
    print("Incorrect " + str(incorrect))
    print()
    calcGrade(correct)

  
