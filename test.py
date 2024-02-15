import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process JSON string argument')
    parser.add_argument('json_string', type=str, help='A JSON string to process')
    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        # Load JSON string as a dictionary
        json_data = json.loads(args.json_string)

        # Print the dictionary
        print("JSON data:")
        print(json_data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

if __name__ == "__main__":
    main()
