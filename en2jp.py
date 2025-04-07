def translate_text(input_file, output_file, cipher):
    """
    Translate English characters in input_file into Japaness, and output to output_file

    Args:
        input_file (str): input file name.
        output_file (str): output file name.
        cipher (dict): Mapping from English to Japaness.
    """

    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            count = 0
            for line in infile:
                translated_line = ""
                for char in line:
                    if char.isalpha() and char.upper() in cipher:
                        translated_line += cipher[char.upper()]
                    elif char == '"' and count%2 == 0:
                        translated_line += "「"
                        count += 1
                    elif char == '"' and count%2 != 0:
                        translated_line += "」"
                        count += 1 
                    elif char == "'" and count%2 == 0:
                        translated_line += "「"
                        count += 1
                    elif char == "'" and count%2 != 0:
                        translated_line += "」"
                        count += 1
                    elif char == "“":
                        translated_line += "「"
                    elif char == "”":
                        translated_line += "」"
                    else:
                        translated_line += char

                outfile.write(translated_line)

        print(f"Success! Output is saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Can't find file {input_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import  sys
    cipher = {
        'A': 'ム',
        'B': '乃',
        'C': 'て',
        'D': 'ワ',
        'E': 'モ',
        'F': 'ヂ',
        'G': 'ク',
        'H': 'カ',
        'I': 'エ',
        'J': 'ゴ',
        'K': 'ケ',
        'L': 'レ',
        'M': '巾',
        'N': 'ウ',
        'O': 'ロ',
        'P': 'ア',
        'Q': 'ヲ',
        'R': 'ャ',
        'S': 'ラ',
        'T': 'ナ',
        'U': 'リ',
        'V': 'Ｖ',
        'W': '山',
        'X': 'メ',
        'Y': 'ン',
        'Z': '乙'
    }


    if len(sys.argv) != 3:
        print("Usage: python jp2en.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    translate_text(input_file, output_file, cipher)