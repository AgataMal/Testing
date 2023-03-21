def wynik_BMI(wzrost, waga):
    if wzrost is None or waga is None:
        raise ValueError("wprowadź obie wartości liczbowe")
    if type(wzrost) == str or type(waga) == str:
        raise ValueError("błędne wartości")
    if wzrost <= 0 or waga <= 0:
        raise ValueError("podaj wartość większą niż 0")

    BMI = waga/wzrost**2

    if BMI < 18.5:
        return "niedowaga"
    else:
        if BMI >= 18.5 and BMI <= 24.9:
            return "norma"
        elif BMI >= 25 and BMI <= 29.9:
            return "nadwaga"
        elif BMI >= 30 and BMI <= 34.9:
            return "otyłość"
        elif BMI > 35:
            return "otyłość kliniczna"

    
