import json
import argparse
import os

def process_large_json(input_file_path, output_file_path):
    print("Opening JSON file...")
    with open(input_file_path, 'r', encoding='utf-8') as file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        print("Loading JSON data...")
        data = json.load(file)
        print("JSON data loaded.")
        
        for item in data['properties']['worldSaveData']['value']['GroupSaveDataMap']['value']:
            if item['value']['GroupType']['value']['value'] == "EPalGroupType::Guild":
                players = item['value']['RawData']['value']['players']
                print(players)
                for player in players:
                    # Write each player entry to the output file with indentation for readability
                    json.dump(player, output_file, indent=4)
                    output_file.write('\n')  # Add a newline after each player entry
                   
    print("Processing complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a level.sav.json file and output the player name + guids")
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument("--output_file", help="Path to the output JSON file (default: script directory)")

    args = parser.parse_args()

    input_file_path = args.input_file
    output_file_path = args.output_file

    if output_file_path is None:
        # If output file path is not provided, use the script directory
        script_directory = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_directory, "Players.json")

    process_large_json(input_file_path, output_file_path)