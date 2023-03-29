def pizza_split(no_people: int, no_pizza_slices: int) -> int:
    given_slices = [0 for i in range(no_people)]  # nikt nic nie ma
    for i in range(1000):
        if i % no_people == 0:
            if i > 0 and i % no_pizza_slices == 0:
                return i / no_pizza_slices

        idx = i % no_people;
        given_slices[idx] = given_slices[idx]+1


