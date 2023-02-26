def czy_gruby(wzrost,waga):
    BMI=waga/wzrost**2

    if BMI <18.5:
        return "niedowaga"
    else:
        if BMI>=18.5 and BMI<=24.9:
            return "norma"
        elif BMI>=25 and BMI<=29.9:
            return "nadwaga"
        elif BMI>=30 and BMI<=34.9:
            return "otyłość"
        elif BMI>35:
            return "otyłość kliniczna"
