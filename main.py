def main():
    regular_expression = input()
    proteins = []
    number_of_proteins = int(input())
    for i in range(number_of_proteins):
        proteins.append(input())

    regex_parts = regular_expression.split("-")
    regex_parts_with_repeats_replaced = []

    for part in regex_parts:
        if '(' in part and ')' in part:
            repeat_number = int(part[part.find('(') + 1: part.find(')')])
        else:
            repeat_number = 1

        for i in range(repeat_number):
            regex_parts_with_repeats_replaced.append(part.replace('(' + repeat_number.__str__() + ')', ''))

    protein_match_mismatches = []
    for protein in proteins:
        result = ""
        for i, part in enumerate(regex_parts_with_repeats_replaced):
            if part == "X":
                result += '1'

            elif len(part) == 1:
                if protein[i] == part:
                    result += '1'
                else:
                    result += '0'

            elif part.startswith("[") and part.endswith("]"):
                alternative_residues = part[1: len(part)]
                if protein[i] in alternative_residues:
                    result += '1'
                else:
                    result += '0'

            elif part.startswith("{") and part.endswith("}"):
                excluded_residues = part[1: len(part)]
                if protein[i] not in excluded_residues:
                    result += '1'
                else:
                    result += '0'

        protein_match_mismatches.append(result)

    for result in protein_match_mismatches:
        number_of_mismatches = result.count('0')
        if number_of_mismatches <= 2:
            print("Yes ", result)
        else:
            print("No ", result)


if __name__ == '__main__':
    main()
