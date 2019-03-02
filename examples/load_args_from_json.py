from ez_args.parser import EasyArgs

args_json = 'args_example.json'
e = EasyArgs(arguments=args_json).parse_args()

if e.file:
    print('file value: {}'.format(e.file))
if e.verbose_level:
    print('verbose_level value: {}'.format(e.verbose_level))
    
