# Flexcreo

FlexCreo analyzes the PTC Creo Parametric FlexNet License Server's ptc_d.log file for license feature usage.
An example of the license feature usage graph generated by FlexCreo:
![](/image/creo_usage1.png)


# Features

FlexCreo calculates these statistics:
* Number of license checkouts from the license server
* Number of license returns to the license server
* Number of denials of license request

It also plots the following graphs:
* Usage over time (no. of licenses in use) of each of the Creo license features found in the log file.
* Denials over time of each of the Creo license features found in the log file.


The following temporary json files are created each time FlexSolidworks is run:
* log_file_name.json:  Each "line" in this file represents a check-in and check-out of a license by a user.
* feature_name.json: This file contains the co-ordinates used to plot the usage dand denials graphs.

All time stamps in the log file are converted to Pacific Daylight Time PDT.


# Requirements

`Python` must be installed, with the following modules: `Pandas` and `Matplotlib`.

FlexCreo has been tested on `Python 3.10` and `Python 3.11` on `Windows 10`.


# Setup Instructions

Download and install `Python` for Windows from [python.org](https://www.python.org/downloads/).  Check the �Add python.exe to PATH� checkbox during the installation.

Install the `pandas` and `matplotlib` modules.  In the Windows command prompt, run the following commands
```
pip install pandas
pip install matplotlib
```

Download the flexcreo.py script and put it in a directory containing the Solidworks log files you want to analyze, e.g., C:\temp\example\.  CD Change Directory to the directory and run `python flexsolidworks.py`.
```
cd C:\temp\example
python flexcreo.py
```

An unsigned Pyinstaller compiled executable flexsolidworks.exe is available here: 
[flexcreo.exe](https://drive.google.com/file/d/1bbUdUQ2R18S9ZdDKw0F0RLp0Mu9S9ps9/view?usp=sharing)

