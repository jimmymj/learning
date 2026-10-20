import sys
sys.path.insert(0, '.')
from scratch.unit1_questions import UNIT1_QUESTIONS
from scratch.unit2_questions import UNIT2_QUESTIONS
from scratch.unit3_questions import UNIT3_QUESTIONS

# Define formattedAnswer for all 60 questions
FORMATTED_ANSWERS = {
    # Unit 1
    "u1_q01": "3 × 4 Array (3 rows of 4 = 12 tiles)",
    "u1_q02": "3 (18 ÷ 3 = 6 with 0 remainder)",
    "u1_q03": "24 (6 × 4 = 24)",
    "u1_q04": "5 groups of 4 stars (5 × 4 = 20, 0 leftovers)",
    "u1_q05": "15 (3 × 5 = 15)",
    "u1_q06": "19 is Prime | 21 is Composite",
    "u1_q07": "1 × 24, 2 × 12, 3 × 8, 4 × 6",
    "u1_q08": "7, 14, 21, 28",
    "u1_q09": "Composite, because 3 × 17 = 51",
    "u1_q10": "6 × 6 Square Array (6 × 6 = 36 tiles)",
    "u1_q11": "(1 × 16), (2 × 8), (4 × 4)",
    "u1_q12": "24 (LCM of 6 and 8)",
    "u1_q13": "Factors of 30: 5, 6 | Multiples of 30: 60, 90",
    "u1_q14": "8 (7 × 8 = 56)",
    "u1_q15": "Primes: 2, 13, 29 | Composites: 9, 21, 33",
    "u1_q16": "4 rectangular arrays (1×30, 2×15, 3×10, 5×6)",
    "u1_q17": "{1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}",
    "u1_q18": "23, 29, 31",
    "u1_q19": "24 (Multiple of 4, factor of 48, between 20 and 30)",
    "u1_q20": "Exactly 3 Factors: 4, 9 | More than 3 Factors: 12, 18",

    # Unit 2
    "u2_q01": "4/6 Strip (4 out of 6 parts shaded, equivalent to 2/3)",
    "u2_q02": "5/10 (Equivalent to 1/2)",
    "u2_q03": "5/8 (5 eighths is greater than 3 eighths)",
    "u2_q04": "6 out of 8 grid cells shaded (3/4 = 6/8)",
    "u2_q05": "1/2 (Coordinate 0.50 on number line)",
    "u2_q06": "< (Less Than) — 2/6 is less than 4/6",
    "u2_q07": "> (Greater Than) — 3/4 is greater than 5/8 (6/8 > 5/8)",
    "u2_q08": "3/4 (or 6/8, coordinate 0.75)",
    "u2_q09": "Multiply both numerator and denominator by 2",
    "u2_q10": "3/8 > 3/10 because eighths are larger pieces than tenths",
    "u2_q11": "Tape of 12 (4 shaded) aligned with Tape of 3 (1 shaded): 4/12 = 1/3",
    "u2_q12": "Pair of 2/4 and 50/100 (both equal 1/2)",
    "u2_q13": "7/10 (70/100, coordinate 0.70)",
    "u2_q14": "Less than 1/2: 2/5, 3/8 | Greater than 1/2: 4/6, 7/10",
    "u2_q15": "5/8 is greater than 1/2, and 4/10 is less than 1/2",
    "u2_q16": "9/12 (3/4 = 9/12)",
    "u2_q17": "Point at 8/10 (Coordinate 0.80 on number line)",
    "u2_q18": "1/3 (or 4/12, coordinate 0.33)",
    "u2_q19": "2/6 < 1/2 < 5/6",
    "u2_q20": "1/4 = 3/12, 2/3 = 8/12, 3/5 = 6/10, 4/10 = 40/100",

    # Unit 3
    "u3_q01": "1/6 + 1/6 + 1/6 = 3/6",
    "u3_q02": "3/5 (1/5 + 2/5 = 3/5)",
    "u3_q03": "Tape of 6 parts (1 shaded + 3 shaded = 4/6 total)",
    "u3_q04": "1/8 + 1/8 + 1/8 + 1/8 = 4/8",
    "u3_q05": "3/8 (Coordinate 0.375 on number line)",
    "u3_q06": "3/4 (1/4 + 3/4 = 4/4 = 1 whole)",
    "u3_q07": "5/8 = 1/8 + 1/8 + 3/8",
    "u3_q08": "5/8 of the pizza (2/8 + 3/8 = 5/8)",
    "u3_q09": "1/5 + 1/5 + 1/5 + 1/5 = 4/5",
    "u3_q10": "3 jumps of size 1/4 landing on 3/4",
    "u3_q11": "7/10 (Coordinate 0.70 on number line)",
    "u3_q12": "2/6 (or 1/3, coordinate 0.33)",
    "u3_q13": "Decompositions of 5/6: 2/6 + 3/6 and 1/6 + 4/6",
    "u3_q14": "5 × (1/6) = 5/6, 2 × (1/3) = 2/3, 3 × (1/8) = 3/8",
    "u3_q15": "1 2/6 (or 4/3, coordinate 1.33)",
    "u3_q16": "1 2/6 yards (or 1 1/3 yards)",
    "u3_q17": "6/4 miles (or 1 2/4 = 1 1/2 miles)",
    "u3_q18": "1 whole tape + 3 eighths + 4 eighths = 1 7/8 total",
    "u3_q19": "5/8 (Coordinate 0.625 on number line)",
    "u3_q20": "True: 4 × 2/5 = 8/5 and 3 × 3/8 = 9/8 | False: 2 × 3/4 = 6/8 and 5 × 1/6 = 5/30"
}

def balance_unit_questions(questions, unit_num):
    # Desired target indices for MC questions in order: C, B, D, A, C, B...
    target_mc_indices = [2, 1, 3, 0, 2, 1, 3, 0]
    # Desired target indices for Visual questions in order: B, D, A, C, B...
    target_vis_indices = [1, 3, 0, 2, 1, 3, 0, 2]

    mc_counter = 0
    vis_counter = 0

    letters = ["A", "B", "C", "D"]
    opt_ids = ["optA", "optB", "optC", "optD"]

    for q in questions:
        qid = q["id"]
        if qid in FORMATTED_ANSWERS:
            q["formattedAnswer"] = FORMATTED_ANSWERS[qid]

        # Clean hint/explanation references to Option A / Model A
        new_hints = []
        for h in q.get("hints", []):
            h_clean = h.replace("Model A has 3 rows and 4 columns, giving an area of exactly 12 square units.", "The 3 × 4 array has 3 rows and 4 columns, giving an area of exactly 12 square units.")
            h_clean = h_clean.replace("Notice Model A has exactly 3 groups of 5 with 0 leftovers.", "Notice that 3 groups of 5 stars totals 15 with 0 leftovers.")
            h_clean = h_clean.replace("Option A lists all 4 factor pairs for 24: 1 × 24, 2 × 12, 3 × 8, 4 × 6.", "All 4 factor pairs for 24 are: 1 × 24, 2 × 12, 3 × 8, 4 × 6.")
            h_clean = h_clean.replace("Option B misses 2 × 12. Option D has 3 × 9 = 27 (not 24).", "Check every pair: 2 × 12 = 24 must be included, while 3 × 9 = 27 is not 24.")
            h_clean = h_clean.replace("Option A includes all 4 factor pairs for 24.", "The correct list includes all 4 factor pairs for 24.")
            h_clean = h_clean.replace("Model A has 6 rows and 6 columns: 6 × 6 = 36.", "A 6 × 6 square array has 6 rows and 6 columns: 6 × 6 = 36.")
            h_clean = h_clean.replace("Model A contains all 12 factors without any incorrect numbers.", "The correct factor set contains all 12 factors without any incorrect numbers.")
            h_clean = h_clean.replace("Model A has 4 out of 6 parts shaded, covering the exact same length as 2/3.", "The 4/6 strip has 4 out of 6 parts shaded, covering the exact same length as 2/3.")
            h_clean = h_clean.replace("Model A has 4 out of 6 parts shaded, which covers the exact same length as 2/3.", "The 4/6 strip has 4 out of 6 parts shaded, which covers the exact same length as 2/3.")
            h_clean = h_clean.replace("Model A shows 6 shaded cells out of 8 total cells (6/8).", "The 6/8 grid shows 6 shaded cells out of 8 total cells.")
            h_clean = h_clean.replace("Model A has 6 shaded cells out of 8 total cells.", "The 6/8 model has 6 shaded cells out of 8 total cells.")
            h_clean = h_clean.replace("Model A shows 4 twelfths aligned with 1 third.", "4 twelfths aligns perfectly with 1 third (4/12 = 1/3).")
            h_clean = h_clean.replace("Model A shows 1/6 + 3/6 = 4/6 on a tape partitioned into 6 parts.", "1/6 + 3/6 = 4/6 is modeled on a tape partitioned into 6 parts.")
            h_clean = h_clean.replace("Model A shows 1/8 + 1/8 + 1/8 + 1/8 = 4/8.", "1/8 + 1/8 + 1/8 + 1/8 = 4/8 shows the unit fraction decomposition.")
            h_clean = h_clean.replace("In Option A: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.", "Calculate: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.")
            h_clean = h_clean.replace("In Option C: 1 + 2 + 3 = 6/8. Option A is the correct decomposition.", "Adding 1/8 + 2/8 + 3/8 gives 6/8. The correct decomposition gives 5/8.")
            h_clean = h_clean.replace("In Option C: 1 + 2 + 3 = 6/8 (not 5/8). Option A is the correct decomposition.", "Adding 1/8 + 2/8 + 3/8 gives 6/8 (not 5/8). 1/8 + 1/8 + 3/8 gives exactly 5/8.")
            h_clean = h_clean.replace("Model A shows 3 jumps of 1/4 landing on 3/4.", "3 consecutive jumps of 1/4 land on 3/4 (3 × 1/4 = 3/4).")
            h_clean = h_clean.replace("Model A shows 3 consecutive jumps of 1/4 landing on 3/4.", "3 consecutive jumps of 1/4 land on 3/4 (3 × 1/4 = 3/4).")
            h_clean = h_clean.replace("Total is 1 7/8. Model A displays 1 full whole bar plus 7 eighths shaded.", "Total is 1 7/8, modeled by 1 full whole bar plus 7 eighths shaded.")
            h_clean = h_clean.replace("Combine: 1 + 7/8 = 1 7/8. Model A displays 1 full bar plus 7 eighths shaded.", "Combine: 1 + 7/8 = 1 7/8, modeled by 1 full bar plus 7 eighths shaded.")
            new_hints.append(h_clean)
        q["hints"] = new_hints

        if "explanation" in q:
            for step, text in q["explanation"].items():
                t_clean = text.replace("For Model A, 3 × 4 = 12 square units. Model B has 10, Model C has 15, Model D has 16.", "3 × 4 = 12 square units forms the target area.")
                t_clean = t_clean.replace("Model A has 0 leftover stars.", "The correct model has 0 leftover stars.")
                t_clean = t_clean.replace("Model: Model A has 6 rows and 6 columns: 6 × 6 = 36.", "Model: 6 rows and 6 columns form 6 × 6 = 36.")
                t_clean = t_clean.replace("Solve: Model A is a square 6 × 6 array.", "Solve: A square 6 × 6 array models 36.")
                t_clean = t_clean.replace("Verify: Model A contains every valid factor without extras.", "Verify: The factor list contains every valid factor without extras.")
                t_clean = t_clean.replace("Verify: Exactly 12 factors in Model A.", "Verify: Exactly 12 factors.")
                t_clean = t_clean.replace("Solve: Model A shows a 2 × 4 grid with 6 shaded cells.", "Solve: A 2 × 4 grid with 6 shaded cells models 6/8.")
                t_clean = t_clean.replace("Solve: Model A shows a 2 × 4 grid with 6 cells shaded, representing 6/8.", "Solve: A 2 × 4 grid with 6 cells shaded represents 6/8.")
                t_clean = t_clean.replace("Verify: Model A represents 4/6, which is equivalent to 2/3.", "Verify: 4/6 is equivalent to 2/3.")
                t_clean = t_clean.replace("Solve: Model A aligns 4 shaded twelfths with 1 shaded third.", "Solve: 4 shaded twelfths aligns with 1 shaded third.")
                t_clean = t_clean.replace("Solve: Model A aligns 4 twelfths with 1 third.", "Solve: 4 twelfths aligns with 1 third.")
                t_clean = t_clean.replace("Solve: Option A accurately states 5/8 > 1/2 and 4/10 < 1/2.", "Solve: 5/8 > 1/2 and 4/10 < 1/2.")
                t_clean = t_clean.replace("Solve: Model A is the unit fraction decomposition.", "Solve: The unit fraction decomposition uses only unit fractions.")
                t_clean = t_clean.replace("Solve: Model A is the only option showing exclusively unit fractions.", "Solve: Only unit fractions (1/8) are used.")
                t_clean = t_clean.replace("Model: Test Option A: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.", "Model: Test: 1/8 + 1/8 + 3/8 = (1 + 1 + 3)/8 = 5/8.")
                t_clean = t_clean.replace("Solve: Option A correctly equals 5/8.", "Solve: 1/8 + 1/8 + 3/8 correctly equals 5/8.")
                t_clean = t_clean.replace("Verify: Option B equals 5/4, and Option C equals 6/8.", "Verify: Distractors equal 5/4 and 6/8.")
                t_clean = t_clean.replace("Solve: Option A shows 4 copies of 1/5.", "Solve: 4 copies of 1/5 equals 4/5.")
                t_clean = t_clean.replace("Solve: Model A shows 1 full bar + 7/8 bar.", "Solve: 1 full bar + 7/8 bar equals 1 7/8.")
                t_clean = t_clean.replace("Solve: Model A shows 1 complete whole bar and 7 out of 8 parts in the second bar.", "Solve: 1 complete whole bar and 7 out of 8 parts equals 1 7/8.")
                q["explanation"][step] = t_clean

        # Handle MCQ
        if q.get("format") == "mc" and "options" in q:
            opts = q["options"]
            # Find the correct option
            correct_opt = None
            distractors = []
            for o in opts:
                if o.get("correct") is True or o.get("id") == q.get("answerKey"):
                    correct_opt = dict(o)
                    correct_opt["correct"] = True
                else:
                    d = dict(o)
                    d["correct"] = False
                    distractors.append(d)

            target_idx = target_mc_indices[mc_counter % len(target_mc_indices)]
            mc_counter += 1

            new_opts = distractors[:target_idx] + [correct_opt] + distractors[target_idx:]
            for idx, o in enumerate(new_opts):
                o["id"] = letters[idx]
            q["options"] = new_opts
            q["answerKey"] = letters[target_idx]

        # Handle Visual
        if q.get("format") == "visual" and "visualCards" in q:
            cards = q["visualCards"]
            correct_card = None
            distractor_cards = []
            for c in cards:
                if c.get("id") == q.get("answerKey") or c.get("correct") is True:
                    correct_card = dict(c)
                    correct_card["correct"] = True
                else:
                    d = dict(c)
                    d["correct"] = False
                    distractor_cards.append(d)

            target_idx = target_vis_indices[vis_counter % len(target_vis_indices)]
            vis_counter += 1

            new_cards = distractor_cards[:target_idx] + [correct_card] + distractor_cards[target_idx:]
            for idx, c in enumerate(new_cards):
                c["id"] = opt_ids[idx]
                # Update label letter
                raw_label = c["label"]
                prefix_map = ["Model", "Pair", "Point", "Rainbow"]
                for p in prefix_map:
                    if raw_label.startswith(p + " "):
                        # e.g. Model A: -> Model B:
                        parts = raw_label.split(":", 1)
                        if len(parts) == 2:
                            c["label"] = f"{p} {letters[idx]}:{parts[1]}"
                        break
            q["visualCards"] = new_cards
            q["answerKey"] = opt_ids[target_idx]

    return questions

# Run balance on all units
u1 = balance_unit_questions(UNIT1_QUESTIONS, 1)
u2 = balance_unit_questions(UNIT2_QUESTIONS, 2)
u3 = balance_unit_questions(UNIT3_QUESTIONS, 3)

from collections import Counter
print("Unit 1 MC keys:", Counter(q['answerKey'] for q in u1 if q['format'] == 'mc'))
print("Unit 1 Visual keys:", Counter(q['answerKey'] for q in u1 if q['format'] == 'visual'))
print("Unit 2 MC keys:", Counter(q['answerKey'] for q in u2 if q['format'] == 'mc'))
print("Unit 2 Visual keys:", Counter(q['answerKey'] for q in u2 if q['format'] == 'visual'))
print("Unit 3 MC keys:", Counter(q['answerKey'] for q in u3 if q['format'] == 'mc'))
print("Unit 3 Visual keys:", Counter(q['answerKey'] for q in u3 if q['format'] == 'visual'))
