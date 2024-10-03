lang = "EN"
lang_opt = input("Enter L to change language or other key to continue>> ")
while lang_opt == '1':
    if lang == "RU":
        lang = "EN"
        lang_opt = input("Enter L to change language or other key to continue>> ")
    else:
        lang = "RU"
        lang_opt = input("Введите L, чтобы сменить язык, или любую клавишу, чтобы продолжить>>")
if lang_opt == "EN":
    f = "Enter first number>> "
    o = "Enter operation (+, -, /, *)>> "
    s = "Enter second number>> "
    r = "Result>> "
    e = "Error"
    p = "Enter 'y' to continue amd other key to finish>> "
if lang_opt == "RU":
    f = "Введите первое число>> "
    o = "Введите операцию (+, -, /, *)>> "
    s = "Введите второе число>> "
    r = "Результат>> "
    e = "Ошибка"
    p = "Введите 'y' чтобы продолжить, или любую клавишу, чтобы заверишть >> "
prodolzhit = 'y'
while prodolzhit == 'y':
            f_num = float(input(f))
            oper = input(o)
            s_num = float(input(s))
            if oper == '+':
                print(r, f_num + s_num)
            elif oper == '-':
                print(r, f_num - s_num)
            elif oper == '*':
                print(r, f_num * s_num)
            elif oper == '/':
                print(r, f_num / s_num)
            else:
                print(e)
            prodolzhit = input(p)