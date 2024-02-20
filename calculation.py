from utilities import check


def cell_counter(start_x: int, start_y: int) -> int:

    count_cells: int = 0
    buffer = [(start_x, start_y)]
    all_visited_cells = {(start_x, start_y)}

    while buffer:

        x_and_y: tuple = buffer.pop()

        x = x_and_y[0]
        y = x_and_y[1]

        count_cells += 1

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:

            new_x = x + dx
            new_y = y + dy

            if check(new_x, new_y, 25) and (new_x, new_y) not in all_visited_cells:
                buffer.append((new_x, new_y))
                all_visited_cells.add((new_x, new_y))

    return count_cells
