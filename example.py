from ez_args.parser import EasyArgs

args = [
    dict(name='--file'),
    dict(name='--verbose_level')
]
e = EasyArgs(arguments=args).parse_args()

if e.file:
    print('file value: {}'.format(e.file))
if e.verbose_level:
    print('verbose_level value: {}'.format(e.verbose_level))
