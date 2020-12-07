# Hanoi Tower Solver

This is a simple **Hanoi Tower Solver** that receives the amount of disks, the rod from, the rod to and the auxiliary
rod.

## Usage

You can clone this repository or just navigate to `main.py` and copy the code. 

## Example

Here we use the `solve_tower` to solve a Hanoi Tower of 4 disks and will give us the way to follow.

```python
def solve_tower(x, from_rod, to_rod, aux_rod):
    if x > 0:
        solve_tower(x - 1, from_rod, aux_rod, to_rod)
        print(f'Move the disk {x} from {from_rod} to {to_rod}')
        solve_tower(x - 1, aux_rod, to_rod, from_rod)


if __name__ == '__main__':
    solve_tower(4, 'A', 'C', 'B')
```

Here the expected output.

```shell
Move the disk 1 from A to B
Move the disk 2 from A to C
Move the disk 1 from B to C
Move the disk 3 from A to B
Move the disk 1 from C to A
Move the disk 2 from C to B
Move the disk 1 from A to B
Move the disk 4 from A to C
Move the disk 1 from B to C
Move the disk 2 from B to A
Move the disk 1 from C to A
Move the disk 3 from B to C
Move the disk 1 from A to B
Move the disk 2 from A to C
Move the disk 1 from B to C
```