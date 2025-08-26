import argparse

def create_parser(*args):
    """
    Creates and configures an ArgumentParser instance in a single call.

    This function is a wrapper for argparse that simplifies the creation
    of complex parsers.

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
    """
    # 1. Basic input validation
    if not args:
        raise ValueError(
            "At least one dictionary for parser configuration must be provided.")

    parser_config = args[0]
    arg_definitions = args[1:]

    if not isinstance(parser_config, dict):
        raise ValueError(
            "The first argument must be a configuration dictionary.")

    # 2. Create the parser instance
    #    We unpack the first dictionary to configure the parser
    parser = argparse.ArgumentParser(**parser_config)

    # 3. Add all defined arguments
    for arg_def in arg_definitions:
        if 'name' not in arg_def:
            raise ValueError(
                f"The argument dictionary {arg_def} is missing the 'name' key.")

        # Copy the dictionary to avoid modifying the original
        options = arg_def.copy()
        # Extract the name (or flags), which is not a keyword for add_argument
        name_or_flags = options.pop('name')

        # `name_or_flags` can be a string (positional argument)
        # or a list of strings (optional flags like ['-f', '--file'])
        if isinstance(name_or_flags, list):
            parser.add_argument(*name_or_flags, **options)
        else:
            parser.add_argument(name_or_flags, **options)

    return parser.parse_args()