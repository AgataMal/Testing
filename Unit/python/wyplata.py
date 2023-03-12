def wyplac(kwota, kod_pin):
    stan_konta = 1000
    if kwota <= stan_konta and kwota > 0:
        poprawny_pin = 2345
        if poprawny_pin == kod_pin:
            return kwota
