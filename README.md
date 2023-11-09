# ViralForth
ViralForth, or `VF`, is a Forth interpreter written in Python. 
It intends to demonstrate the ease with which Forth can "infect" other bedrock platforms, like a virus.

Clone the repo and run `python vf.py` to try it out.

# Structure
`VF` uses 3 main files: `vf.py`, `core.pydef`, and `boot.vf`.
`vf.py` runs the interpreter loop and reads in a dictionary of "bedrock" words defined as small python blocks in `core.pydef`.
It then runs `boot.vf`, which is comprised of only valid viralforth words.
Afterward, the interpreter loop reads directly from standard input.

# PYDEF files
The only commnication `.pydef` (PYDEF) files have outside themselves are the functions `push()` and `pop()`, which push and pop numbers to stack respectively.
PYDEF files may only use these two functions to interact with the program's global state.
Aside from this, the primitives in `core.pydef` are only confined to using standard Python functions, such as `print()` and `chr()`.

PYDEF files are defined using this general format:
```
# duplicates a value on stack
# (n -- n n)
: DUP
n = pop()
push(n)
push(n)
$$$
```
- `#` indicates a comment.
- `:` indicates the start of the definition, and the all-caps word after is the VF word being defined.
- `$$$` indicates the end of the definition.


