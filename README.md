# TFF_Optimization
A tool to help make decisions for Telegraph Fantasy Football
This tool was derived from a Sky version built by Sam Troy which can be found here:
https://github.com/SamTroy/SkyFF_Optimization
Please note that because of this you will still see the word sky mentioned a lot in the code!

Generates player expected points and transfer plan

Modifying player EV and xMins or using other sources to reflect your own judgment is encouraged

## Setting up
- Install python
- Add CBC to environment path
- Clone this repository to your machine
- Install all packages in the Imports section of the notebook

## Running the solver
- Download the latest TFF player list from https://www.ffstuff.co.uk/playersTFF202324.php. Save this as "TFF players.csv" in the "data" folder. 
- In the "scripts" folder run the "playerCopy" script to copy relevant players details to the "prior_player_data.csv" file. 
- Download FPL Review projections, and save the file in data folder as fplreview.csv (alternatively produce your own set of expected minutes, or omit this step to use defaults)
- Run import and function definition cells
- Generate model output using generate_model_output function
- Generate optimal solution using solve_tff_mp function

### Future plans
- Periodically update player and team prior data
- Add a function to run the solver with multiple possible fixture permutations
- Perform experiments to get a better idea of what parameters and settings are best for the solver
- Refine player and team model
- Add a user interface to the solver to streamline the process