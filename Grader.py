import os
import importlib.util

names = ["Agniv Sarkar"]

def names_to_directories(names):
    for name in names:
        split = name.split()
        first, second = split[0], split[1]
        if len(split) == 3:
            second += ' ' + split[2]
        yield name, f"{second}, {first} - Cryptography"

def test_function(func_name, args, expected_result, module, name):
    try:
        result = getattr(module, func_name)(*args)
        if result != expected_result:
            print(f'{name} code fails on {func_name}')
            return False
        return True
    except Exception as e:
        print(f"{name}'s {func_name} has exception {e}")
        return False

for name, directory in names_to_directories(names):
    first = name.split()[0]
    dir_path = os.path.join(os.getcwd(), directory)
    os.chdir(dir_path)
    if os.path.isdir(dir_path):
        try:
            spec = importlib.util.spec_from_file_location("functions", os.path.join(dir_path, "functions.py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"{name}'s code cannot import: {e}")
            
        passes_all = True
        
        passes_all &= test_function("block_encode", ['dog: 🐶', 4], [1685022522, 552640400, 3053453312], module, first)
        passes_all &= test_function("block_decode", [[1685022522, 552640400, 3053453312], 4], 'dog: 🐶', module, first)
        passes_all &= test_function("affine_encrypt", [[1685022522, 552640400, 3053453312], (123456789, 987654321), 4], [4115223155, 1183960961, 685664433], module, first)
        passes_all &= test_function("gcd", [2024, 748], 44, module, first)
        passes_all &= test_function("egcd", [2024, 748], (44, -7, 19), module, first)
        passes_all &= test_function("multiplicative_inverse", [33, 256], 225, module, first)
        passes_all &= test_function("affine_decrypt", [[4115223155, 1183960961, 685664433], (123456789, 987654321), 4], [1685022522, 552640400, 3053453312], module, first)
        
        if passes_all:
            print(f"All tests passed for {first}!")
    else:
        print(f"'{directory}' not found, ask {first}")
    print('')