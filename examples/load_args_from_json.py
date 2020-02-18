from ez_args.parser import EasyArgs

# json file to load
args_json = 'args_json/args_example.json'
# returns the arg namespaces
e = EasyArgs(arguments=args_json).parse_args()

if e.file:
    print('file Key: {}'.format(e.file))
if e.verbose_level:
    print('verbose_level value: {}'.format(e.verbose_level))
