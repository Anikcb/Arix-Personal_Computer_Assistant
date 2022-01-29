import sys
from Arix import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType


import speech_recognition as sr
from PyDictionary import PyDictionary
from pywikihow import search_wikihow
import pyttsx3 
import socket
import datetime
import wikipedia 
import webbrowser
import pywhatkit
import pyautogui
import pyjokes
import keyboard
from playsound import playsound
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    print("   ")
    engine.say(audio)
    print(f"{audio}")
    print("   ")
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-US')
        print(f"Anik: {query}\n")

    except Exception as e:
        print("I didn't get it, will you Say that again please...")  
        return "None"
    return query.lower()


def startup():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  
    time = datetime.datetime.now().strftime('%I:%M %p')   
    speak(f"the time is {time}")



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task()

    def Task(self):
        startup()
        while True:
            query = takeCommand()


            def checking(list_lst):
                for x in list_lst:
                    if x in query:
                        return True
                return False

            def sleep_mode():
                sleep_md=["go to sleep", "shutdown the program", "stop program",
                "quit program", "a break", 'bye', 'stop your program', 'quit your program', 'shutdown your program']
                return checking(sleep_md) == True


            def about_Arix():
                Arix_qu = ["about yourself", "who are you" ,"what are you"]
                return checking(Arix_qu)==True


            def searching():
                sea = ['search', 'find']
                return checking(sea)==True


            def question():
                sea = ['tell me', 'who', 'what is', 'where']
                return checking(sea)==True

            
            def computer_music(qur):
                dic = {"one": 0,"first": 0, "second": 1, "two": 1, "third": 2, "three": 2, "forth": 3, "four": 3, "fifth": 4, "five": 4}
                music = [ "second", "two", "third", "three", "forth", "four", "fifth", "five", "one", "first"]
                for x in music:
                    if x in qur:
                        return dic[x]
                return 0


            def open_softwares():

                if 'code blocks' in query:
                    Path = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                    speak("Opening codeblocks...")
                    os.startfile(Path)
                
                elif 'chrome' in query or 'open google' in query:
                    Path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    speak("Opening Google chrome...")
                    os.startfile(Path)

                elif 'eclipse' in query:
                    Path = "C:\\Users\\Anik Chakraborty\\eclipse\\java-2021-03\\eclipse\\eclipse.exe"
                    speak("Opening Eclipse...")
                    os.startfile(Path)

                elif 'code' in query:
                    Path = "C:\\Users\Anik Chakraborty\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    speak("Opening Visual Studio code...")
                    os.startfile(Path)

                elif 'photoshop' in query:
                    Path = "C:\\Program Files\\Adobe\Adobe Photoshop 2020\\photoshop.exe"
                    speak("Opening Adobe photoshop...")
                    os.startfile(Path)

                elif 'firefox' in query:
                    Path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    speak("Opening firefox...")
                    os.startfile(Path)

                elif 'notepad' in query:
                    Path = "notepad.exe"
                    speak("Opening Notepad...")
                    os.startfile(Path)

                elif 'cmd' in query:
                    Path = "cmd.exe"
                    speak("Opening command prompt...")
                    os.startfile(Path)

                elif 'facebook' in query:
                    speak("Opening facebook...")
                    webbrowser.open("https://www.facebook.com/profile.php?id=100030484703065")

                elif 'instagram' in query:
                    speak("Opening instagram...")
                    webbrowser.open("https://www.instagram.com/__.anik._/")

                elif 'github' in query:
                    speak("Opening github...")
                    webbrowser.open("https://github.com/Anikcb")

                elif 'portfolio' in query:
                    speak("Opening portfolio...")
                    webbrowser.open("https://anikcb.github.io/")

                elif 'linkedin' in query:
                    speak("Opening linkedin...")
                    webbrowser.open("https://www.linkedin.com/in/anik-chakraborty-b16243208")

                elif 'stack overflow' in query:
                    speak("Opening stackoverflow...")
                    webbrowser.open("https://stackoverflow.com/users/16171263/anik-chakraborty?tab=profile")

                elif 'kora' in query:
                    speak("Opening qoura...")
                    webbrowser.open("https://www.quora.com/profile/Anik-Chakraborty-47")


            def close_sotwares():
                speak("Ok sir...")
                
                if 'code blocks' in query:
                    os.system("TASKKILL /F /im codeblocks.exe")

                elif 'chrome' in query:
                    os.system("TASKKILL /F /im chrome.exe")

                elif 'eclipse' in query:
                    os.system("TASKKILL /F /im eclipse.exe")

                elif 'code' in query:
                    os.system("TASKKILL /F /im Code.exe")

                elif 'photoshop' in query:
                    os.system("TASKKILL /F /im photoshop.exe")

                elif 'firefox' in query:
                    os.system("TASKKILL /F /im firefox.exe")

                elif 'notepad' in query:
                    os.system("TASKKILL /F /im notepad.exe")

                elif 'cmd' in query:
                    os.system("TASKKILL /F /im cmd.exe")

                speak("Your Command has been completed sir")


            def dict():
                speak("Dictionary activated successfully.")
                while True:
                    speak("what do you want to know...")
                    word = takeCommand()
                    word = word.replace('what','')
                    word = word.replace('tell me','')
                    word = word.replace('is','')
                    word = word.replace('the','')
                    print(word)

                    if 'close' in word:
                        speak("Dictionary closed...")
                        break

                    elif 'meaning' in word:
                        word = word.replace('meaning','')
                        word = word.replace('of','')
                        word = word.replace(' ','')
                        mean = PyDictionary.meaning(word)
                        speak(f"The meaning for {word} is {mean}")
                    
                    elif 'synonym' in word:
                        word = word.replace('synonym','')
                        word = word.replace('of','')
                        word = word.replace(' ','')
                        syn = PyDictionary.synonym(word)
                        speak(f"The synonym of {word} is {syn}")

                    elif 'antonym' in word:
                        word = word.replace('antonym','')
                        word = word.replace('of','')
                        word = word.replace(' ','')
                        ant = PyDictionary.antonym(word)
                        speak(f"The antonym of {word} is {ant}")

                
            def validate_time(alarm_time):
                if len(alarm_time) != 8:
                    speak("Invalid HOUR format! Please try again.")
                    return False
                else:
                    if int(alarm_time[0:2]) > 12:
                        speak("Invalid HOUR format! Please try again.")
                        return False
                    elif int(alarm_time[3:5]) > 59:
                        speak("Invalid HOUR format! Please try again.")
                        return False
                    else:
                        speak("Ok")
                        return True
            

            def Hot_word():
                speak("Hello Sir, How can i help you??")




            if 'hello' in query or 'hey' in query:
                speak("Hello sir. How can I help you...")
             
            elif 'how are you' in query or 'how do you' in query:
                speak("I am Fine sir, how about you...")

            elif sleep_mode():
                if 'bye' in query:
                    speak("Ok sir, Bye. Glad to help you...")
                else:
                    speak("Ok sir, Have a good day...")
                sys.exit()

            elif 'thank you' in query:
                speak("you are most welcome. this is my job to help you....")

            elif 'good' in query:
                speak("Thank you sir...")

            elif about_Arix():
                speak("I am Arix. version 1.1. I am a computer program. I am helping Anik to work on his computer.")
            
            elif "play" in query and "youtube" in query:
                speak("playing your song on youtube.....")
                query = query.replace('play','')
                query = query.replace('youtube','')
                query = query.replace('on','')
                pywhatkit.playonyt(query)

            elif 'open youtube' in query:
                speak("What do you want me to search sir...")
                qur = takeCommand()
                qur = qur.replace('search','')
                qur = qur.replace(' ','+')
                web = 'https://www.youtube.com/results?search_query='+qur
                webbrowser.open(web)
                speak("Here you go sir...")

            elif searching():
                query = query.replace('search','')
                query = query.replace('find','')
                pywhatkit.search(query)
                speak("Done sir...")

            elif 'play music' in query:
                music_dir = 'D:\\A\\music'
                songs = os.listdir(music_dir)
                print(songs)
                speak("Which one you like to play...")
                qur = takeCommand()
                music = computer_music(qur)
                os.startfile(os.path.join(music_dir, songs[music]))

            elif 'send' in query and 'whatsapp' in query:
                speak("Tell me the number sir...")
                qur = takeCommand()
                hr = None
                mn = None

                while True:
                    speak("When do you want to send the message...")
                    time = takeCommand()
                    time = time.replace('.','')

                    if time[1]==':':
                        hr = time[0]
                        mn = time[2:4]
                        send_time = '0' + time
                    else:
                        hr = time[0:2]
                        mn = time[3:5]
                        send_time = time

                    print(f"valid Time: {send_time}")
                    if validate_time(send_time):
                        break

                
                speak("And the message is....")
                qur1 = takeCommand()
                qur = qur.replace(' ','')
                speak("Ok sir, the message will be send in time...")
                pywhatkit.sendwhatmsg("+880"+qur, qur1, int(hr), int(mn),20)
                keyboard.press_and_release("Enter")
                speak("Done Sir...")

            elif 'screenshot' in query:
                speak("And the file name would be...")
                name = takeCommand()
                pyautogui.screenshot(f"D:\\Anik\\Screenshot\{name}.png")
                speak("The screenshot has been taken sir, check this out")
                os.startfile("D:\\Anik\\Screenshot")

            elif 'open code blocks' in query:
                open_softwares()
                
            elif 'open chrome' in query or 'open google' in query:
                open_softwares()

            elif 'open eclipse' in query:
                open_softwares()

            elif 'open code' in query:
                open_softwares()

            elif 'open photoshop' in query:
                open_softwares()
                
            elif 'open firefox' in query:
                open_softwares()

            elif 'open notepad' in query:
                open_softwares()

            elif 'open cmd' in query:
                open_softwares()

            elif 'open facebook' in query:
                open_softwares()

            elif 'open instagram' in query:
                open_softwares()

            elif 'open github' in query:
                open_softwares()

            elif 'open portfolio' in query:
                open_softwares()

            elif 'open linkedin' in query:
                open_softwares()

            elif 'open stack overflow' in query:
                open_softwares()

            elif 'open kora' in query:
                open_softwares()

            elif 'close code blocks' in query:
                close_sotwares()

            elif 'close' in query and 'chrome' in query:
                close_sotwares()

            elif 'close eclipse' in query:
                close_sotwares()

            elif 'close code' in query:
                close_sotwares()

            elif 'close photoshop' in query:
                close_sotwares()

            elif 'close firefox' in query:
                close_sotwares()

            elif 'close notepad' in query:
                close_sotwares()

            elif 'close cmd' in query:
                close_sotwares()

            elif 'are you there' in 'are you listening' in query:
                speak("Yes sir, i am Listening...")
            
            elif 'how dare you' in query:
                speak("I am sorry, if i did something wrong...")

            elif 'ip address' in query:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                speak(f"sir, your ip address is:{ip_address}")

            elif 'pause' in query or 'play' in query:
                if 'pause' in query:
                    speak("ok sir, pausing the video....")
                    keyboard.press('k')
                else:
                    speak("ok sir, playing the video....")
                    keyboard.press('k')

            elif 'restart' in query:
                speak("Restarting the video....")
                keyboard.press('0')

            elif 'mute' in query or 'unmute' in query:
                if 'unmute' in query:
                    keyboard.press('m')
                else:
                    keyboard.press('m')
                    speak("The video has been muted....")

            elif 'keep' in query:
                speak("Skiping 10 second....")
                keyboard.press('l')

            elif 'back' in query:
                keyboard.press('j')

            elif 'full screen' in query or 'normal' in query:
                speak("Ok sir...")
                keyboard.press('f')

            elif 'film mode' in query:
                speak("Ok sir....")
                keyboard.press('t')

            elif 'reopen' in query and 'tab' in query:
                keyboard.press_and_release("Ctrl + Shift + t")

            elif 'close' in query and 'tab' in query:
                speak("Closing the tab...")
                keyboard.press_and_release("Ctrl + w")

            elif 'new tab' in query:
                speak("Opening new tab...")
                keyboard.press_and_release("Ctrl + t")

            elif 'history' in query:
                speak("Here is your history...")
                keyboard.press_and_release("Ctrl + h")

            elif 'next tab' in query:
                speak("Ok sir...")
                keyboard.press_and_release("Ctrl + Tab")
            
            elif 'previous tab' in query:
                speak("Ok sir...")
                keyboard.press_and_release("Ctrl + Shift + Tab")

            elif 'last tab' in query:
                keyboard.press_and_release("Ctrl + 9")
                speak("It's the last tab sir...")
            
            elif 'download' in query:
                speak("Here is your downloading history sir...")
                keyboard.press_and_release("Ctrl + j")
            
            elif 'search now' in query:
                keyboard.press_and_release("Ctrl + k")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            elif 'dictionary' in query:
                dict()

            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')   
                speak(f"Sir, the time is {time}")

            elif 'date' in query:
                today = datetime.date.today()
                speak(f"The Date is: {today}")
            
            elif 'how to' in query:
                speak("Getting data from Internet: ")
                op = query.replace('tell me','')
                op = op.replace('show me', '')
                max_result = 1
                func = search_wikihow(op,max_result)
                assert len(func) == 1
                speak(func[0].summary)

            elif question():
                query = query.replace('who is','')
                query = query.replace('what is','')
                query = query.replace('tell me','')
                query = query.replace('about','')

                try:
                    pywhatkit.search(query)
                    results = wikipedia.summary(query, sentences=1)
                    speak(results)
                except:
                    speak("No speakable data vailable...")
            
            elif 'alarm' in query:
                
                while  True:
                    speak("Give me the time sir...")
                    time = takeCommand()
                    time = time.replace('.','')

                    if time[1]==':':
                        alarm_time = '0' + time
                    else:
                        alarm_time = time

                    print(f"valid Time: {alarm_time}")
                    if validate_time(alarm_time):
                        break
                    

                alarm_hour = alarm_time[0:2]
                alarm_min = alarm_time[3:5]
                alarm_period = alarm_time[6:].upper()

                while True:
                    now = datetime.datetime.now()
                    current_hour = now.strftime("%I")
                    current_min = now.strftime("%M")
                    current_period = now.strftime("%p")
                    if alarm_period == current_period:
                        if alarm_hour == current_hour:
                            if alarm_min == current_min:
                                speak("Time to wake up sir...")
                                music_dir2 = 'C:\\Users\\Anik Chakraborty\\Helloworld\\music'
                                songs1 = os.listdir(music_dir2)
                                os.startfile(os.path.join(music_dir2, songs1[0]))
                                break

            elif 'window' in query and 'first' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 1')

            elif 'window' in query and 'second' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 2')
            
            elif 'window' in query and 'third' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 3')

            elif 'window' in query and '4th' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 4')

            elif 'window' in query and 'fifth' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 5')
            
            elif 'window' in query and 'sixth' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 6')

            elif 'window' in query and 'seventh' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 7')

            elif 'window' in query and 'eighth' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 8')

            elif 'window' in query and 'nineth' in query:
                speak("Okay sir...")
                keyboard.press_and_release('windows + 9')

            elif 'close' in query and 'folder' in query:
                speak("Closing the folder...")
                keyboard.press_and_release("Ctrl + spacebar + w")

            elif 'select' in query:
                keyboard.press_and_release("Ctrl + spacebar")
                speak("Selected...")

            elif "hide the files" in query or "hide this folder" in query:
                os.system("attrib +h /s /d")
                speak("All the files are now hidden!!!!!!")

            elif "show" in query and "file" in query:
                os.system("attrib -h /s /d")
                speak("Done sir....")
            

            elif 'enter' in query or 'show' in query:
                speak("Ok,sir...")
                keyboard.press_and_release("Enter")

            elif 'minimise all window' in query:
                speak("Okay sir!")
                keyboard.press_and_release("windows + m")
            
            elif 'next' in query or 'right' in query:
                speak("Okay...")
                keyboard.press_and_release("Right")

            elif 'previous' in query or 'left' in query:
                speak("Okay....")
                keyboard.press_and_release('Left')
            
            elif 'up' in query:
                speak("Okay....")
                keyboard.press_and_release('Up')

            elif 'down' in query:
                speak("Okay....")
                keyboard.press_and_release('Down')

            elif 'first image' in query:
                speak("Okay....")
                keyboard.press_and_release('Alt + Home')
            
            elif 'last image' in query:
                speak("Okay....")
                keyboard.press_and_release('Alt + End')

            elif 'rotate' in query:
                speak("Okay....")
                keyboard.press_and_release('Ctrl + R')

            elif 'close' in query:
                speak("Okay...")
                keyboard.press_and_release('Alt + F4')
            
            elif 'drive' in query:
                speak("Opening D-drive...")
                os.startfile("D:\\")

            elif "switch the window" in query or "switch window" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


    
            

startExecution = MainThread()

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__


    def startTask(self):

        self.ui.movie = QtGui.QMovie("run.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("heart.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("anik.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()



app = QApplication(sys.argv)
Arix = UI()
Arix.show()
exit(app.exec_())