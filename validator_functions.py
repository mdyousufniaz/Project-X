def convert_number(num: str) -> int | None:
    try:
        return int(num)
    except ValueError:
        return None
    

def is_valid_term(value: str) -> bool:

    if value:
        for term in value.split(','):
            if term.count('-') == 1:
                num1, num2 = term.split('-')
                num1 = convert_number(num1)
                num2 = convert_number(num2)

                if None in (num1, num2) or num1 >= num2:
                    return False
                
            else:
                if convert_number(term) == None:
                    return False
                
    return True
                