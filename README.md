# ez_args
argparse the ez py way


## Example 

```py

from ez_args.parser import EasyArgs

args = [
    dict(name='file'),
    dict(name='verbose_level')
]
e_args = EasyArgs(arguments=args).parse_args()

# check `file` arg and print value
if e_args.file:
    print('file value: {}'.format(e.file))
    
# check `verbose_level` arg and print value
if e_args.verbose_level:
    print('verbose_level value: {}'.format(e.verbose_level))
```
### Full arg name
```sh
  $ python examples/example.py --file this_is_a_test.py --verbose_level 9
  
  file value: this_is_a_test.py
  verbose_level value: 9
  
  $
```
### Shorthand arg
```sh
  $ python examples/example.py -f this_is_a_test.py -v 9
  
  file value: this_is_a_test.py
  verbose_level value: 9
  
  $
```
