import subprocess
import datetime
import random
from datetime import date, timedelta
import pdb;
import os

# Define the path to the file you want to edit
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = f'{ROOT_DIR}/backend/src/main.js'
messages = ["Updated main.js", "Added console", "console.log hello added"]
# breakpoint() #for debugger
start_date = date(2023, 1, 5)
end_date = date(2023, 5, 20)
delta = timedelta(days=1)
while start_date <= end_date:
  if start_date.weekday() < 5:
    while 0 < random.randint(0,9):
      # Open the file and make your edits
      with open(file_path, "a") as f:
        f.write("\n console.log('hello');")

      # Set the commit date to a past date
      past_date = datetime.datetime(start_date.year, start_date.month, start_date.day, 12, 0, 0) # Change this to the date you want
      env = {"GIT_COMMITTER_DATE": past_date.strftime("%s %z")}

      # Use Git to add and commit the changes to the file with past date
      subprocess.call(["git", "add", file_path])
      subprocess.call(["git", "commit", "--date", past_date.strftime("%c %z"), "-m", random.sample(messages, 1)[0]], env=env)
  start_date += delta

subprocess.call(["git", "push", "origin", "main"])
