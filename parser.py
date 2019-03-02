from argparse import ArgumentParser


class EasyArgs:
    """Users argparse to return the ArgumentParser"""

    def __init__(self, arguments=None, parser_description=None):
        self.arguments = self._validate_arguments(arguments_to_check=arguments)
        self.parser = ArgumentParser(description=parser_description)

    def _validate_arguments(self, arguments_to_check=None):
        if arguments_to_check is not None:
            if type(arguments_to_check).__name__ == 'list':
                for argument in arguments_to_check:
                    try:
                        if argument.items():
                            return arguments_to_check
                    except AttributeError:
                        raise AttributeError('Please check your commands list!')
            raise AttributeError('Please make sure your commands are in a list!')
        raise ValueError('commands is not defined!')

    def build_arguments(self):
        for _arg in self.arguments:
            try:
                self.parser.add_argument(_arg.get('name'), _arg.get('name')[1:3])
            except Exception as e:
                print(str(e))

    def parse_args(self):
        self.build_arguments()
        return self.parser.parse_args()

