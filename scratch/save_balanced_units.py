import sys
import pprint
sys.path.insert(0, '.')
from scratch.balance_questions import balance_unit_questions, UNIT1_QUESTIONS, UNIT2_QUESTIONS, UNIT3_QUESTIONS

u1 = balance_unit_questions(UNIT1_QUESTIONS, 1)
u2 = balance_unit_questions(UNIT2_QUESTIONS, 2)
u3 = balance_unit_questions(UNIT3_QUESTIONS, 3)

def write_unit_file(filename, var_name, data, unit_title):
    content = f"# {unit_title} - Exactly {len(data)} Questions\n"
    content += f"# Aligned with CMS Quarter 1 / NC SCOS\n\n"
    content += f"{var_name} = " + pprint.pformat(data, indent=4, width=120) + "\n"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {len(data)} questions to {filename}")

write_unit_file("scratch/unit1_questions.py", "UNIT1_QUESTIONS", u1, "Unit 1: Factors & Multiples (NC.4.OA.4)")
write_unit_file("scratch/unit2_questions.py", "UNIT2_QUESTIONS", u2, "Unit 2: Fraction Equivalence & Comparison (NC.4.NF.1, NC.4.NF.2)")
write_unit_file("scratch/unit3_questions.py", "UNIT3_QUESTIONS", u3, "Unit 3: Fraction Operations & Multiplication (NC.4.NF.3, NC.4.NF.4)")
