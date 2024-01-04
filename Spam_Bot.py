import pyautogui, time

validIn = False
pyautogui.FAILSAFE = True

#input validation
while (validIn == False):
    x = int(input('Enter number of messages: '))
    message = input('What message would you like to send: ')

    #Makes sure that the number of messages or characters in each message are not too large
    if (x > 1000 or x < 1):
        print("Please enter a number between  and 1000")
        validIn = False
    if (len(message) > 100):
        print("Too many characters. Please use less than 100")
        validIn = False
    else:
        validIn = True
    
#Gives the user time to switch tabs
print("Go to the text field. The messages will send in 30 seconds")
time.sleep(30) 

#displays the messages
for i in range(x):
    
    pyautogui.write(message)  
    pyautogui.press("enter") 

print("Messages successfully sent")






