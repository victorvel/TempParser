import Parser

file_dict = {}

object = Parser.Parser(file_dict)

file_dict = object.ReadFile("0.6_YMnO3.mcif")

print("Example: ")
print("_chemical_formula_sum: ")
print(file_dict["_chemical_formula_sum"])