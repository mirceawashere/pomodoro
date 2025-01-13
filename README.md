# my own version of pomodoro, with macos alerts 

## needs code cleanup


the idea is to use it as an executable file in mac

for this:

*1*. create a new file pomo.command on ur desktop

*2*. pomo.command should have one line: 

> wget -qO- https://raw.githubusercontent.com/mirceawashere/pomodoro/main/pomodoro.py | python3

*3*. in terminal use this line to make it executable: 
 
> chmod +x pomo.command to make it executable. 

*4*. voilla, should work.