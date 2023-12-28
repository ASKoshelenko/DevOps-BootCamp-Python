>Please use branch ```snapshot-util``` for this task that already exist in your forked repository after you has been started task
### TASK 1
Create a simple python app which would monitor your system/server. Output should be written to json file and stdout.

For monitoring purposes use **psutil** module, see: https://pypi.org/project/psutil/ 

It should create snapshots of the state of the system each 30 seconds (configurable):

    {"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
    "%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
    "KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
    "KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
    "Timestamp": 1624400255}

Output should be written to the console and  json file.

The script has to accept an interval (default value = 30 seconds) and output file name. Use argparse module, see: https://docs.python.org/3/library/argparse.html

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", default=20)

    args = parser.parse_args()
    ...
    with open((args.f, "a") as file:
	    # use json.dump to write JSON-snapshot to file
	    # don’t forget to import json before
	    ...
		
Use for console output:
    os.system('clear')
    print(snapshot, end="\r")

Use __time.sleep()__ to make an interval.

Timestamp is the current time timestamp without a float part.

Separate snapshots in json-file by new line.

Clean file content when the script is started.

**(!) At least one (any) class should be created.**

 
### TASK 2
Create a distributive package of the script from **Task 1**

The package should have similar structure:
```bash
zoo-example
├── animals
│   ├──handlers
│   │  ├── __init__.py
│   │  ├── walk.py
│   │  └── swim.py
│   ├── __init__.py
│   ├── crocodile.py
│   ├── monkey.py
│   └── zoo.py
├── README.md
└── setup.py
```

Add setup.py

Tool name is **snapshot** (name="snapshot")

Add README.md with description how to install and use the tool
https://docs.gitlab.com/ee/user/markdown.html	

Note, you haven’t put any distributions to PR (*.whl, *.tar.gz, *.rpm and so on), only the project.

Verify package:

    cd ..
    snapshot-util$ pip install -U ./snapshot-util
    snapshot-util$ snapshot -i 1
