

def random_check(random_start, random_end):
    """Validates the input values for generating random number."""
    if random_start > random_end:
        return False
    return True


def predict_check(value_list):
    """Validates the input values for generating prediction on list"""
    for value in value_list:
        if isinstance(value, (int, float)):
            pass
        else:
            return False
    return True

def string_to_digit(input_list):
    output_list = []
    for i in input_list:
        try:
            i = float(i)
        except:
            pass
        output_list.append(i)
    return output_list
