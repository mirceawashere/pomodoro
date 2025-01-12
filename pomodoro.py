import subprocess
import time


def start_timer(minutes):
                seconds = int(minutes) * 60  # Convert minutes to seconds
                print(f"Timer started for {minutes} minutes...")
                time.sleep(seconds)  # Wait for the specified time
                return show_alert_with_osascript(f"Au trecut {minutes} minute, mai bagi o tura?", "Bine bo$$!")

def show_alert_with_osascript(message, title="Alert"):
            script = f'display dialog "{message}" with title "{title}" buttons {{"Repeta", "Inchide"}} default button "Inchide"'
            result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True)
            button_clicked = result.stdout.strip().replace("button returned:", "").strip()
            return button_clicked

def show_input_with_osascript(message, title="Input", default_text=""):
    script = f'''
    display dialog "{message}" with title "{title}" default answer "{default_text}" buttons {{"OK", "Cancel"}} default button "OK"
    '''
    result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True)
    
    # Check if user pressed "Cancel"
    if "button returned:Cancel" in result.stdout:
        return None  # User canceled
    
    # Extract the user input
    user_input = result.stdout.split("text returned:")[1].strip()
    return user_input

# Example usage
user_response = show_input_with_osascript("Cate minute", "Name Input")
if user_response is None:
    print("User canceled the input.")
else:
    print(f"User entered: {user_response}")
    while True:
        button = start_timer(user_response)
        if button == "Inchide":
            break
    
        

 