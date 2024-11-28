import json
import sys

def json_to_custom_lang(data):
    """
    Преобразует JSON-данные в формат учебного конфигурационного языка.
    """
    if isinstance(data, dict):
        return "{\n" + "\n".join(f" {key} -> {json_to_custom_lang(value)}." for key, value in data.items()) + "\n}"
    elif isinstance(data, list):
        return "( " + ", ".join(json_to_custom_lang(item) for item in data) + " )"
    elif isinstance(data, str):
        return f'"{data}"'
    elif isinstance(data, (int, float)):
        return str(data)
    else:
        raise ValueError(f"Unsupported JSON value: {data}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    try:
        result = json_to_custom_lang(json_data)
        print(result)
    except Exception as e:
        print(f"Error converting JSON to custom language: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
