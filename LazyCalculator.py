import requests
import time
import socket
#internet check
try:
    socket.setdefaulttimeout(2)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
except: #No internet access
    print("ERROR: ")
    print("Without internet i can't get the joke from the internet so please get an internet connection and restart the program, thanks")
    exit()
#internet check passed

try:
    A = int(input("Enter the first number: ")) #ask the user to input the numbers
    B = int(input("Enter the second number: "))
    print("Loading...") 
    error = requests.get("https://naas.isalman.dev/no") #gets the joke form the api (you can also visit the link in a browser)
    print("Error: ")
    print(error.json()["reason"]) #Print the joke into the terminal
    time.sleep(2)   
    result = A + B   #actually calculate the result
    print(f"it's {result} Btw") 
    time.sleep(2)
    exit()
except ValueError:#if the user doesn't input a number
    print("You need to put a number when i ask for a number") 
    time.sleep(5)
    exit()

#Suggestion for this code are wellcome!
#Script by Alessio1009