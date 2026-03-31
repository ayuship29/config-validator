import json

def validate_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)

        # Simple rules
        if "port" in config:
            if not isinstance(config["port"], int):
                print("❌ Error: 'port' must be an integer")
        else:
            print("❌ Error: 'port' field is missing")

        if "host" not in config:
            print("❌ Error: 'host' field is missing")

        print("✅ Validation complete")

    except Exception as e:
        print("Error reading file:", e)

# Example usage
validate_config("config.json")
