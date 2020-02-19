def move_tower(height, original, final, intermediate):
    """ Tower of Hanoi algorithm:
    1. Move tower of height-1 to intermediate using the final pole
    2. Move remaining disc to final pole
    3. Move tower of height-1 to final using the original pole
    """
    # count = 1
    if height >= 1:
        move_tower(height-1, original, intermediate, final)
        # print(f"Step: {count}")
        move_disc(original, final, height)
        move_tower(height-1, intermediate, final, original)
        # count += 1

def move_disc(origin, destination, disc_number):
    """ Move a single disc
    """
    print(f"Moving disc {disc_number} from {origin} to {destination}")

move_tower(5, "A", "C", "B")


