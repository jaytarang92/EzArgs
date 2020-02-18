from argparse import ArgumentParser
from json import loads

class EasyArgs:
    """Users argparse to return the ArgumentParser"""

    def __init__(self, arguments=None, parser_description=None, prefix=None):
        self.arguments = self._load_arguments(arguments=arguments)
        self.validated_args = self._validate_arguments(arguments_to_check=self.arguments)
        self.prefix = self._set_arg_prefix(prefix=prefix)
        self.parser = ArgumentParser(description=parser_description, prefix_chars=self.prefix)

    def _set_arg_prefix(self, prefix=None):
        if prefix is not None:
            return prefix
        return '-'

    def _load_arguments(self, arguments=None):
        if arguments is not None and type(arguments).__name__ != 'str':
            return arguments
        try:
            _args_from_file = None
            with open(arguments, 'r') as args:
                _args_from_file = loads(args.read())
            return _args_from_file
        except IOError:
            raise ValueError('File not found!')

    def _validate_arguments(self, arguments_to_check=None):
        if arguments_to_check is not None:
            if type(arguments_to_check).__name__ == 'list':
                for argument in arguments_to_check:
                    try:
                        if argument.items():
                            return arguments_to_check
                    except AttributeError:
                        raise AttributeError('Please check your arguments list!')
            raise AttributeError('Please make sure your arguments are in a list!')
        raise ValueError('arguments is not defined!')

    def build_arguments(self):
        for _arg in self.arguments:
            try:
                # slice the .get('name')[1:3] to extract the -f/ shorthand
                self.parser.add_argument('--{}'.format(_arg.get('name')), '-{}'.format( _arg.get('name')[1:3]),
                                         default=_arg.get('value'))
            except Exception as e:
                print(str(e))

    def parse_args(self):
        self.build_arguments()
        return self.parser.parse_args()

