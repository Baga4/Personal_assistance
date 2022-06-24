import time
import androidhelper.sl4a as android

def speak (content):
    droid=android.Android ()
    print (content)
    droid.ttsSpeak(content)

def AppendName():
    speak (f"Do you want to change your name ?")
    con=input("Yes / No - ").lower ().capitalize ()
    if con=="Yes":
        pass
    
    if user_name=="":
        speak ("\nFirst of all set your nickname")
        speak ("\nYou can change your nickname any time by just saying  'change my name'")
        speak ("\nwhat shall I call you? ")
        name=input ("- ")
        speak (f"\nYour name is {name} is it right")
        conform=input ("Yes / No  - ").capitalize ()
        
        if conform=="Yes" or "Done" or "Good" or "ok":
            user_name.append (name)
            speak (f"okay i will call you {user_name} now on")
            speak ("Any other thing i can do for you")
        elif conform=="No":
            speak ("Try again typing your name ")
            Run (input ("•°○"))
        

def Run (command):
    """This function is the main function to recognize the user command and answering them """
    # Change name possibility
    if "change my name" in command:
        AppendName() 
        
    elif "hy" in command:
        speak (f"hello {user_name}")
        
    elif "my name " or "say my name " in command:
        speak (f"your name is {user_name[0]} ")
        
        
    else:
        speak("Shut your fucking mouth ")   



if __name__=="__main__":
    speak ("Hey..\n")
    user_name=['Juice wrld']
    speak ("How can i help you")
    while (True):
        Arguments=input("\n○•° ").lower ()
        
        #Running main function to communicate
        Run (Arguments)
        
             
        
    
        
