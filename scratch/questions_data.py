# Generator for 4th Grade Math Learning App
# Aligned with CMS Quarter 1 / NC SCOS (NC.4.OA.4, NC.4.NF.1, NC.4.NF.2, NC.4.NF.3, NC.4.NF.4)
import json

def get_questions_data():
    questions = [
        # =========================================================================
        # UNIT 1: FACTORS AND MULTIPLES (NC.4.OA.4)
        # =========================================================================
        # Easy Tier (6 questions: 2 MC, 2 Visual, 1 Number Line, 1 Drag-Drop)
        {
            "id": "u1_e1",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "visual",
            "question": "Which rectangular array shows a factor pair for the number 12? Select the grid model that forms an area of exactly 12 square units.",
            "visualCards": [
                {"id": "optA", "label": "Model A: 3 × 4 Array", "rows": 3, "cols": 4, "total": 12, "desc": "3 rows of 4 = 12"},
                {"id": "optB", "label": "Model B: 2 × 5 Array", "rows": 2, "cols": 5, "total": 10, "desc": "2 rows of 5 = 10"},
                {"id": "optC", "label": "Model C: 3 × 5 Array", "rows": 3, "cols": 5, "total": 15, "desc": "3 rows of 5 = 15"},
                {"id": "optD", "label": "Model D: 4 × 4 Array", "rows": 4, "cols": 4, "total": 16, "desc": "4 rows of 4 = 16"}
            ],
            "answerKey": "optA",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Count the total number of square tiles inside each rectangular grid (rows × columns).",
                "Multiply the length by the width for each model: 3 × 4 = 12, 2 × 5 = 10, 3 × 5 = 15, 4 × 4 = 16.",
                "Model A has 3 rows and 4 columns, giving an area of exactly 12 square units. Both 3 and 4 are factors of 12."
            ],
            "explanation": {
                "step1": "Understand: We need to find which rectangle has an area of exactly 12 square units.",
                "step2": "Model: Area is calculated by multiplying rows by columns: Area = Length × Width.",
                "step3": "Solve: For Model A, 3 × 4 = 12 square units. Model B has 10, Model C has 15, Model D has 16.",
                "step4": "Verify: Since 3 × 4 = 12, 3 and 4 form a valid factor pair for 12."
            }
        },
        {
            "id": "u1_e2",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "mc",
            "question": "Which of the following numbers is a factor of 18?",
            "options": [
                {"id": "A", "text": "3", "correct": True},
                {"id": "B", "text": "4", "correct": False},
                {"id": "C", "text": "5", "correct": False},
                {"id": "D", "text": "7", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "A factor divides a number evenly without leaving any remainder.",
                "Test each number: Does 18 ÷ 3 leave a remainder? What about 18 ÷ 4?",
                "18 ÷ 3 = 6 with 0 remainder. 3 × 6 = 18, so 3 is a factor of 18."
            ],
            "explanation": {
                "step1": "Understand: A factor is a whole number that divides 18 evenly with no remainder.",
                "step2": "Model: Check division for each option: 18 ÷ 3 = 6 (R 0); 18 ÷ 4 = 4 (R 2); 18 ÷ 5 = 3 (R 3); 18 ÷ 7 = 2 (R 4).",
                "step3": "Solve: Only 3 divides 18 with zero remainder (3 × 6 = 18).",
                "step4": "Verify: 3 and 6 are a factor pair for 18."
            }
        },
        {
            "id": "u1_e3",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "mc",
            "question": "Which of the following numbers is a multiple of 6?",
            "options": [
                {"id": "A", "text": "16", "correct": False},
                {"id": "B", "text": "24", "correct": True},
                {"id": "C", "text": "26", "correct": False},
                {"id": "D", "text": "32", "correct": False}
            ],
            "answerKey": "B",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "A multiple of 6 is the product of 6 and any counting number (skip-counting by 6).",
                "Skip count by 6: 6, 12, 18, 24, 30, 36...",
                "24 appears in the sequence because 6 × 4 = 24."
            ],
            "explanation": {
                "step1": "Understand: We need a number that can be reached by skip-counting by 6.",
                "step2": "Model: Multiples of 6: 6 × 1 = 6, 6 × 2 = 12, 6 × 3 = 18, 6 × 4 = 24, 6 × 5 = 30.",
                "step3": "Solve: 24 is 6 × 4.",
                "step4": "Verify: 24 ÷ 6 = 4 with no remainder, so 24 is a multiple of 6."
            }
        },
        {
            "id": "u1_e4",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "visual",
            "question": "Which equal-group model proves that 5 is a factor of 15 because it partitions 15 items with zero remainder?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 3 groups of 5 stars (0 leftover)", "groups": 3, "size": 5, "rem": 0, "total": 15},
                {"id": "optB", "label": "Model B: 2 groups of 6 stars (3 leftover)", "groups": 2, "size": 6, "rem": 3, "total": 15},
                {"id": "optC", "label": "Model C: 4 groups of 3 stars (3 leftover)", "groups": 4, "size": 3, "rem": 3, "total": 15},
                {"id": "optD", "label": "Model D: 2 groups of 7 stars (1 leftover)", "groups": 2, "size": 7, "rem": 1, "total": 15}
            ],
            "answerKey": "optA",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "A factor divides items into equal groups with NO leftovers (remainder = 0).",
                "Notice Model A has exactly 3 groups of 5 with 0 leftovers.",
                "3 × 5 = 15. Since there are 0 leftovers, 5 is a factor of 15."
            ],
            "explanation": {
                "step1": "Understand: Equal grouping tests whether a number divides evenly.",
                "step2": "Model: 15 items arranged into groups of 5.",
                "step3": "Solve: 15 ÷ 5 = 3 equal groups with 0 items remaining.",
                "step4": "Verify: Because the remainder is zero, 5 and 3 are factors of 15."
            }
        },
        {
            "id": "u1_e5",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "numberline",
            "question": "On the number line from 0 to 20, tap to plot the multiple of 5 that is between 12 and 18.",
            "lineData": {"min": 0, "max": 20, "step": 1, "target": 15, "label": "Multiple of 5"},
            "answerKey": 15,
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "List the multiples of 5: 5, 10, 15, 20...",
                "Find which of these numbers is greater than 12 and less than 18.",
                "15 is between 12 and 18 because 5 × 3 = 15."
            ],
            "explanation": {
                "step1": "Understand: We need a multiple of 5 strictly between 12 and 18.",
                "step2": "Model: 5 × 1 = 5, 5 × 2 = 10, 5 × 3 = 15, 5 × 4 = 20.",
                "step3": "Solve: 15 is between 12 and 18.",
                "step4": "Verify: 12 < 15 < 18, and 15 is a multiple of 5."
            }
        },
        {
            "id": "u1_e6",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "easy",
            "format": "dragdrop",
            "question": "Drag each number card into the correct category box: Prime or Composite.",
            "dragData": {
                "items": [{"id": "c1", "val": 5}, {"id": "c2", "val": 6}],
                "targets": [
                    {"id": "primeBox", "name": "Prime Number Box", "expected": ["c1"]},
                    {"id": "compBox", "name": "Composite Number Box", "expected": ["c2"]}
                ]
            },
            "answerKey": {"primeBox": ["c1"], "compBox": ["c2"]},
            "misconceptionKey": "prime_composite_error",
            "hints": [
                "A prime number has EXACTLY two unique factors: 1 and itself.",
                "5 has factors 1 and 5 only (prime). 6 has factors 1, 2, 3, 6 (composite).",
                "Put 5 in Prime and 6 in Composite."
            ],
            "explanation": {
                "step1": "Understand: Prime numbers have only two factors; composite numbers have more than two.",
                "step2": "Model: 5 = 1 × 5 (2 factors). 6 = 1 × 6 and 2 × 3 (4 factors).",
                "step3": "Solve: 5 is Prime; 6 is Composite.",
                "step4": "Verify: 5 has no divisors other than 1 and 5."
            }
        },

        # Medium Tier (8 questions: 2 MC, 2 Visual, 2 Number Line, 2 Drag-Drop)
        {
            "id": "u1_m1",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "mc",
            "question": "Which list contains ALL of the factor pairs for 24?",
            "options": [
                {"id": "A", "text": "1 × 24, 2 × 12, 3 × 8, 4 × 6", "correct": True},
                {"id": "B", "text": "1 × 24, 3 × 8, 4 × 6", "correct": False},
                {"id": "C", "text": "2 × 12, 4 × 6", "correct": False},
                {"id": "D", "text": "1 × 24, 2 × 12, 3 × 9", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Check sequentially starting with 1: 1 × 24, then 2: 2 × 12, then 3: 3 × 8, then 4: 4 × 6.",
                "Make sure no factor pairs are missing (Option B misses 2 × 12, Option C misses 1 × 24 and 3 × 8).",
                "Option A lists all 4 factor pairs for 24: 1 × 24, 2 × 12, 3 × 8, 4 × 6."
            ],
            "explanation": {
                "step1": "Understand: We must find every pair of whole numbers whose product is 24.",
                "step2": "Model: Test systematically: 24 ÷ 1 = 24, 24 ÷ 2 = 12, 24 ÷ 3 = 8, 24 ÷ 4 = 6. 5 is not a factor.",
                "step3": "Solve: The complete list of factor pairs is 1 × 24, 2 × 12, 3 × 8, 4 × 6.",
                "step4": "Verify: Each product equals 24, and no factors are omitted."
            }
        },
        {
            "id": "u1_m2",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "numberline",
            "question": "Plot points on the number line to show the first four multiples of 7 starting at 7.",
            "lineData": {"min": 0, "max": 35, "step": 1, "target": [7, 14, 21, 28], "multi": True, "label": "Multiples of 7"},
            "answerKey": [7, 14, 21, 28],
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Skip-count by 7 starting at 7: 7 × 1, 7 × 2, 7 × 3, 7 × 4.",
                "7 × 1 = 7, 7 × 2 = 14, 7 × 3 = 21, 7 × 4 = 28.",
                "Plot the four points: 7, 14, 21, and 28."
            ],
            "explanation": {
                "step1": "Understand: Multiples are generated by multiplying 7 by 1, 2, 3, and 4.",
                "step2": "Model: 7 × 1 = 7, 7 × 2 = 14, 7 × 3 = 21, 7 × 4 = 28.",
                "step3": "Solve: The points on the number line are 7, 14, 21, and 28.",
                "step4": "Verify: Each step represents an equal jump of +7."
            }
        },
        {
            "id": "u1_m3",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "mc",
            "question": "Is 51 a prime or composite number, and why?",
            "options": [
                {"id": "A", "text": "Composite, because 3 × 17 = 51", "correct": True},
                {"id": "B", "text": "Prime, because it is an odd number", "correct": False},
                {"id": "C", "text": "Prime, because it ends in 1", "correct": False},
                {"id": "D", "text": "Neither prime nor composite", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "prime_composite_error",
            "hints": [
                "Not all odd numbers are prime! Test if 51 is divisible by 3 (add digits: 5 + 1 = 6, which is divisible by 3).",
                "51 ÷ 3 = 17 with 0 remainder.",
                "Since 51 has factors 1, 3, 17, and 51 (more than 2 factors), it is composite."
            ],
            "explanation": {
                "step1": "Understand: A composite number has more than two factors.",
                "step2": "Model: Test divisibility by 3: 5 + 1 = 6. 51 ÷ 3 = 17.",
                "step3": "Solve: 3 × 17 = 51. The factors of 51 are 1, 3, 17, 51.",
                "step4": "Verify: Having 4 factors proves 51 is composite, not prime."
            }
        },
        {
            "id": "u1_m4",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "visual",
            "question": "Which rectangular area model shows that 36 has a factor pair of equal length and width (forming a square)?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 6 × 6 Square Array", "rows": 6, "cols": 6, "total": 36, "desc": "6 × 6 = 36"},
                {"id": "optB", "label": "Model B: 4 × 9 Rectangular Array", "rows": 4, "cols": 9, "total": 36, "desc": "4 × 9 = 36"},
                {"id": "optC", "label": "Model C: 3 × 12 Rectangular Array", "rows": 3, "cols": 12, "total": 36, "desc": "3 × 12 = 36"},
                {"id": "optD", "label": "Model D: 5 × 7 Rectangular Array", "rows": 5, "cols": 7, "total": 35, "desc": "5 × 7 = 35"}
            ],
            "answerKey": "optA",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "A square has equal length and width (rows = columns).",
                "Which model has both rows and columns equal to 6?",
                "6 × 6 = 36 forms a square array, showing 6 is a factor of 36."
            ],
            "explanation": {
                "step1": "Understand: A square array has side lengths that are identical: side × side = area.",
                "step2": "Model: Model A has 6 rows and 6 columns: 6 × 6 = 36.",
                "step3": "Solve: 6 × 6 = 36 is a square array.",
                "step4": "Verify: 36 is a square number with factor pair (6, 6)."
            }
        },
        {
            "id": "u1_m5",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "visual",
            "question": "Which factor rainbow diagram correctly connects all pairs of factors for the number 16?",
            "visualCards": [
                {"id": "optA", "label": "Rainbow A: (1 × 16), (2 × 8), (4 × 4)", "pairs": "1-16, 2-8, 4-4", "correct": True},
                {"id": "optB", "label": "Rainbow B: (1 × 16), (3 × 5)", "pairs": "1-16, 3-5", "correct": False},
                {"id": "optC", "label": "Rainbow C: (2 × 8), (3 × 6)", "pairs": "2-8, 3-6", "correct": False},
                {"id": "optD", "label": "Rainbow D: (1 × 16) only", "pairs": "1-16 only", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Find all pairs of numbers that multiply to 16: 1 × 16, 2 × 8, 4 × 4.",
                "Notice 3 is not a factor of 16 (3 × 5 = 15).",
                "Rainbow A connects 1 with 16, 2 with 8, and 4 with 4."
            ],
            "explanation": {
                "step1": "Understand: Factor rainbows link matching factor pairs from outside inward.",
                "step2": "Model: 1 × 16 = 16, 2 × 8 = 16, 4 × 4 = 16.",
                "step3": "Solve: Rainbow A correctly shows all pairs (1, 16), (2, 8), and (4, 4).",
                "step4": "Verify: The complete factor set for 16 is {1, 2, 4, 8, 16}."
            }
        },
        {
            "id": "u1_m6",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "numberline",
            "question": "Plot the number on the number line that is a common multiple of BOTH 3 and 4 between 20 and 30.",
            "lineData": {"min": 15, "max": 35, "step": 1, "target": 24, "label": "Common Multiple"},
            "answerKey": 24,
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Multiples of 3: 18, 21, 24, 27, 30. Multiples of 4: 16, 20, 24, 28, 32.",
                "Find the number in both lists that lies between 20 and 30.",
                "24 is in both lists (3 × 8 = 24 and 4 × 6 = 24)."
            ],
            "explanation": {
                "step1": "Understand: A common multiple is a number that is a multiple of both 3 and 4.",
                "step2": "Model: Multiples of 3: 21, 24, 27. Multiples of 4: 20, 24, 28.",
                "step3": "Solve: 24 is shared by both and satisfies 20 < 24 < 30.",
                "step4": "Verify: 24 ÷ 3 = 8 and 24 ÷ 4 = 6 with 0 remainder."
            }
        },
        {
            "id": "u1_m7",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Sort each number card: Is it a Factor of 30 or a Multiple of 30?",
            "dragData": {
                "items": [
                    {"id": "n5", "val": 5},
                    {"id": "n6", "val": 6},
                    {"id": "n60", "val": 60},
                    {"id": "n90", "val": 90}
                ],
                "targets": [
                    {"id": "factorBox", "name": "Factors of 30", "expected": ["n5", "n6"]},
                    {"id": "multipleBox", "name": "Multiples of 30", "expected": ["n60", "n90"]}
                ]
            },
            "answerKey": {"factorBox": ["n5", "n6"], "multipleBox": ["n60", "n90"]},
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Factors of 30 divide into 30 (they are smaller than or equal to 30).",
                "Multiples of 30 are produced by multiplying 30 (they are equal to or larger than 30).",
                "5 and 6 are factors (5 × 6 = 30). 60 and 90 are multiples (30 × 2 = 60, 30 × 3 = 90)."
            ],
            "explanation": {
                "step1": "Understand: Factors divide into 30; multiples are products of 30.",
                "step2": "Model: 30 ÷ 5 = 6 and 30 ÷ 6 = 5 (factors). 30 × 2 = 60 and 30 × 3 = 90 (multiples).",
                "step3": "Solve: Factors of 30: 5, 6. Multiples of 30: 60, 90.",
                "step4": "Verify: Factors are ≤ 30, while multiples are ≥ 30."
            }
        },
        {
            "id": "u1_m8",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Drag the correct factor card to complete the equation: 5 × [ ? ] = 40.",
            "dragData": {
                "items": [
                    {"id": "c6", "val": 6},
                    {"id": "c7", "val": 7},
                    {"id": "c8", "val": 8},
                    {"id": "c9", "val": 9}
                ],
                "targets": [
                    {"id": "slot1", "name": "Missing Factor Slot", "expected": ["c8"]}
                ]
            },
            "answerKey": {"slot1": ["c8"]},
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Ask yourself: 5 times what number equals 40?",
                "Use division to find the missing factor: 40 ÷ 5 = ?",
                "40 ÷ 5 = 8, so 5 × 8 = 40."
            ],
            "explanation": {
                "step1": "Understand: We need the missing factor in the factor pair for 40 with 5.",
                "step2": "Model: 5 × ? = 40 means ? = 40 ÷ 5.",
                "step3": "Solve: 40 ÷ 5 = 8.",
                "step4": "Verify: 5 × 8 = 40, so 8 is the correct factor."
            }
        },

        # Hard Tier (6 questions: 1 MC, 1 Visual, 2 Number Line, 2 Drag-Drop)
        {
            "id": "u1_h1",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "dragdrop",
            "question": "Drag each number card into the correct category box: Prime or Composite. Numbers to sort: 2, 9, 13, 21, 29, 33.",
            "dragData": {
                "items": [
                    {"id": "n2", "val": 2},
                    {"id": "n9", "val": 9},
                    {"id": "n13", "val": 13},
                    {"id": "n21", "val": 21},
                    {"id": "n29", "val": 29},
                    {"id": "n33", "val": 33}
                ],
                "targets": [
                    {"id": "primeBox", "name": "Prime Box", "expected": ["n2", "n13", "n29"]},
                    {"id": "compBox", "name": "Composite Box", "expected": ["n9", "n21", "n33"]}
                ]
            },
            "answerKey": {"primeBox": ["n2", "n13", "n29"], "compBox": ["n9", "n21", "n33"]},
            "misconceptionKey": "prime_composite_error",
            "hints": [
                "2 is the only even prime number (factors: 1, 2).",
                "9 (3 × 3), 21 (3 × 7), and 33 (3 × 11) all have more than 2 factors, so they are composite.",
                "Prime Box = {2, 13, 29}; Composite Box = {9, 21, 33}."
            ],
            "explanation": {
                "step1": "Understand: Categorize each number based on whether it has exactly 2 factors (prime) or more than 2 factors (composite).",
                "step2": "Model: Factors of 2: {1, 2}. Factors of 9: {1, 3, 9}. Factors of 13: {1, 13}. Factors of 21: {1, 3, 7, 21}. Factors of 29: {1, 29}. Factors of 33: {1, 3, 11, 33}.",
                "step3": "Solve: Prime Box = {2, 13, 29}; Composite Box = {9, 21, 33}.",
                "step4": "Verify: Exactly 3 numbers in Prime and 3 numbers in Composite."
            }
        },
        {
            "id": "u1_h2",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "mc",
            "question": "Maya arranges 42 square desks into a rectangular array with equal rows and columns and no desks leftover. Which of the following CANNOT be the number of rows?",
            "options": [
                {"id": "A", "text": "4 rows", "correct": True},
                {"id": "B", "text": "6 rows", "correct": False},
                {"id": "C", "text": "7 rows", "correct": False},
                {"id": "D", "text": "14 rows", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "The number of rows must be a factor of 42 (must divide 42 evenly).",
                "Test 42 ÷ 4, 42 ÷ 6, 42 ÷ 7, and 42 ÷ 14.",
                "42 ÷ 4 = 10 with a remainder of 2. 4 is NOT a factor of 42."
            ],
            "explanation": {
                "step1": "Understand: A full rectangular array requires the row count to divide 42 with zero remainder.",
                "step2": "Model: 42 ÷ 6 = 7 (R 0); 42 ÷ 7 = 6 (R 0); 42 ÷ 14 = 3 (R 0); 42 ÷ 4 = 10 (R 2).",
                "step3": "Solve: 4 rows would leave 2 desks left over.",
                "step4": "Verify: 4 is not a factor of 42."
            }
        },
        {
            "id": "u1_h3",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "visual",
            "question": "Which factor diagram correctly shows ALL 12 factors for the number 60?",
            "visualCards": [
                {"id": "optA", "label": "Model A: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}", "factors": "1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60", "correct": True},
                {"id": "optB", "label": "Model B: {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 30, 60}", "factors": "Includes 8 (incorrect)", "correct": False},
                {"id": "optC", "label": "Model C: {1, 2, 3, 5, 6, 10, 15, 20, 30, 60}", "factors": "Missing 4 and 12", "correct": False},
                {"id": "optD", "label": "Model D: {1, 3, 5, 10, 20, 30, 60}", "factors": "Missing all even factors below 10", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "Find all factor pairs for 60: 1 × 60, 2 × 30, 3 × 20, 4 × 15, 5 × 12, 6 × 10.",
                "Notice that 8 is NOT a factor of 60 (60 ÷ 8 = 7 R 4), which rules out Model B.",
                "Model A includes all 12 factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60."
            ],
            "explanation": {
                "step1": "Understand: We need the complete set of factors for 60.",
                "step2": "Model: Factor pairs: 1×60, 2×30, 3×20, 4×15, 5×12, 6×10.",
                "step3": "Solve: The full list has 12 factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.",
                "step4": "Verify: Model A contains every valid factor without extras."
            }
        },
        {
            "id": "u1_h4",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "numberline",
            "question": "Plot ALL prime numbers between 20 and 35 on the number line.",
            "lineData": {"min": 20, "max": 35, "step": 1, "target": [23, 29, 31], "multi": True, "label": "Prime Numbers"},
            "answerKey": [23, 29, 31],
            "misconceptionKey": "prime_composite_error",
            "hints": [
                "Check odd numbers: 21 (3 × 7), 23 (prime), 25 (5 × 5), 27 (3 × 9), 29 (prime), 31 (prime), 33 (3 × 11), 35 (5 × 7).",
                "The only numbers with exactly two factors in this range are 23, 29, and 31.",
                "Plot the three points: 23, 29, and 31."
            ],
            "explanation": {
                "step1": "Understand: Identify all numbers between 20 and 35 that have no factors other than 1 and themselves.",
                "step2": "Model: Eliminate composites: 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35.",
                "step3": "Solve: The remaining numbers are 23, 29, and 31.",
                "step4": "Verify: None of 23, 29, 31 can be divided evenly by 2, 3, or 5."
            }
        },
        {
            "id": "u1_h5",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "numberline",
            "question": "Plot the Least Common Multiple (LCM) of 6 and 8 on the number line.",
            "lineData": {"min": 0, "max": 40, "step": 2, "target": 24, "label": "LCM of 6 and 8"},
            "answerKey": 24,
            "misconceptionKey": "factor_multiple_confuse",
            "hints": [
                "List multiples of 6: 6, 12, 18, 24, 30, 36, 42, 48.",
                "List multiples of 8: 8, 16, 24, 32, 40, 48.",
                "The smallest number that appears in BOTH lists is 24."
            ],
            "explanation": {
                "step1": "Understand: The Least Common Multiple is the smallest non-zero multiple shared by both numbers.",
                "step2": "Model: Multiples of 6: 6, 12, 18, 24... Multiples of 8: 8, 16, 24...",
                "step3": "Solve: 24 is the smallest shared multiple.",
                "step4": "Verify: 24 ÷ 6 = 4 and 24 ÷ 8 = 3."
            }
        },
        {
            "id": "u1_h6",
            "unit": 1,
            "unitName": "Unit 1: Factors and Multiples",
            "standard": "NC.4.OA.4",
            "difficulty": "hard",
            "format": "dragdrop",
            "question": "Sort each number into: Numbers with EXACTLY 3 factors vs Numbers with MORE than 3 factors.",
            "dragData": {
                "items": [
                    {"id": "n4", "val": 4},
                    {"id": "n9", "val": 9},
                    {"id": "n12", "val": 12},
                    {"id": "n18", "val": 18}
                ],
                "targets": [
                    {"id": "box3", "name": "Exactly 3 Factors", "expected": ["n4", "n9"]},
                    {"id": "boxMore", "name": "More Than 3 Factors", "expected": ["n12", "n18"]}
                ]
            },
            "answerKey": {"box3": ["n4", "n9"], "boxMore": ["n12", "n18"]},
            "misconceptionKey": "prime_composite_error",
            "hints": [
                "Find factors of each: 4 has {1, 2, 4} (3 factors). 9 has {1, 3, 9} (3 factors).",
                "12 has {1, 2, 3, 4, 6, 12} (6 factors). 18 has {1, 2, 3, 6, 9, 18} (6 factors).",
                "4 and 9 go into 'Exactly 3 Factors'. 12 and 18 go into 'More Than 3 Factors'."
            ],
            "explanation": {
                "step1": "Understand: Count the total number of distinct factors for each number.",
                "step2": "Model: Squares of prime numbers (p²) always have exactly 3 factors: 1, p, and p².",
                "step3": "Solve: 4 (2²) has 3 factors. 9 (3²) has 3 factors. 12 and 18 have 6 factors each.",
                "step4": "Verify: 4 and 9 fit the 3-factor category."
            }
        },

        # =========================================================================
        # UNIT 2: FRACTION EQUIVALENCE AND COMPARISON (NC.4.NF.1 & NC.4.NF.2)
        # =========================================================================
        # Easy Tier (6 questions: 2 MC, 2 Visual, 1 Number Line, 1 Drag-Drop)
        {
            "id": "u2_e1",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "easy",
            "format": "visual",
            "question": "Select the fraction strip model that shows a fraction equivalent to 2/3.",
            "visualCards": [
                {"id": "optA", "label": "Model A: 4/6 Strip", "num": 4, "den": 6, "val": "4/6", "desc": "4 out of 6 parts shaded"},
                {"id": "optB", "label": "Model B: 3/6 Strip", "num": 3, "den": 6, "val": "3/6", "desc": "3 out of 6 parts shaded"},
                {"id": "optC", "label": "Model C: 2/4 Strip", "num": 2, "den": 4, "val": "2/4", "desc": "2 out of 4 parts shaded"},
                {"id": "optD", "label": "Model D: 5/8 Strip", "num": 5, "den": 8, "val": "5/8", "desc": "5 out of 8 parts shaded"}
            ],
            "answerKey": "optA",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Multiply both numerator and denominator of 2/3 by 2.",
                "(2 × 2) / (3 × 2) = 4/6.",
                "Model A has 4 out of 6 parts shaded, which covers the exact same length as 2/3."
            ],
            "explanation": {
                "step1": "Understand: We need a fraction that represents the same amount as 2/3.",
                "step2": "Model: When each 1/3 part is cut in half, 2 parts become 4, and 3 parts become 6.",
                "step3": "Solve: 2/3 = (2 × 2)/(3 × 2) = 4/6.",
                "step4": "Verify: Model A represents 4/6, which is equivalent to 2/3."
            }
        },
        {
            "id": "u2_e2",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "easy",
            "format": "mc",
            "question": "Which fraction is equivalent to 1/2?",
            "options": [
                {"id": "A", "text": "5/10", "correct": True},
                {"id": "B", "text": "3/8", "correct": False},
                {"id": "C", "text": "4/6", "correct": False},
                {"id": "D", "text": "2/5", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "benchmark_half",
            "hints": [
                "In a fraction equivalent to 1/2, the numerator is exactly half of the denominator.",
                "What is half of 10? Half of 10 is 5.",
                "5/10 is equivalent to 1/2 because (1 × 5) / (2 × 5) = 5/10."
            ],
            "explanation": {
                "step1": "Understand: A fraction equals 1/2 if its numerator is half its denominator.",
                "step2": "Model: Half of 10 is 5; half of 8 is 4; half of 6 is 3.",
                "step3": "Solve: 5/10 has numerator 5, which is exactly half of 10.",
                "step4": "Verify: 5/10 = 1/2."
            }
        },
        {
            "id": "u2_e3",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "easy",
            "format": "mc",
            "question": "Which of the following fractions is GREATER than the benchmark fraction 1/2?",
            "options": [
                {"id": "A", "text": "5/8", "correct": True},
                {"id": "B", "text": "2/6", "correct": False},
                {"id": "C", "text": "3/10", "correct": False},
                {"id": "D", "text": "1/4", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Find 1/2 of each denominator: half of 8 is 4; half of 6 is 3; half of 10 is 5; half of 4 is 2.",
                "Compare each numerator to half of its denominator.",
                "For 5/8, the numerator 5 is greater than 4, so 5/8 > 1/2."
            ],
            "explanation": {
                "step1": "Understand: Compare each fraction to the benchmark 1/2.",
                "step2": "Model: 1/2 = 4/8, 3/6, 5/10, 2/4.",
                "step3": "Solve: 5/8 > 4/8 (greater than 1/2). 2/6 < 3/6, 3/10 < 5/10, 1/4 < 2/4.",
                "step4": "Verify: 5/8 is the only fraction greater than 1/2."
            }
        },
        {
            "id": "u2_e4",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "easy",
            "format": "visual",
            "question": "Which area model shows 3/4 partitioned horizontally into 6/8 by splitting each fourth into 2 equal parts?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 6 out of 8 grid cells shaded", "rows": 2, "cols": 4, "shaded": 6, "total": 8},
                {"id": "optB", "label": "Model B: 3 out of 5 grid cells shaded", "rows": 1, "cols": 5, "shaded": 3, "total": 5},
                {"id": "optC", "label": "Model C: 2 out of 6 grid cells shaded", "rows": 2, "cols": 3, "shaded": 2, "total": 6},
                {"id": "optD", "label": "Model D: 4 out of 8 grid cells shaded", "rows": 2, "cols": 4, "shaded": 4, "total": 8}
            ],
            "answerKey": "optA",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Start with 3 vertical columns shaded out of 4.",
                "When you draw a horizontal line across, 3 columns become 6 cells, and 4 columns become 8 cells.",
                "Model A has 6 shaded cells out of 8 total cells."
            ],
            "explanation": {
                "step1": "Understand: Partitioning an area model multiplies numerator and denominator by the same number.",
                "step2": "Model: 3/4 × 2/2 = 6/8.",
                "step3": "Solve: Model A shows a 2 × 4 grid with 6 cells shaded, representing 6/8.",
                "step4": "Verify: 6/8 is equivalent to 3/4."
            }
        },
        {
            "id": "u2_e5",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "easy",
            "format": "numberline",
            "question": "On the number line from 0 to 1 partitioned into 4 equal intervals, tap to place a point on 2/4.",
            "lineData": {"min": 0, "max": 1, "step": 0.25, "target": 0.5, "label": "2/4 (or 1/2)"},
            "answerKey": 0.5,
            "misconceptionKey": "benchmark_half",
            "hints": [
                "The number line is divided into 4 equal segments: 0, 1/4, 2/4, 3/4, 4/4.",
                "Count 2 hops from 0 to reach 2/4.",
                "2/4 is exactly in the middle of 0 and 1 (equal to 1/2)."
            ],
            "explanation": {
                "step1": "Understand: Plot 2/4 on a fourths number line.",
                "step2": "Model: 0 -> 1/4 -> 2/4 -> 3/4 -> 1.",
                "step3": "Solve: 2/4 is at coordinate 0.5.",
                "step4": "Verify: 2/4 is halfway between 0 and 1."
            }
        },
        {
            "id": "u2_e6",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "easy",
            "format": "dragdrop",
            "question": "Drag the correct comparison symbol (<, >, or =) to make the statement true: 3/8 ○ 5/8.",
            "dragData": {
                "items": [
                    {"id": "symLess", "val": "<"},
                    {"id": "symGreater", "val": ">"},
                    {"id": "symEqual", "val": "="}
                ],
                "targets": [
                    {"id": "compareCircle", "name": "Comparison Circle", "expected": ["symLess"]}
                ]
            },
            "answerKey": {"compareCircle": ["symLess"]},
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Both fractions have the same denominator (8), meaning the unit pieces are identical in size.",
                "Compare the numerators: Is 3 less than or greater than 5?",
                "3 is less than 5, so 3/8 < 5/8."
            ],
            "explanation": {
                "step1": "Understand: Compare fractions with like denominators.",
                "step2": "Model: Both represent eighths of the same whole.",
                "step3": "Solve: 3 eighths is less than 5 eighths (3 < 5).",
                "step4": "Verify: 3/8 < 5/8."
            }
        },

        # Medium Tier (8 questions: 2 MC, 2 Visual, 2 Number Line, 2 Drag-Drop)
        {
            "id": "u2_m1",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Drag the correct comparison symbol (<, >, or =) into the circle to make the statement true: 3/5 ○ 4/10.",
            "dragData": {
                "items": [
                    {"id": "symLess", "val": "<"},
                    {"id": "symGreater", "val": ">"},
                    {"id": "symEqual", "val": "="}
                ],
                "targets": [
                    {"id": "compareCircle", "name": "Comparison Circle", "expected": ["symGreater"]}
                ]
            },
            "answerKey": {"compareCircle": ["symGreater"]},
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Convert 3/5 to tenths by multiplying numerator and denominator by 2.",
                "3/5 = (3 × 2) / (5 × 2) = 6/10.",
                "Now compare 6/10 and 4/10: 6/10 > 4/10, so 3/5 > 4/10."
            ],
            "explanation": {
                "step1": "Understand: We need to compare 3/5 and 4/10 with different denominators.",
                "step2": "Model: Find a common denominator: 5 × 2 = 10, so 3/5 = 6/10.",
                "step3": "Solve: Since 6/10 > 4/10, 3/5 > 4/10.",
                "step4": "Verify: You can also use benchmarks: 3/5 > 1/2 while 4/10 < 1/2."
            }
        },
        {
            "id": "u2_m2",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "medium",
            "format": "numberline",
            "question": "Place a point on the number line below to plot a fraction equivalent to 3/4 with a denominator of 12.",
            "lineData": {"min": 0, "max": 1, "step": 0.08333333333333333, "target": 0.75, "label": "9/12 (Equivalent to 3/4)"},
            "answerKey": 0.75,
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Find what you multiply 4 by to get 12: 4 × 3 = 12.",
                "Multiply the numerator 3 by the same number 3: 3 × 3 = 9.",
                "The equivalent fraction is 9/12. On a line with 12 ticks, plot at tick 9 (0.75)."
            ],
            "explanation": {
                "step1": "Understand: Find the fraction equivalent to 3/4 that has a denominator of 12.",
                "step2": "Model: 3/4 = (3 × 3) / (4 × 3) = 9/12.",
                "step3": "Solve: On a 12-segment number line, the 9th mark represents 9/12 = 0.75.",
                "step4": "Verify: 9/12 simplifies back to 3/4."
            }
        },
        {
            "id": "u2_m3",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "medium",
            "format": "mc",
            "question": "How can you generate a fraction equivalent to 2/5 with a denominator of 10?",
            "options": [
                {"id": "A", "text": "Multiply both numerator and denominator by 2", "correct": True},
                {"id": "B", "text": "Add 5 to both numerator and denominator", "correct": False},
                {"id": "C", "text": "Multiply numerator by 2 and denominator by 5", "correct": False},
                {"id": "D", "text": "Add 2 to the numerator only", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Adding to numerator and denominator changes the value of the fraction!",
                "To keep the fraction equivalent, multiply both parts by the SAME number (multiplying by 2/2 = 1).",
                "(2 × 2) / (5 × 2) = 4/10."
            ],
            "explanation": {
                "step1": "Understand: Equivalent fractions must maintain the exact same ratio of parts to whole.",
                "step2": "Model: Multiplying numerator and denominator by n multiplies the fraction by n/n = 1.",
                "step3": "Solve: Multiply 2 and 5 by 2 to get 4/10.",
                "step4": "Verify: Adding numbers (like 2+5 / 5+5 = 7/10) alters the ratio incorrectly."
            }
        },
        {
            "id": "u2_m4",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "medium",
            "format": "mc",
            "question": "Which statement correctly compares 3/10 and 3/8?",
            "options": [
                {"id": "A", "text": "3/8 > 3/10 because eighths are larger pieces than tenths", "correct": True},
                {"id": "B", "text": "3/10 > 3/8 because 10 is greater than 8", "correct": False},
                {"id": "C", "text": "3/10 = 3/8 because both numerators are 3", "correct": False},
                {"id": "D", "text": "3/8 < 3/10 because 8 is smaller than 10", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Both fractions have the SAME numerator (3 pieces).",
                "When a whole is divided into 8 pieces, each piece is LARGER than when divided into 10 pieces.",
                "3 larger pieces is greater than 3 smaller pieces: 3/8 > 3/10."
            ],
            "explanation": {
                "step1": "Understand: When numerators are equal, compare the piece sizes (denominators).",
                "step2": "Model: 1/8 > 1/10 because dividing a whole into fewer parts makes each part larger.",
                "step3": "Solve: Therefore, 3 eighths is greater than 3 tenths: 3/8 > 3/10.",
                "step4": "Verify: 3/8 = 0.375 and 3/10 = 0.30; 0.375 > 0.30."
            }
        },
        {
            "id": "u2_m5",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "medium",
            "format": "visual",
            "question": "Which tape diagram correctly shows why 4/12 is equivalent to 1/3?",
            "visualCards": [
                {"id": "optA", "label": "Model A: Tape of 12 (4 shaded) aligned with Tape of 3 (1 shaded)", "numA": 4, "denA": 12, "numB": 1, "denB": 3, "correct": True},
                {"id": "optB", "label": "Model B: Tape of 12 (3 shaded) aligned with Tape of 3 (1 shaded)", "numA": 3, "denA": 12, "numB": 1, "denB": 3, "correct": False},
                {"id": "optC", "label": "Model C: Tape of 10 (4 shaded)", "numA": 4, "denA": 10, "numB": 1, "denB": 3, "correct": False},
                {"id": "optD", "label": "Model D: Tape of 8 (2 shaded)", "numA": 2, "denA": 8, "numB": 1, "denB": 3, "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Simplify 4/12: Divide 4 and 12 by 4: (4 ÷ 4) / (12 ÷ 4) = 1/3.",
                "The shaded portion of 4 twelfths must match the exact length of 1 third.",
                "Model A shows 4 twelfths perfectly aligned with 1 third."
            ],
            "explanation": {
                "step1": "Understand: Equivalent fraction tape diagrams have identical shaded lengths.",
                "step2": "Model: 4/12 = 1/3 because each third contains 4 twelfths.",
                "step3": "Solve: Model A aligns 4 shaded twelfths with 1 shaded third.",
                "step4": "Verify: 4/12 = 1/3."
            }
        },
        {
            "id": "u2_m6",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "medium",
            "format": "visual",
            "question": "Which pair of visual fraction models shows two EQUIVALENT fractions?",
            "visualCards": [
                {"id": "optA", "label": "Pair A: 2/4 and 50/100 (both equal 1/2)", "correct": True},
                {"id": "optB", "label": "Pair B: 2/3 and 3/4", "correct": False},
                {"id": "optC", "label": "Pair C: 3/5 and 3/8", "correct": False},
                {"id": "optD", "label": "Pair D: 4/6 and 5/12", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Check the value of each: 2/4 = 1/2.",
                "What is 50/100? 50 is half of 100, so 50/100 = 1/2.",
                "Since both 2/4 and 50/100 equal 1/2, Pair A is equivalent."
            ],
            "explanation": {
                "step1": "Understand: Equivalent fractions represent the exact same value.",
                "step2": "Model: 2/4 = 1/2. 50/100 = 1/2.",
                "step3": "Solve: Both equal 1/2, so 2/4 = 50/100.",
                "step4": "Verify: In Pair B, 2/3 (0.67) ≠ 3/4 (0.75). Only Pair A is equivalent."
            }
        },
        {
            "id": "u2_m7",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "medium",
            "format": "numberline",
            "question": "On the number line partitioned into tenths, plot the fraction equivalent to 70/100.",
            "lineData": {"min": 0, "max": 1, "step": 0.1, "target": 0.7, "label": "7/10 (Equivalent to 70/100)"},
            "answerKey": 0.7,
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "Simplify 70/100 by dividing both numerator and denominator by 10.",
                "70 ÷ 10 = 7, and 100 ÷ 10 = 10, so 70/100 = 7/10.",
                "Plot the point on 7/10 (the 7th tick mark at 0.7)."
            ],
            "explanation": {
                "step1": "Understand: Convert hundredths to tenths: 70/100 = ?/10.",
                "step2": "Model: (70 ÷ 10) / (100 ÷ 10) = 7/10.",
                "step3": "Solve: 7/10 is plotted at coordinate 0.7.",
                "step4": "Verify: 7 tenths is equivalent to 70 hundredths."
            }
        },
        {
            "id": "u2_m8",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Sort the fraction cards into two boxes: 'Less than 1/2' vs 'Greater than 1/2'.",
            "dragData": {
                "items": [
                    {"id": "f25", "val": "2/5"},
                    {"id": "f38", "val": "3/8"},
                    {"id": "f46", "val": "4/6"},
                    {"id": "f710", "val": "7/10"}
                ],
                "targets": [
                    {"id": "lessHalfBox", "name": "Less than 1/2", "expected": ["f25", "f38"]},
                    {"id": "greaterHalfBox", "name": "Greater than 1/2", "expected": ["f46", "f710"]}
                ]
            },
            "answerKey": {"lessHalfBox": ["f25", "f38"], "greaterHalfBox": ["f46", "f710"]},
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Compare each to 1/2: Half of 5 is 2.5 (so 2/5 < 1/2). Half of 8 is 4 (so 3/8 < 1/2).",
                "Half of 6 is 3 (so 4/6 > 1/2). Half of 10 is 5 (so 7/10 > 1/2).",
                "Less than 1/2: {2/5, 3/8}. Greater than 1/2: {4/6, 7/10}."
            ],
            "explanation": {
                "step1": "Understand: Benchmark comparison against 1/2.",
                "step2": "Model: 1/2 benchmarks: 2.5/5, 4/8, 3/6, 5/10.",
                "step3": "Solve: 2/5 < 2.5/5 and 3/8 < 4/8 (Less than 1/2). 4/6 > 3/6 and 7/10 > 5/10 (Greater than 1/2).",
                "step4": "Verify: Correctly categorizes all 4 fractions."
            }
        },

        # Hard Tier (6 questions: 2 MC, 1 Visual, 1 Number Line, 2 Drag-Drop)
        {
            "id": "u2_h1",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "hard",
            "format": "mc",
            "question": "Which explanation correctly describes why 5/8 is greater than 4/10?",
            "options": [
                {"id": "A", "text": "5/8 is greater than 1/2, and 4/10 is less than 1/2", "correct": True},
                {"id": "B", "text": "Both fractions are less than 1/2, but 5 is greater than 4", "correct": False},
                {"id": "C", "text": "The denominator 8 is smaller than 10, so any eighth is smaller than any tenth", "correct": False},
                {"id": "D", "text": "5/8 is equal to 1/2, while 4/10 is equal to 1", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Use the benchmark fraction 1/2.",
                "1/2 = 4/8 and 1/2 = 5/10.",
                "5/8 > 4/8 (so 5/8 > 1/2) and 4/10 < 5/10 (so 4/10 < 1/2). Therefore, 5/8 > 4/10."
            ],
            "explanation": {
                "step1": "Understand: Explain the comparison between 5/8 and 4/10 using benchmark reasoning.",
                "step2": "Model: 1/2 in eighths is 4/8. 1/2 in tenths is 5/10.",
                "step3": "Solve: 5/8 > 1/2 and 4/10 < 1/2. Since 5/8 is above 1/2 and 4/10 is below 1/2, 5/8 must be greater.",
                "step4": "Verify: 5/8 = 0.625 and 4/10 = 0.40; 0.625 > 0.40."
            }
        },
        {
            "id": "u2_h2",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "hard",
            "format": "mc",
            "question": "Which fraction is equivalent to 6/8 and has a denominator of 12?",
            "options": [
                {"id": "A", "text": "9/12", "correct": True},
                {"id": "B", "text": "8/12", "correct": False},
                {"id": "C", "text": "10/12", "correct": False},
                {"id": "D", "text": "7/12", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "First simplify 6/8 by dividing numerator and denominator by 2: 6/8 = 3/4.",
                "Now convert 3/4 to twelfths: multiply numerator and denominator by 3.",
                "(3 × 3) / (4 × 3) = 9/12."
            ],
            "explanation": {
                "step1": "Understand: Convert 6/8 into an equivalent fraction with denominator 12.",
                "step2": "Model: 6/8 simplifies to 3/4 by dividing by 2/2.",
                "step3": "Solve: Scale 3/4 to twelfths by multiplying by 3/3: 3 × 3 = 9, 4 × 3 = 12.",
                "step4": "Verify: 6/8 = 0.75 and 9/12 = 0.75."
            }
        },
        {
            "id": "u2_h3",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "hard",
            "format": "visual",
            "question": "Look at the fraction comparison model. Which point represents a fraction that is BOTH equivalent to 4/5 AND has a denominator of 10?",
            "visualCards": [
                {"id": "optA", "label": "Point A: 8/10", "val": "8/10", "correct": True},
                {"id": "optB", "label": "Point B: 6/10", "val": "6/10", "correct": False},
                {"id": "optC", "label": "Point C: 7/12", "val": "7/12", "correct": False},
                {"id": "optD", "label": "Point D: 5/8", "val": "5/8", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "To find 4/5 with a denominator of 10, multiply by 2/2.",
                "4 × 2 = 8, and 5 × 2 = 10.",
                "Point A represents 8/10."
            ],
            "explanation": {
                "step1": "Understand: Find the point that equals 4/5 in tenths.",
                "step2": "Model: (4 × 2) / (5 × 2) = 8/10.",
                "step3": "Solve: Point A is at 8/10.",
                "step4": "Verify: 8/10 simplifies to 4/5."
            }
        },
        {
            "id": "u2_h4",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "hard",
            "format": "numberline",
            "question": "On the number line with 12 equal intervals from 0 to 1, plot the fraction equivalent to 1/3.",
            "lineData": {"min": 0, "max": 1, "step": 0.08333333333333333, "target": 0.3333333333333333, "label": "4/12 (Equivalent to 1/3)"},
            "answerKey": 0.3333333333333333,
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "How many twelfths equal 1 third? 12 ÷ 3 = 4.",
                "1/3 = (1 × 4) / (3 × 4) = 4/12.",
                "Plot the point on the 4th tick mark (4/12)."
            ],
            "explanation": {
                "step1": "Understand: Plot 1/3 on a number line divided into 12 parts.",
                "step2": "Model: 1/3 = (1 × 4)/(3 × 4) = 4/12.",
                "step3": "Solve: 4/12 is at the 4th tick mark from 0.",
                "step4": "Verify: 4/12 simplifies to 1/3."
            }
        },
        {
            "id": "u2_h5",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.2",
            "difficulty": "hard",
            "format": "dragdrop",
            "question": "Drag the fractions into order from LEAST to GREATEST using benchmark reasoning against 1/2: 2/6, 1/2, 5/6.",
            "dragData": {
                "items": [
                    {"id": "f56", "val": "5/6"},
                    {"id": "f26", "val": "2/6"},
                    {"id": "fHalf", "val": "1/2"}
                ],
                "targets": [
                    {"id": "pos1", "name": "Least (1st)", "expected": ["f26"]},
                    {"id": "pos2", "name": "Middle (2nd)", "expected": ["fHalf"]},
                    {"id": "pos3", "name": "Greatest (3rd)", "expected": ["f56"]}
                ]
            },
            "answerKey": {"pos1": ["f26"], "pos2": ["fHalf"], "pos3": ["f56"]},
            "misconceptionKey": "benchmark_half",
            "hints": [
                "Convert 1/2 to sixths: 1/2 = 3/6.",
                "Now compare the three fractions: 2/6, 3/6, and 5/6.",
                "From least to greatest: 2/6 < 1/2 < 5/6."
            ],
            "explanation": {
                "step1": "Understand: Order three fractions from least to greatest.",
                "step2": "Model: 1/2 = 3/6. Compare: 2/6 < 3/6 < 5/6.",
                "step3": "Solve: Least is 2/6; middle is 1/2; greatest is 5/6.",
                "step4": "Verify: 2/6 (0.33) < 1/2 (0.50) < 5/6 (0.83)."
            }
        },
        {
            "id": "u2_h6",
            "unit": 2,
            "unitName": "Unit 2: Fraction Equivalence & Comparison",
            "standard": "NC.4.NF.1",
            "difficulty": "hard",
            "format": "dragdrop",
            "question": "Match each fraction card with its exact equivalent fraction target: 1/4 -> 3/12, 2/3 -> 8/12, 3/5 -> 6/10, 4/10 -> 40/100.",
            "dragData": {
                "items": [
                    {"id": "c14", "val": "1/4"},
                    {"id": "c23", "val": "2/3"},
                    {"id": "c35", "val": "3/5"},
                    {"id": "c410", "val": "4/10"}
                ],
                "targets": [
                    {"id": "t312", "name": "Matches 3/12", "expected": ["c14"]},
                    {"id": "t812", "name": "Matches 8/12", "expected": ["c23"]},
                    {"id": "t610", "name": "Matches 6/10", "expected": ["c35"]},
                    {"id": "t40100", "name": "Matches 40/100", "expected": ["c410"]}
                ]
            },
            "answerKey": {"t312": ["c14"], "t812": ["c23"], "t610": ["c35"], "t40100": ["c410"]},
            "misconceptionKey": "fraction_compare_wholes",
            "hints": [
                "1/4 = (1 × 3)/(4 × 3) = 3/12.",
                "2/3 = (2 × 4)/(3 × 4) = 8/12.",
                "3/5 = (3 × 2)/(5 × 2) = 6/10; 4/10 = 40/100."
            ],
            "explanation": {
                "step1": "Understand: Match each simplified fraction to its scaled equivalent.",
                "step2": "Model: 1/4 = 3/12; 2/3 = 8/12; 3/5 = 6/10; 4/10 = 40/100.",
                "step3": "Solve: Place each card into its matching slot.",
                "step4": "Verify: Every pair simplifies to the exact same irreducible fraction."
            }
        },

        # =========================================================================
        # UNIT 3: OPERATIONS WITH FRACTIONS (NC.4.NF.3 & NC.4.NF.4)
        # =========================================================================
        # Easy Tier (6 questions: 1 MC, 2 Visual, 1 Number Line, 2 Drag-Drop)
        {
            "id": "u3_e1",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "dragdrop",
            "question": "Drag three unit fraction tiles into the workspace container to build an expression equal to 3/6.",
            "dragData": {
                "items": [
                    {"id": "u6a", "val": "1/6"},
                    {"id": "u6b", "val": "1/6"},
                    {"id": "u6c", "val": "1/6"},
                    {"id": "u8", "val": "1/8"},
                    {"id": "u4", "val": "1/4"}
                ],
                "targets": [
                    {"id": "composeBox", "name": "Decomposition Container (Goal: 3/6)", "expected": ["u6a", "u6b", "u6c"]}
                ]
            },
            "answerKey": {"composeBox": ["u6a", "u6b", "u6c"]},
            "misconceptionKey": "add_denominators",
            "hints": [
                "A unit fraction has a numerator of 1: 1/6.",
                "3/6 means 3 pieces of size 1/6: 1/6 + 1/6 + 1/6.",
                "Drag the three 1/6 tiles into the container."
            ],
            "explanation": {
                "step1": "Understand: Decompose 3/6 into a sum of unit fractions.",
                "step2": "Model: 3/6 = 1/6 + 1/6 + 1/6.",
                "step3": "Solve: Place three 1/6 tiles together to equal 3/6.",
                "step4": "Verify: 1/6 + 1/6 + 1/6 = 3/6."
            }
        },
        {
            "id": "u3_e2",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "mc",
            "question": "What is 2/5 + 1/5?",
            "options": [
                {"id": "A", "text": "3/5", "correct": True},
                {"id": "B", "text": "3/10", "correct": False},
                {"id": "C", "text": "2/10", "correct": False},
                {"id": "D", "text": "1/5", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "add_denominators",
            "hints": [
                "When adding fractions with like denominators, only add the numerators!",
                "The denominator tells you the size of the piece, which does NOT change (it stays 5).",
                "2 + 1 = 3, so the answer is 3/5 (NOT 3/10)."
            ],
            "explanation": {
                "step1": "Understand: Add two fractions with the same denominator (fifths).",
                "step2": "Model: 2 fifths + 1 fifth = 3 fifths.",
                "step3": "Solve: (2 + 1) / 5 = 3/5.",
                "step4": "Verify: Common error alert: Do not add the denominators (5 + 5 ≠ 10). The denominator stays 5."
            }
        },
        {
            "id": "u3_e3",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "visual",
            "question": "Which length model tape diagram shows the sum 1/6 + 3/6 = 4/6?",
            "visualCards": [
                {"id": "optA", "label": "Model A: Tape of 6 parts (1 shaded + 3 shaded = 4/6 total)", "correct": True},
                {"id": "optB", "label": "Model B: Tape of 12 parts (4 shaded = 4/12)", "correct": False},
                {"id": "optC", "label": "Model C: Tape of 6 parts (2 shaded = 2/6)", "correct": False},
                {"id": "optD", "label": "Model D: Tape of 8 parts (4 shaded = 4/8)", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "add_denominators",
            "hints": [
                "Adding like fractions joins segments along the SAME whole tape.",
                "1 sixth joined with 3 sixths makes 4 sixths of the whole tape.",
                "Model A shows 1/6 + 3/6 = 4/6 on a tape partitioned into 6 parts."
            ],
            "explanation": {
                "step1": "Understand: Model fraction addition on a continuous length tape.",
                "step2": "Model: Joining 1 unit of length 1/6 with 3 units of length 1/6.",
                "step3": "Solve: Total shaded length = 4 sixths = 4/6.",
                "step4": "Verify: The tape still has 6 parts, showing the denominator remains 6."
            }
        },
        {
            "id": "u3_e4",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "visual",
            "question": "Which diagram correctly illustrates the unit fraction decomposition of 4/8?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 1/8 + 1/8 + 1/8 + 1/8", "correct": True},
                {"id": "optB", "label": "Model B: 2/8 + 2/8", "correct": False},
                {"id": "optC", "label": "Model C: 1/4 + 1/4", "correct": False},
                {"id": "optD", "label": "Model D: 4/1 + 1/8", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "add_denominators",
            "hints": [
                "A unit fraction decomposition uses ONLY fractions with numerator 1 (like 1/8).",
                "To make 4/8, add four 1/8 tiles together.",
                "Model A shows 1/8 + 1/8 + 1/8 + 1/8 = 4/8."
            ],
            "explanation": {
                "step1": "Understand: Unit fractions always have a numerator of 1.",
                "step2": "Model: 4/8 = 1/8 + 1/8 + 1/8 + 1/8.",
                "step3": "Solve: Model A is the only option showing exclusively unit fractions.",
                "step4": "Verify: 1 + 1 + 1 + 1 = 4, so 4/8 is correctly formed."
            }
        },
        {
            "id": "u3_e5",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "numberline",
            "question": "Start at 5/8 on the number line and subtract 2/8. Plot the ending point.",
            "lineData": {"min": 0, "max": 1, "step": 0.125, "target": 0.375, "label": "3/8 (5/8 - 2/8)"},
            "answerKey": 0.375,
            "misconceptionKey": "add_denominators",
            "hints": [
                "Find 5/8 on the number line (the 5th tick out of 8).",
                "Move backward to the left by 2 steps of 1/8.",
                "5/8 - 2/8 = 3/8 (the 3rd tick mark at 0.375)."
            ],
            "explanation": {
                "step1": "Understand: Subtract 2/8 from 5/8 using a number line.",
                "step2": "Model: Start at 5/8, move left 2 ticks: 5 - 2 = 3.",
                "step3": "Solve: The ending point is 3/8 = 0.375.",
                "step4": "Verify: 3/8 + 2/8 = 5/8."
            }
        },
        {
            "id": "u3_e6",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "easy",
            "format": "dragdrop",
            "question": "Drag the correct fraction card to complete the equation: 1/4 + 2/4 = [ ? ].",
            "dragData": {
                "items": [
                    {"id": "ans34", "val": "3/4"},
                    {"id": "ans38", "val": "3/8"},
                    {"id": "ans24", "val": "2/4"},
                    {"id": "ans14", "val": "1/4"}
                ],
                "targets": [
                    {"id": "sumSlot", "name": "Sum Slot", "expected": ["ans34"]}
                ]
            },
            "answerKey": {"sumSlot": ["ans34"]},
            "misconceptionKey": "add_denominators",
            "hints": [
                "Add the numerators: 1 + 2 = 3.",
                "Keep the denominator 4: fourths remain fourths!",
                "The answer is 3/4 (NOT 3/8!)."
            ],
            "explanation": {
                "step1": "Understand: Add like fractions 1/4 and 2/4.",
                "step2": "Model: 1 fourth + 2 fourths = 3 fourths.",
                "step3": "Solve: 1/4 + 2/4 = 3/4.",
                "step4": "Verify: 3/8 is an incorrect misconception caused by adding denominators."
            }
        },

        # Medium Tier (8 questions: 3 MC, 1 Visual, 2 Number Line, 2 Drag-Drop)
        {
            "id": "u3_m1",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "medium",
            "format": "mc",
            "question": "Which equation shows a correct decomposition of 5/8?",
            "options": [
                {"id": "A", "text": "5/8 = 1/8 + 1/8 + 3/8", "correct": True},
                {"id": "B", "text": "5/8 = 2/4 + 3/4", "correct": False},
                {"id": "C", "text": "5/8 = 1/8 + 2/8 + 3/8", "correct": False},
                {"id": "D", "text": "5/8 = 5/1 + 1/8", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "add_denominators",
            "hints": [
                "Add the numerators in each option to see which equals 5 eighths.",
                "In Option A: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.",
                "In Option C: 1 + 2 + 3 = 6/8 (not 5/8). Option A is the correct decomposition."
            ],
            "explanation": {
                "step1": "Understand: Decompose 5/8 into multiple fractional parts.",
                "step2": "Model: Test Option A: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.",
                "step3": "Solve: Option A correctly equals 5/8.",
                "step4": "Verify: Option B equals 5/4, and Option C equals 6/8."
            }
        },
        {
            "id": "u3_m2",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "medium",
            "format": "mc",
            "question": "Landon ate 2/8 of a pizza for lunch and 3/8 of the same whole pizza for dinner. How much of the pizza did Landon eat in all?",
            "options": [
                {"id": "A", "text": "5/8", "correct": True},
                {"id": "B", "text": "5/16", "correct": False},
                {"id": "C", "text": "1/8", "correct": False},
                {"id": "D", "text": "6/8", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "add_denominators",
            "hints": [
                "Landon ate 2 slices of the 8-slice pizza, then 3 more slices of the same 8-slice pizza.",
                "Total slices eaten: 2 + 3 = 5 slices.",
                "The pizza still has 8 slices in total, so Landon ate 5/8 of the pizza (NOT 5/16!)."
            ],
            "explanation": {
                "step1": "Understand: Combine fractional parts of the same whole pizza.",
                "step2": "Model: 2/8 + 3/8.",
                "step3": "Solve: 2/8 + 3/8 = (2 + 3)/8 = 5/8.",
                "step4": "Verify: The total number of slices in the pizza is still 8, so the denominator remains 8."
            }
        },
        {
            "id": "u3_m3",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "medium",
            "format": "mc",
            "question": "Which expression represents 4 × (1/5) as repeated addition of unit fractions?",
            "options": [
                {"id": "A", "text": "1/5 + 1/5 + 1/5 + 1/5", "correct": True},
                {"id": "B", "text": "4/5 + 4/5 + 4/5 + 4/5", "correct": False},
                {"id": "C", "text": "1/20 + 1/20 + 1/20 + 1/20", "correct": False},
                {"id": "D", "text": "4/1 + 1/5", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "Multiplication by a whole number means repeated addition of that group.",
                "4 × (1/5) means 4 copies of 1/5 added together.",
                "1/5 + 1/5 + 1/5 + 1/5 = 4/5."
            ],
            "explanation": {
                "step1": "Understand: Conceptualize whole number multiplication with unit fractions as repeated addition.",
                "step2": "Model: n × (1/b) = (1/b) added n times.",
                "step3": "Solve: 4 × (1/5) = 1/5 + 1/5 + 1/5 + 1/5 = 4/5.",
                "step4": "Verify: Multiplying 4 by 1/5 yields 4/5."
            }
        },
        {
            "id": "u3_m4",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "medium",
            "format": "visual",
            "question": "Which number line jump diagram correctly models 3 × (1/4) starting at 0?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 3 jumps of size 1/4 landing on 3/4", "jumps": 3, "size": "1/4", "land": "3/4", "correct": True},
                {"id": "optB", "label": "Model B: 3 jumps of size 1/12 landing on 3/12", "jumps": 3, "size": "1/12", "land": "3/12", "correct": False},
                {"id": "optC", "label": "Model C: 1 single jump landing on 3/4", "jumps": 1, "size": "3/4", "land": "3/4", "correct": False},
                {"id": "optD", "label": "Model D: 4 jumps of size 1/3 landing on 4/3", "jumps": 4, "size": "1/3", "land": "4/3", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "3 × (1/4) means making 3 separate jumps, each of length 1/4.",
                "First jump: 0 to 1/4. Second jump: 1/4 to 2/4. Third jump: 2/4 to 3/4.",
                "Model A shows 3 consecutive jumps of 1/4 landing on 3/4."
            ],
            "explanation": {
                "step1": "Understand: Model unit fraction multiplication as equal distance jumps on a number line.",
                "step2": "Model: 3 jumps of 1/4: 0 -> 1/4 -> 2/4 -> 3/4.",
                "step3": "Solve: The runner lands on 3/4.",
                "step4": "Verify: 3 × (1/4) = 3/4."
            }
        },
        {
            "id": "u3_m5",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "medium",
            "format": "numberline",
            "question": "On the number line marked in tenths, start at 3/10 and add 4/10. Plot the sum.",
            "lineData": {"min": 0, "max": 1, "step": 0.1, "target": 0.7, "label": "7/10 (3/10 + 4/10)"},
            "answerKey": 0.7,
            "misconceptionKey": "add_denominators",
            "hints": [
                "Start at 3/10 on the number line.",
                "Jump forward to the right by 4 tenths: 3 + 4 = 7 tenths.",
                "Plot the point on 7/10 (at 0.7)."
            ],
            "explanation": {
                "step1": "Understand: Add 3/10 + 4/10.",
                "step2": "Model: Start at 3/10, advance 4 ticks: 3/10 + 4/10 = 7/10.",
                "step3": "Solve: Landing coordinate is 0.7.",
                "step4": "Verify: 3/10 + 4/10 = 7/10 (not 7/20)."
            }
        },
        {
            "id": "u3_m6",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "medium",
            "format": "numberline",
            "question": "Start at 7/12 on the number line and subtract 3/12. Plot the difference.",
            "lineData": {"min": 0, "max": 1, "step": 0.08333333333333333, "target": 0.3333333333333333, "label": "4/12 (7/12 - 3/12)"},
            "answerKey": 0.3333333333333333,
            "misconceptionKey": "add_denominators",
            "hints": [
                "Find 7/12 on the number line.",
                "Move backward to the left by 3 twelfths: 7 - 3 = 4 twelfths.",
                "Plot the point on 4/12 (which is equal to 1/3, at coordinate 0.333)."
            ],
            "explanation": {
                "step1": "Understand: Subtract fractions with like denominator 12.",
                "step2": "Model: 7/12 - 3/12 = (7 - 3)/12 = 4/12.",
                "step3": "Solve: 4/12 is at the 4th tick mark (0.333).",
                "step4": "Verify: 4/12 simplifies to 1/3."
            }
        },
        {
            "id": "u3_m7",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Decompose 4/5 in two different ways by dragging the matching expression cards.",
            "dragData": {
                "items": [
                    {"id": "expA", "val": "1/5 + 1/5 + 1/5 + 1/5"},
                    {"id": "expB", "val": "2/5 + 2/5"},
                    {"id": "expC", "val": "3/5 + 2/5"},
                    {"id": "expD", "val": "4/10 + 4/10"}
                ],
                "targets": [
                    {"id": "boxDecomp1", "name": "Way 1: Unit Fractions", "expected": ["expA"]},
                    {"id": "boxDecomp2", "name": "Way 2: Two Equal Parts", "expected": ["expB"]}
                ]
            },
            "answerKey": {"boxDecomp1": ["expA"], "boxDecomp2": ["expB"]},
            "misconceptionKey": "add_denominators",
            "hints": [
                "Unit fractions: 1/5 + 1/5 + 1/5 + 1/5 = 4/5.",
                "Two equal parts: 2/5 + 2/5 = 4/5.",
                "Place '1/5 + 1/5 + 1/5 + 1/5' into Way 1, and '2/5 + 2/5' into Way 2."
            ],
            "explanation": {
                "step1": "Understand: Decompose 4/5 into sums of fractions with the same denominator in multiple ways.",
                "step2": "Model: 4/5 = 1/5 + 1/5 + 1/5 + 1/5 (unit fractions) and 4/5 = 2/5 + 2/5.",
                "step3": "Solve: Assign expA to Way 1 and expB to Way 2.",
                "step4": "Verify: Both expressions evaluate to exactly 4/5."
            }
        },
        {
            "id": "u3_m8",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "medium",
            "format": "dragdrop",
            "question": "Match each repeated addition sum to its multiplication expression: 5 × 1/6, 2 × 1/3, 3 × 1/8.",
            "dragData": {
                "items": [
                    {"id": "mult56", "val": "5 × (1/6)"},
                    {"id": "mult23", "val": "2 × (1/3)"},
                    {"id": "mult38", "val": "3 × (1/8)"}
                ],
                "targets": [
                    {"id": "sum56", "name": "1/6 + 1/6 + 1/6 + 1/6 + 1/6", "expected": ["mult56"]},
                    {"id": "sum23", "name": "1/3 + 1/3", "expected": ["mult23"]},
                    {"id": "sum38", "name": "1/8 + 1/8 + 1/8", "expected": ["mult38"]}
                ]
            },
            "answerKey": {"sum56": ["mult56"], "sum23": ["mult23"], "sum38": ["mult38"]},
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "Count how many times the unit fraction is added.",
                "Five copies of 1/6 equals 5 × (1/6).",
                "Two copies of 1/3 equals 2 × (1/3); three copies of 1/8 equals 3 × (1/8)."
            ],
            "explanation": {
                "step1": "Understand: Connect repeated addition of unit fractions to whole number multiplication.",
                "step2": "Model: Repeated addition is multiplication: n copies of 1/b = n × (1/b).",
                "step3": "Solve: 5 copies of 1/6 is 5 × 1/6; 2 copies of 1/3 is 2 × 1/3; 3 copies of 1/8 is 3 × 1/8.",
                "step4": "Verify: Matches the definition of NC.4.NF.4."
            }
        },

        # Hard Tier (6 questions: 2 MC, 1 Visual, 2 Number Line, 1 Drag-Drop)
        {
            "id": "u3_h1",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "hard",
            "format": "numberline",
            "question": "Use the jump tool to show 4 × (1/3) on the number line. Start at 0 and make 4 jumps of size 1/3. What point do you land on?",
            "lineData": {"min": 0, "max": 2, "step": 0.3333333333333333, "target": 1.3333333333333333, "label": "4/3 (or 1 1/3)"},
            "answerKey": 1.3333333333333333,
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "Start at 0 and count 4 jumps of size 1/3: 1/3, 2/3, 3/3 (which is 1), 4/3.",
                "4/3 is an improper fraction equal to the mixed number 1 1/3.",
                "Plot the point on 4/3 (at coordinate 1.333)."
            ],
            "explanation": {
                "step1": "Understand: Calculate 4 × (1/3) using jumps along a number line beyond 1 whole.",
                "step2": "Model: 0 + 1/3 + 1/3 + 1/3 + 1/3 = 4/3 = 1 1/3.",
                "step3": "Solve: 4/3 is one step past 1 on a thirds number line.",
                "step4": "Verify: 4 × 1/3 = 4/3 = 1 1/3."
            }
        },
        {
            "id": "u3_h2",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "hard",
            "format": "mc",
            "question": "Zoe has 2 3/6 yards of ribbon. She uses 1 1/6 yards for a craft project. How much ribbon does Zoe have left?",
            "options": [
                {"id": "A", "text": "1 2/6 yards (or 1 1/3 yards)", "correct": True},
                {"id": "B", "text": "1 4/6 yards", "correct": False},
                {"id": "C", "text": "3 4/6 yards", "correct": False},
                {"id": "D", "text": "2 2/6 yards", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "add_denominators",
            "hints": [
                "Subtract the whole number parts: 2 - 1 = 1.",
                "Subtract the fractional parts with like denominators: 3/6 - 1/6 = 2/6.",
                "Combine the results: 1 + 2/6 = 1 2/6 yards."
            ],
            "explanation": {
                "step1": "Understand: Subtract mixed numbers with like denominators: 2 3/6 - 1 1/6.",
                "step2": "Model: Separate into whole numbers and fractions: (2 - 1) + (3/6 - 1/6).",
                "step3": "Solve: 2 - 1 = 1; 3/6 - 1/6 = 2/6. Result: 1 2/6 yards.",
                "step4": "Verify: 1 2/6 + 1 1/6 = 2 3/6."
            }
        },
        {
            "id": "u3_h3",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "hard",
            "format": "mc",
            "question": "Liam runs 1/4 mile around the school track every day for 6 days. How many miles did Liam run in all?",
            "options": [
                {"id": "A", "text": "6/4 miles (or 1 2/4 miles)", "correct": True},
                {"id": "B", "text": "6/24 miles", "correct": False},
                {"id": "C", "text": "1/24 miles", "correct": False},
                {"id": "D", "text": "7/4 miles", "correct": False}
            ],
            "answerKey": "A",
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "Multiply the number of days (6) by the distance each day (1/4 mile): 6 × (1/4).",
                "6 × (1/4) = 6/4 miles.",
                "6/4 can be written as 1 2/4 miles or 1 1/2 miles. Common error: Do not multiply the denominator by 6 (6/24 is wrong!)."
            ],
            "explanation": {
                "step1": "Understand: Multiply a whole number by a unit fraction in a real-world context.",
                "step2": "Model: 6 × (1/4) = 1/4 + 1/4 + 1/4 + 1/4 + 1/4 + 1/4 = 6/4.",
                "step3": "Solve: 6/4 miles = 1 2/4 miles.",
                "step4": "Verify: 6 × 1/4 = 6/4 (not 6/24)."
            }
        },
        {
            "id": "u3_h4",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "hard",
            "format": "visual",
            "question": "Which visual tape diagram correctly models 1 3/8 + 4/8?",
            "visualCards": [
                {"id": "optA", "label": "Model A: 1 whole tape + 3 eighths + 4 eighths = 1 7/8 total", "correct": True},
                {"id": "optB", "label": "Model B: 1 whole tape showing 1 7/16 total", "correct": False},
                {"id": "optC", "label": "Model C: 2 full whole tapes (2 1/8)", "correct": False},
                {"id": "optD", "label": "Model D: Only 7/8 (missing the whole unit)", "correct": False}
            ],
            "answerKey": "optA",
            "misconceptionKey": "add_denominators",
            "hints": [
                "Keep the 1 whole unit intact.",
                "Add the fractional parts: 3/8 + 4/8 = 7/8.",
                "Combine: 1 + 7/8 = 1 7/8. Model A displays 1 full bar plus 7 eighths shaded."
            ],
            "explanation": {
                "step1": "Understand: Add a fraction to a mixed number with like denominators.",
                "step2": "Model: 1 3/8 + 4/8 = 1 + (3/8 + 4/8) = 1 7/8.",
                "step3": "Solve: Model A shows 1 complete whole bar and 7 out of 8 parts in the second bar.",
                "step4": "Verify: 1 7/8 is less than 2 wholes."
            }
        },
        {
            "id": "u3_h5",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.4",
            "difficulty": "hard",
            "format": "numberline",
            "question": "A baker uses a 1/8-cup scoop to add 5 scoops of sugar into a recipe. Use the jump tool to show 5 jumps of 1/8 starting at 0. Plot where the sugar level reaches.",
            "lineData": {"min": 0, "max": 1, "step": 0.125, "target": 0.625, "label": "5/8 (5 × 1/8 cup)"},
            "answerKey": 0.625,
            "misconceptionKey": "whole_times_fraction",
            "hints": [
                "Each scoop is 1/8 cup. 5 scoops is 5 × (1/8).",
                "Make 5 jumps of 1/8 from 0: 1/8, 2/8, 3/8, 4/8, 5/8.",
                "Plot the point on 5/8 (coordinate 0.625)."
            ],
            "explanation": {
                "step1": "Understand: 5 scoops of 1/8 cup equals 5 × 1/8.",
                "step2": "Model: 5 × (1/8) = 5/8 cup.",
                "step3": "Solve: On an eighths scale, 5 ticks from 0 equals 5/8 = 0.625.",
                "step4": "Verify: 5 × 1/8 = 5/8."
            }
        },
        {
            "id": "u3_h6",
            "unit": 3,
            "unitName": "Unit 3: Operations with Fractions",
            "standard": "NC.4.NF.3",
            "difficulty": "hard",
            "format": "dragdrop",
            "question": "Sort each equation card: Is it Mathematically TRUE or a Common Student ERROR?",
            "dragData": {
                "items": [
                    {"id": "eq1", "val": "1/4 + 2/4 = 3/4"},
                    {"id": "eq2", "val": "3 × (1/5) = 3/5"},
                    {"id": "eq3", "val": "1/4 + 2/4 = 3/8"},
                    {"id": "eq4", "val": "3 × (1/5) = 3/15"}
                ],
                "targets": [
                    {"id": "trueBox", "name": "Mathematically TRUE", "expected": ["eq1", "eq2"]},
                    {"id": "errorBox", "name": "Common Student ERROR", "expected": ["eq3", "eq4"]}
                ]
            },
            "answerKey": {"trueBox": ["eq1", "eq2"], "errorBox": ["eq3", "eq4"]},
            "misconceptionKey": "add_denominators",
            "hints": [
                "Remember: NEVER add denominators when adding like fractions!",
                "1/4 + 2/4 = 3/4 is TRUE. 1/4 + 2/4 = 3/8 is a false error.",
                "3 × (1/5) = 3/5 is TRUE. 3 × (1/5) = 3/15 is a false error."
            ],
            "explanation": {
                "step1": "Understand: Evaluate true mathematical equations vs misconception errors.",
                "step2": "Model: Denominators represent unit sizes and do not add or multiply by whole numbers.",
                "step3": "Solve: 1/4 + 2/4 = 3/4 (True); 3 × 1/5 = 3/5 (True); 1/4 + 2/4 = 3/8 (Error); 3 × 1/5 = 3/15 (Error).",
                "step4": "Verify: Accurately classifies all 4 cards."
            }
        }
    ]
    return questions

if __name__ == '__main__':
    qs = get_questions_data()
    print(f"Total questions generated: {len(qs)}")
    u1 = [q for q in qs if q['unit'] == 1]
    u2 = [q for q in qs if q['unit'] == 2]
    u3 = [q for q in qs if q['unit'] == 3]
    print(f"Unit 1: {len(u1)} (Easy: {len([q for q in u1 if q['difficulty']=='easy'])}, Med: {len([q for q in u1 if q['difficulty']=='medium'])}, Hard: {len([q for q in u1 if q['difficulty']=='hard'])})")
    print(f"Unit 2: {len(u2)} (Easy: {len([q for q in u2 if q['difficulty']=='easy'])}, Med: {len([q for q in u2 if q['difficulty']=='medium'])}, Hard: {len([q for q in u2 if q['difficulty']=='hard'])})")
    print(f"Unit 3: {len(u3)} (Easy: {len([q for q in u3 if q['difficulty']=='easy'])}, Med: {len([q for q in u3 if q['difficulty']=='medium'])}, Hard: {len([q for q in u3 if q['difficulty']=='hard'])})")
