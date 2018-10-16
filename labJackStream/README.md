# How to use of labJackStream

This is a program made to automate the measurement of RAT (réflexion,absorption et transmission)  data to determine the diffusion coefficients of biological sample. Th program, if used with the correct experimental setup, performs a correction of the laser source fluctuations.

## Getting Started

These instructions will get you a copy of the project on your local machine for usage and development purposes.

### Prerequisites

It is obligatory to get the Anaconda distribution for python 3 since it has most of the required modules.
**To be able to use labJackStream, make sure to install the following packages through a command window: (power shell)**

```powershell
$ pip install labjackpython
```

If those modules are missing you wont be able to use the program properly.

### Installing

First of all, if it has not been done yet, get a copy of the repository (with clone, fork, or download - see GitHub's documentation for more information).

```powershell
$ git clone https://github.com/JLBegin/TPOBLabs.git
```

### Running main from IDE

To run the main app, open the labJackStream project in your IDE and run the *main.py* file.

You can now choose to start an acquisition and visualize the data live. Pressing on the 'STOP' button will save a .txt file with the following architecture:

| Time | Laser power | Reflexion power | Transmission Power |
| ---- | ----------- | --------------- | ------------------ |
| ...  | ...         | ...             | ...                |


It also will print a table in your *run* window with different statistics from the acquisition you just done. You are recommended to rename the .txt data file after each acquisition with a significant name. 

It also will print a table in your command prompt with different statistics from the acquisition you just done. You are recommended to rename the .txt data file after each acquisition with a significant name. 

It also will print a table in your command prompt with different statistics from the acquisition you just done. You are recommended to rename the .txt data file after each acquisition with a significant name. 

