# example.py

from easy_argparse import create_parser

def main():
    # Define the parser configuration
    parser_config = {
        'description': 'A simple command-line tool to greet someone.'
    }

    # Define the arguments
    name_arg = {
        'name': 'name',
        'type': str,
        'help': 'The name of the person to greet.'
    }

    verbose_arg = {
        'name': ['-v', '--verbose'],
        'action': 'store_true',
        'help': 'Enable verbose output.'
    }

    # Create the parser and parse the arguments
    args = create_parser(parser_config, name_arg, verbose_arg)

    # Use the parsed arguments
    greeting = f"Hello, {args.name}!"
    if args.verbose:
        print("Verbose mode enabled.")
        print(f"Executing greeting for '{args.name}'...")

    print(greeting)

if __name__ == '__main__':
    main()
