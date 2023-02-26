def czy_gruby(wzrost, waga):
    if wzrost is None or waga is None:
        return "błąd"
    if type(wzrost) == str or type(waga) == str:
        return "błąd"
    if wzrost <= 0 and waga <= 0:
        return "błąd"

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
