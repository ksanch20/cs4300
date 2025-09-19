import subprocess 
import os

def test_task1_output():
	script_path =  os.path.expanduser("~/cs4300/homework1/src/task1.py")
	result = subprocess.run(
		["python3", script_path],
		capture_output=True,
		text = True
	)
	assert result.stdout.strip() == "Hello, World!"
