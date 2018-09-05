<center>

# olympics


<center>

![Olympic Logo](images/200px-Olympic_flag.svg.png)




## Introduction

This is the historical olympic data analysis project for MSDS 7331. The dataset
was taken from [kaggle](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results). The dataset consists of 271k rows and 15 columns full of olympic data which span
the years 1896 to 2016.


## Windows Anaconda Setup

The `environment.yml` file holds all the dependencies for this particular project.
In order to have the project working on your machine you will need to perform the
following setup of [anaconda]() as `conda` is used to manage the python environment
for this project.

If Anaconda is not setup on your machine you can follow the directions [here](https://conda.io/docs/user-guide/install/windows.html)

## Mac Anaconda setup

If you are using a mac the following directions for set up can be found [here](https://conda.io/docs/user-guide/install/macos.html).

### Starting the project for first time

Creating the `olympics` environment

```bash
# cd into the olympics directory
cd <your_local_path>/olympics/
#in the terminal run

conda env create -f environment.yml

```
This creates the `olympic` conda environment with all the dependencies listed in
`environment.yml`. You can now switch to the environment  by running the following..

```bash
source activate olympics
```

### Making updates to environment

If you add a new dependency to the project make sure you update the `environment.yml`
file so in order to have those new updates reflect locally for you.

```bash
conda env update -f environment.yml
```

This `olympics` environment includes `jupyter notebook` as well as many of the other
packages we need in order to run the analysis on this project.



## Group Members

| Brian Coari  |
Stephen Merritt |
Cory Thigpen    |
Quentin Thomas |
