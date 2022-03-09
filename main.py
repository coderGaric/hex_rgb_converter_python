import re
from time import sleep


hexadecimal_table_str = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5,"6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}


def hex_to_rgb(code):
    code = code.upper()
    try:
        converted = [str(hexadecimal_table_str[code[i]] * 16 + hexadecimal_table_str[code[i + 1]]) \
                      for i in range(1, len(code) - 1, 2)]
    except KeyError: 
        return False, "Error: Not a valid hexadecimal color code"
    else:
        return True, f"rgb({', '.join(converted)})"


def rgb_to_hex(string):
    hexadecimal_table_int = {value: key for key, value in hexadecimal_table_str.items()}
    pattern = re.compile(r"\d{1,3}")

    extracted = [num for num in pattern.findall(string)]

    if len(extracted) == 3:
        try:
            converted = [f"{hexadecimal_table_int[int(int(num) / 16)]}{hexadecimal_table_int[int(num) % 16]}" \
                         for num in extracted]
        except KeyError: 
            return False, "Error: RGB numbers must be within 0 ~ 255"
        else:
            return True, f"#{''.join(converted)}"
    else:
        return False, ("Error: RGB numbers must be within 0 ~ 255")


def hex_rgb_converter():
    status = False
    
    while status == False:
        sleep(1)
        color_code = input("Enter a valid color code: ").strip()
        
        if color_code[0] == "#":
            if len(color_code) == 7:
                to_convert = hex_to_rgb(color_code)
                
                if to_convert[0]:
                    status = True
                else:
                    print(to_convert[1])
            else:
                print("Error: Hexadecimal color code must contained 6 char")
            
        elif color_code[0].lower() == "r":
            to_convert = rgb_to_hex(color_code)
            
            if to_convert[0]:
                status = True
            else:
                print(to_convert[1])
        else:
            print("Error: Not a valid color code")
        
    return to_convert[1]


print(hex_rgb_converter())