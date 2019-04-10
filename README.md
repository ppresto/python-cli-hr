
# Python CLI - hr

This sample hr utility exports user data from the OS (pwd) and exports it to csv or json formats.  It will write to stdout by default or to a file if specified.


# Setup

## Installation From Source

To install the package after you've cloned the repository:

```
$ cd ./hr
$ pip install --user -e .
```

## Preparing your Python Development Env

I'm doing most things inside a container to keep a clean system.  My custom python 3.7 container includes additional python dependencies, pip, and pipenv.  You can use the included Dockerfile to build/run this or install these things locally.

Follow these steps to start developing with this project:

1. Ensure `pip`, `pipenv` are installed
2. Clone repository: `git clone https://github.com/ppresto/python-cli-tools.git`
3. `cd` into the repository (./hr)
4. Setup pipenv for new project only: `pipenv --python python3.7`
4. Activate virtualenv: `pipenv shell`
5. Install dependencies from Pipfile.lock: `pipenv install`
6. (Optional) Install pgbackup CLI utility (from ./pgbackup): `pipenv install -e .`
  1. You may have already used pip to install this earlier.  THis will only install in your virtual env.

Verify the utility is available
```
hr -h
```

# Usage
```
$ hr --format=csv --path=path/to/users.csv

$ hr --path=path/to/users.json  #writes output to users.json in default format=json

$ hr
[
  {
    "name": "cloud_user",
    "id": 1002,
    "home": "/home/cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "kevin",
    "id": 1003,
    "home": "/home/kevin",
    "shell": "/bin/zsh"
  },
]

$ hr --format=csv
name,id,home,shell
cloud_user,1002,/home/cloud_user,/bin/bash
kevin,1003,/home/kevin,/bin/zsh
```

# Troubleshooting

## hr - Using pdb to troubleshoot in interactive mode
You can iterate every step of yourScript.py in interactive mode by running `python -m pdb yourScript.py`.  Because your in interactive mode you can output or assign values at every step to see what your code is doing making this a good troubleshooting process.

You can target specific loops and functions easily by including the library at the top of your script temporarily by adding:
`import pdb`

Then set the start of your trace by adding this line exactly where you want to be looking and save.
`pdb.set_trace()`

Run yourScript.py: `python -i yourScript.py`

Some helpful pdb commands:
```
h     # help
ll    # list script
n     # next
a     # print current function args
r     # continue until current function returns
q     # quit

```

# Python Packages
## Python - Creating this Package
```
cd ./hr
mkdir -p src/hr
vi setup.py # create package setup.py
touch src/hr/__init__.py
touch src/hr/.gitkeep
vi src/hr/cli.py  # create initial CLI code.
vi src/hr/users.py
vi src/hr/export.py
vi README.md
```

## Python - Creating Deployable Install File

```
cd ./hr
python setup.py bdist_wheel   #creates dist and build dirs
ls dist/hr-1.0.0-py3-none-any.whl
```
Now we can install the pgbackup utility with pip from a local file or http:// if you have it hosted somewhere.

`pip install dist/hr-1.0.0-py3-none-any.whl`
