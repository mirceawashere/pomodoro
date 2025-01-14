import subprocess
import time


def start_timer(minutes):
                seconds = int(minutes) * 60  
                time.sleep(seconds)  
                return show_alert_with_osascript(f"So {minutes} minutes have passed, want to go another round?", "Nice!")

def show_alert_with_osascript(message, title="Alert"):
            script = f'display dialog "{message}" with title "{title}" buttons {{"Repeat", "Close"}} default button "Close"'
            result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True)
            button_clicked = result.stdout.strip().replace("button returned:", "").strip()
            return button_clicked

def show_input_with_osascript(message, title="Input", default_text=""):
    script = f'''
    display dialog "{message}" with title "{title}" default answer "{default_text}" buttons {{"OK", "Cancel"}} default button "OK"
    '''
    result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True)
    
    
    if "button returned:Cancel" in result.stdout:
        return None  
    
   
    user_input = result.stdout.split("text returned:")[1].strip()
    return user_input


user_response = show_input_with_osascript("Cate minute", "Name Input")
if user_response is None:
    print("User canceled the input.")
else:
    print(f"User entered: {user_response}")
    while True:
        button = start_timer(user_response)
        if button == "Close":
            break
    
        

 