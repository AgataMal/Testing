def wyplac(kwota, kod_pin):
    stan_konta = 1000
    poprawny_pin = 2345
    if not poprawny_pin == kod_pin:
        raise ValueError("błędny pin")
    if kwota <= stan_konta and kwota > 0:
        return kwota
    else:
        raise ValueError("błędna kwota")