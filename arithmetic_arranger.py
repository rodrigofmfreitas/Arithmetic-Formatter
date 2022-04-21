def arithmetic_arranger(problems, *args):
    split_problems = list()
    arranged_problems = ""
    list_above = list()
    list_below = list()
    sep_digits = ""
    if len(problems) > 5:
      return "Error: Too many problems."
    for problem in problems:
        split_problems.append(problem.split())
    for t in split_problems:
        if t[1] != "+" and t[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if t[0].isnumeric() == False or t[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        if len(t[0]) > 4 or len(t[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    for problem in split_problems:
        if len(problem[0]) < len(problem[2]) + 2:
            aux = ""
            while (len(aux) <= len(problem[2]) + 2 - len(problem[0])):
                aux += " "
        else:
            aux = "  "
        aux += problem[0]
        list_above.append(aux)

    for i, problem in enumerate(split_problems):
        aux = problem[1]
        if len(problem[2]) + 2 < len(list_above[i]):
            while (len(aux) < len(list_above[i]) - len(problem[2])):
                aux += " "
        aux += problem[2]
        list_below.append(aux)
        

    for i, v in enumerate(list_above):
        if "   " in list_above[i]:
            list_above[i] = list_above[i].replace("   ", "  ")
            if "  " in list_below[i]:
                list_below[i] = list_below[i].replace("  ", " ")
        while(len(list_above[i]) < len(list_below[i])):
            list_above[i] = " " + list_above[i]
        arranged_problems += list_above[i] + "    "
    arranged_problems = arranged_problems[:-4] + "\n"
    for i in list_below:
        arranged_problems += i + "    "
    arranged_problems = arranged_problems[:-4] + "\n"

    for i in list_below:
        aux = ""
        while (len(aux) < len(i)):
            aux += "-"
        sep_digits += aux + "    "

    arranged_problems += sep_digits[:-4]

    if args:
        aux = sep_digits.split()
        solved_digits = ""
        for i, problem in enumerate(split_problems):
            anaux = ""
            if problem[1] == "+":
                teste = int(problem[0]) + int(problem[2])
            else:
                teste = int(problem[0]) - int(problem[2])
            teste = f"{teste}"
            for j in range(len(aux[i]) - len(teste)):
                anaux += " "
            anaux += teste
            solved_digits += anaux
            solved_digits += "    "
        arranged_problems += "\n" + solved_digits[:-4]

    return arranged_problems