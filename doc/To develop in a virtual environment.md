## For development in a Python virtual environment

Some developers may need to use `venv`, for example when working with Qt Creator in a Python project.

### Create a virtual environment

In Debian 12 and MX Linux 23, support for virtual environments is not installed by default.

**✅ Solution**

Install the required package:

```bash
sudo apt install python3-venv
````

Open a terminal in the Python project folder:

```bash
cd /path/to/the-python-project
```

and once you are there, in a Linux terminal run:

```bash
python3 -m venv venv
```

then activate the environment with:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install PyQt6
```


#### How to deactivate the venv? (skip this if you are still working in your virtual environment)

After you finish what you were developing, to leave the virtual environment, in the terminal you will see something similar to this:

```bash
(venv) youruser@yourmachine:...
```

To exit the virtual environment, simply run:

```bash
deactivate
```
