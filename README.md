# World Cup Scorekeeping

### Players

The teams that players pick are stored in text files in the [players](players) folder. Each file corresponds to a single player. For example, if my name was Bob, and I picked Mexico, Columbia, and South Korea, my file (`bob.txt`) would look like this:
```
Mexico
Columbia
South Korea
```
Make sure that the teams are spelled correctly, so that the names of the countries match the names of the countries in [country names file](teams/abbreviations-english.txt) or in the commented out section of [team-scores.txt](team-scores.txt).

If you have difficulty generating a new text file for a new player, you can simply duplicate one of the original players or open the [make-new-player app](make-new-player.app). Player files must be in plain text format (.txt extension). Uppercase/lowercase doesn't matter.

### Adding Results

To add the results of a game, you need to update the [team-scores.txt](team-scores.txt) file. There are instructions inside of that file, but here are some more.

 - All lines that are empty or start with a `#` are ignored
 - Scores must be entered in the format `AA11 AA11`
    - The AA is a 2 digit country code (which can be found in the [team scores file itself](team-scores.txt) or in [country names file](teams/abbreviations-english.txt).
    - The 11 is a 2 digit, left padded number, so if a team scored 7 goals, you would write 07, and if a team scored 11 goals, you would write 11.
 - The winning team must come before the losing team
 - The order doesn't matter for ties

### Running the program

To run the program, just double-click the [run me app](run-me.app). Alternatively, if that doesn't work, download python3 [here](https://www.python.org/downloads/), open the [open-terminal app](open-terminal.app), and run `python3 scoring.py`. Last resort just ask Will.

