# GUI-MWE

Before starting work on a GUI for a more complicated project I wanted to work out how I can link a separate module with a GUI and have them communicate with each other. I will use this as an initial template for a later project.

## Project directory outline
```
Root directory
│
├── control script (e.g. gui-mwe.py)
│   import function(s)
│   import GUI (perhaps with if statement to allow CLI use)
│
├── Functions directory
│   └── function script(s) (e.g. myfunc.py)
│
└── GUI directory
    └── GUI script (e.g. gui.py)
        import function(s)
        link GUI elements to functions
```
