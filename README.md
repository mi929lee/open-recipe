# Open Recipe
A website that creates ("cooks up") common biological protocols ("recipes") for the Opentrons 2 (OT-2) pipetting robot.


## Instructions to Download the Opentrons Package
This is needed in order to run the OT-2 simulations. The OT-2 simulations virtually run the protocols instantaneously (in seconds), so that we do not have to test the protocol on the OT-2 robot directly, which would take much longer and may potentially cause problems for the robot.

1. On the command line, run `pip install opentrons`. 

    - You should see output that ends with `"Successfully installed opentrons-4.6.2"`.


## Instructions to Simulate Python Protocols
This is to run OT-2 simulations.

1. Open the file directory containing the python protocol files (files ending with `.py`).

    - Here, the protocols are under the `protocols` folder. Assuming this GitHub repository is on your Desktop and you just opened a new terminal, run the commands on the right side of the `%` symbol. 
        - The text on the left of the `%` symbol should be what your command line already provides.
        ```zsh
            name@computer_name ~ % cd Desktop
            name@computer_name Desktop % cd open-recipe
            name@computer_name open-recipe % cd protocols
        ```

2. On the command line, run either of the following commands, depending on your operating system:
    
    - OS X / Linux: `opentrons_simulate my_protocol.py`

    - Windows: `opentrons_simulate.exe my_protocol.py`

    **Note**: Replace `my_protocol.py` with the name of whatever file you want to simulate.

3. The output from running the simulation should show what commands the pipetting robot OT-2 would have done if the protocol were run on the robot directly.
