# Easy ArgParse

Easy ArgParse is a small lib to simplify the use of python's ArgParse.

## API

Creates and configures an ArgumentParser instance in a single call.

This function is a wrapper for argparse that simplifies the creation
of complex parsers.
```
Args:
    *args: A sequence of dictionaries.
        - The first dictionary (required) contains the keyword arguments
            for the `argparse.ArgumentParser` constructor (e.g., 'description').
        - Subsequent dictionaries (optional) define the arguments
            to be added to the parser. Each dictionary must contain a
            'name' key (with the name or flags) and other optional keys
            that correspond to the arguments of `parser.add_argument()`
            (e.g., 'help', 'action', 'type', 'default').

Returns:
    argparse.Namespace: An object from `parser.parse_args()` containing the
                        parsed arguments.

Raises:
    ValueError: If at least one configuration dictionary is not provided,
                or if an argument dictionary is missing the 'name' key.
```

## Usage

```python
# example.py

from easy_argparse import create_parser

def main():

    # Create the parser and parse the arguments
    args = create_parser({'description': 'A simple command-line tool to greet someone.'},
                            {  
                                'name': 'name',
                                'type': str,
                                'help': 'The name of the person to greet.'
                            },
                            {
                                'name': ['-v', '--verbose'],
                                'action': 'store_true',
                                'help': 'Enable verbose output.'
                            }
                        )

    # Use the parsed arguments
    greeting = f"Hello, {args.name}!"
    if args.verbose:
        print("Verbose mode enabled.")
        print(f"Executing greeting for '{args.name}'...")

    print(greeting)

if __name__ == '__main__':
    main()

```

```bash
python example_script.py Alice
# Output: Hello, Alice!

python example_script.py Bob --verbose
# Output:
# Verbose mode enabled.
# Executing greeting for 'Bob'...
# Hello, Bob!
```
