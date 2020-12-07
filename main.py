def solve_tower(x, from_rod, to_rod, aux_rod):
    if x > 0:
        solve_tower(x - 1, from_rod, aux_rod, to_rod)
        print(f'Move the disk {x} from {from_rod} to {to_rod}')
        solve_tower(x - 1, aux_rod, to_rod, from_rod)
