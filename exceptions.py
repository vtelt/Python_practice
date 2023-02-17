# def print_sum(num1, num2):
#     try:
#         print(num1 + num2)
#     except Exception:
#         print('Could not add these numbers')

def print_sum(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sum function must be int')
    print(num1 + num2)


print_sum(2, 3)
try:
    print_sum(2, 'hi')
except Exception as e:
    print(f'Something went wrong: {e}')