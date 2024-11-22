# pdebugger_pdb.py
# d comes from a JSON payload we don't control
d = {"first": "v1", "second": "v2", "fourth": "v4"}
# keys also comes from a JSON payload we don't control
keys = ("first", "second", "third", "fourth")


def do_something_with_value(value):
    print(value)


breakpoint()

# or:
# import pdb; pdb.set_trace()

for key in keys:
    do_something_with_value(d[key])

print("Validation done.")


"""
$ python pdebugger_pdb.py
[0] > .../ch11/pdebugger_pdb.py(17)<module>()
-> for key in keys:
(Pdb++) l
 12     breakpoint()
 13
 14     # or:
 15     # import pdb; pdb.set_trace()
 16
 17  -> for key in keys:
 18         do_something_with_value(d[key])
 19
 20     print("Validation done.")
 21
 22
(Pdb++) keys  # inspect the keys tuple
('first', 'second', 'third', 'fourth')
(Pdb++) d.keys()  # inspect keys of d
dict_keys(['first', 'second', 'fourth'])
(Pdb++) d['third'] = 'placeholder'  # add missing item
(Pdb++) c  # continue
v1
v2
placeholder
v4
Validation done.
"""
