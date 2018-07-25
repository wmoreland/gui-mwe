# GUI-MWE

Before starting work on a GUI for a more complicated project I wanted to work out how I can link a separate module with a GUI and have them communicate with each other. I will use this as an initial template for a later project.

## Project directory outline

*Self-titled directory*

    self-titled script
        import function(s)
        import GUI (perhaps in an if statement to allow CLI use)

    *Functions directory*

        function(s) script(s)

    *GUI directory*

        GUI script
            import function(s)
            link GUI elements to functions
