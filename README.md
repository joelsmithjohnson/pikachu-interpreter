# Pikachu Interpreter

This is an interpreter for Pikachu written in python.

The definition of the esoteric programming language named 'pikachu' can be found [here](http://trove42.com/introducing-pikachu-programming-language/)

### Install

```bash
$ git clone https://github.com/joelsmithjohnson/pikachu-interpreter
$ cd pikachu-interpreter
$ python setup.py install
```

### Usage

From the command line. navigate to where your Pikachu files are located, and run the following command.

```bash
$ python -m pikachu {PikachuFileName}
```

You can also specify n number of integers you want to preload onto the main stack (named `pi pikachu`). Use the following syntax where `[args]` represents a space seperated list of integers. 

```bash
$ python -m pikachu {PikachuFileName} [args]
```

 
