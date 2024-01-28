# PalPlayerDump

## Purpose
Parses a level.sav.json file and exports a Players.json file with the players name, guid, and last login time

This can be used for example to identify the correct player id for troubleshoting server player issues

## How to use
First use cheahjs's great palworld save tools https://github.com/cheahjs/palworld-save-tools
to generate a json file from the level.sav (level.sav.json)

This file will likely be quite large - ours was 1.5gb for example on a server with 5-10 active players


Then - run the script with python with one or two arguments
First argument is the path to the level.sav.json file
Second optional argument is where you would like to output the list
If you don't include the optional argument it defaults to where the script is located

If you use the second argument you need to specify --output_file "<path_to_file>"

## Example usage and output
python "C:\Dev\palplayerdump\palplayerdump.py" "C:\Users\Bonsai\Pal\Pa\Level.sav.json" --output_file "C:\Dev\palplayerdump\Example\Players.json"

```
{
    "player_uid": "8eb33572-0000-0000-0000-000000000000",
    "player_info": {
        "last_online_real_time": 908306000000,
        "player_name": "B4N5TER"
    }
}
{
    "player_uid": "dd046213-0000-0000-0000-000000000000",
    "player_info": {
        "last_online_real_time": 67906190000,
        "player_name": "trueTed"
    }
}
```