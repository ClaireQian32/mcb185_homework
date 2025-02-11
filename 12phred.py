import math 
def quality_to_error(quality_char: str):

    return 10 ** ((ord(quality_char) - 33) / -10)

def error_to_quality(error_rate: float) -> str:

    return chr(int(-10 * (math.log10(error_rate))) + 33)


print(quality_to_error('I')) 
print(error_to_quality(0.01))
