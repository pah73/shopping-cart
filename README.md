# shopping-cart
Shopping Cart Project
# This README file has been adapted from the rock-paper-scissors exercise README file from Professor Rossetti shown in class and available on our course GitHub

Instructions about running the shopping-cart program

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip
  + A text editor and command line tool (I use VSCode and Terminal on MacOS)

## Forking the repo 
  Fork this [remote repository](https://github.com/pah73/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

## Command line instructions & Setup

```sh
cd shopping-cart # directory to where repo is stored locally
cd Documents/GitHub/shopping-cart #my personal file location
```

Use Anaconda to create and activate a new virtual environment in the command line:


```sh
conda create -n shopping-cart-env python=3.8 #run an updated version of python (at least 3.7)
conda activate shopping-cart-env #activating once created
```

## Installing Packages 
Create a requirements.txt file:
+ requirements.txt file
From inside the virtual environment, install package dependencies if necessary.

add the dotenv package to the requirements.txt file and install the package in the command line with this command:

```sh
pip install -r requirements.txt
```

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script and try the program !

```py
python shopping-cart.py
```

The program asks the user to input all the items in their shopping cart at checkout, one-by-one using their integer ID's. When all the products are inputted, the user is asked to type in "DONE". Aterwards, the program will print pricing and greet the user out of the transaction.




