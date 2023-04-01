# Doubt-Submission
A Simple Doubt Submission Software made using flask.

A Simple Doubt Submmission application that notifies me, that someone has posted a doubt via 'notify-send' commans in Linux.
Note: This feature might break the app on several systems so please remove the 'notify_send' function and its calls if this dependency can't be fulfilled.

[https://github.com/vaskovsky/notify-send](Click here to install the Dependency on Windows)
For Mac OS:
Please the Subprocess command should be this 
```bash
osascript -e 'display notification "hello world!"'
```

So the line 41 after change will be something like this :
```python
p = subprocess.Popen(['osascript', '-e', '\'display', 'notification', f'"{title}', f'{message}"\''])
```

## Setup
Clone this Repo then open a Terminal in that Path and run these commands.
```bash
python3 -m venv env
source env/source/activate
pip3 install -r requirements.txt
```
To run:
```bash
python3 app.py
```

## Workings
- The Database is stored in instance/ after you run the app.py script.
- The App has a API Endpoint '/api/doubts'. Make a GET Request and get results.
- Everytime someone submits their doubt, it will run 'notify-send' command. If it is not present in your system, you can either install it (like in Mac and Linux) or just Disable the function and the calls (like in Windows) to Avoid any Potential errors. Without this Edit it might not run on many systems other than mine, since I have not tested the repo in windows or mac.
