# ez_args
argparse the ez py way


## Example 

```py

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
```

```sh
  $ python examples/example.py --file this_is_a_test.py --verbose_level 9
  file value: test.py
  verbose_level value: 9
  $
```

```sh
  $ python examples/example.py -f this_is_a_test.py -v 9
  file value: test.py
  verbose_level value: 9
  $
```
Output of the commands is the same. 
