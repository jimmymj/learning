# 4th Grade Math Quarter 2 Question Bank (Exactly 60 Graded Questions)
# Aligned with CMS Quarter 2 / Illustrative Mathematics / NC SCOS
# Cluster 1: Fractions Continuation & Decimal Notation (NC.4.NF.1, 2, 3, 6, 7) - 20 Q
# Cluster 2: Place Value, Multi-Digit Operations & Multiplicative Comparison (NC.4.NBT.1, 2, 5, 6; NC.4.OA.1, 2, 3) - 20 Q
# Cluster 3: Area, Perimeter, Measurement & Fractional Data (NC.4.MD.1, 2, 3, 4, 8) - 20 Q

CLUSTER1_QUESTIONS = [
    # Easy (6 Items)
    {
        "id": "q2_c1_q01", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "visual",
        "question": "Which grid model represents the decimal 0.6 (6 tenths)? Select the grid that has exactly 6 out of 10 equal columns shaded.",
        "visualCards": [
            {"id": "v1", "label": "Grid A", "desc": "6 columns shaded out of 10 columns (6/10 = 0.6)", "svgType": "tenths_grid", "shaded": 6, "total": 10},
            {"id": "v2", "label": "Grid B", "desc": "6 individual squares shaded out of 100 (6/100 = 0.06)", "svgType": "hundredths_grid", "shaded": 6, "total": 100},
            {"id": "v3", "label": "Grid C", "desc": "4 columns shaded out of 10 columns (4/10 = 0.4)", "svgType": "tenths_grid", "shaded": 4, "total": 10},
            {"id": "v4", "label": "Grid D", "desc": "60 squares shaded out of 100 in 6 columns", "svgType": "tenths_grid", "shaded": 2, "total": 10}
        ],
        "answerKey": "v1", "formattedAnswer": "Grid A: 6 columns shaded out of 10 (6/10 = 0.6)",
        "hints": [
            "Tenths are represented by dividing a whole into 10 equal vertical columns.",
            "6 tenths means shading 6 full columns out of 10.",
            "Shading 6 individual little squares out of 100 is 6 hundredths (0.06), not 6 tenths (0.6)."
        ],
        "explanation": "0.6 represents 6 tenths, which corresponds to 6 out of 10 equal columns shaded on a tenths grid. 6/10 is equivalent to 60/100 or 0.60.",
        "misconception": "Confusing tenths with hundredths (0.6 vs 0.06)"
    },
    {
        "id": "q2_c1_q02", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "mc",
        "question": "What is the decimal equivalent of the fraction 7/10?",
        "options": [
            {"id": "optA", "text": "0.07", "correct": False},
            {"id": "optB", "text": "0.7", "correct": True},
            {"id": "optC", "text": "7.0", "correct": False},
            {"id": "optD", "text": "0.707", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "0.7 (7 tenths)",
        "hints": [
            "The first digit to the right of the decimal point is the tenths place.",
            "7/10 has a 7 in the tenths place, written as 0.7.",
            "0.07 has 7 in the hundredths place, which equals 7/100."
        ],
        "explanation": "7/10 is read as 'seven tenths'. In decimal notation, the first digit after the decimal point is the tenths position, giving 0.7.",
        "misconception": "Placing the digit in the hundredths place instead of tenths"
    },
    {
        "id": "q2_c1_q03", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "numberline",
        "question": "Drag the slider to plot Point P at the location representing the decimal 0.4.",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.05, "answerKey": 0.4,
        "formattedAnswer": "Coordinate 0.40 (4th tenths tick mark)",
        "hints": [
            "The number line is divided from 0 to 1 with tick marks every tenth (0.1, 0.2, 0.3...).",
            "Count 4 tick marks to the right of 0.",
            "Point P belongs right on 0.4 (which is also 4/10 or 40/100)."
        ],
        "explanation": "0.4 is 4 tenths along the number line between 0 and 1. It is positioned at 4/10 (or coordinate 0.40).",
        "misconception": "Misreading interval step sizes on number lines"
    },
    {
        "id": "q2_c1_q04", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "dragdrop",
        "question": "Match each fraction card to its equivalent decimal target slot.",
        "dragData": {
            "items": [
                {"id": "c_310", "text": "3/10"},
                {"id": "c_25100", "text": "25/100"},
                {"id": "c_8100", "text": "8/100"},
                {"id": "c_910", "text": "9/10"}
            ],
            "slots": [
                {"id": "slot_03", "label": "0.3", "accept": "c_310"},
                {"id": "slot_025", "label": "0.25", "accept": "c_25100"},
                {"id": "slot_008", "label": "0.08", "accept": "c_8100"},
                {"id": "slot_09", "label": "0.9", "accept": "c_910"}
            ]
        },
        "answerKey": {"slot_03": ["c_310"], "slot_025": ["c_25100"], "slot_008": ["c_8100"], "slot_09": ["c_910"]},
        "formattedAnswer": "3/10 = 0.3, 25/100 = 0.25, 8/100 = 0.08, 9/10 = 0.9",
        "hints": [
            "Tenths have 1 decimal place; hundredths have 2 decimal places.",
            "3/10 = 0.3 and 9/10 = 0.9.",
            "8/100 needs a zero in tenths place: 0.08."
        ],
        "explanation": "3/10 = 0.3, 25/100 = 0.25, 8/100 = 0.08, and 9/10 = 0.9. Each fraction directly reflects its place value.",
        "misconception": "Writing 8/100 as 0.8 instead of 0.08"
    },
    {
        "id": "q2_c1_q05", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "mc",
        "question": "A 100-square grid has 45 squares shaded. What fraction and decimal describe the shaded part?",
        "options": [
            {"id": "optA", "text": "45/10 and 4.5", "correct": False},
            {"id": "optB", "text": "45/100 and 0.45", "correct": True},
            {"id": "optC", "text": "4/5 and 0.8", "correct": False},
            {"id": "optD", "text": "45/1000 and 0.045", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "45/100 and 0.45",
        "hints": [
            "There are 100 total equal squares in the whole grid.",
            "The numerator is the number of shaded parts (45), denominator is total parts (100).",
            "45/100 is read as forty-five hundredths = 0.45."
        ],
        "explanation": "Out of 100 total equal squares, 45 shaded squares represent the fraction 45/100 and the decimal 0.45.",
        "misconception": "Confusing whole number division by 10 vs 100"
    },
    {
        "id": "q2_c1_q06", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "easy",
        "standard": "NC.4.NF.6", "format": "numberline",
        "question": "Drag Point P to represent the decimal 0.06 on the number line.",
        "nlMin": 0.0, "nlMax": 0.2, "step": 0.01, "answerKey": 0.06,
        "formattedAnswer": "Coordinate 0.06 (6th hundredths mark after 0)",
        "hints": [
            "0.06 is 6 hundredths, which is less than 1 tenth (0.10).",
            "Each tick mark represents 1 hundredth (0.01).",
            "Count 6 small tick marks to the right of 0."
        ],
        "explanation": "0.06 represents 6 hundredths (6/100). On a number line scaled by hundredths, it sits 6 units past 0.",
        "misconception": "Confusing 0.06 with 0.60"
    },

    # Medium (10 Items)
    {
        "id": "q2_c1_q07", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "mc",
        "question": "Which comparison statement is TRUE for 0.8 and 0.74?",
        "options": [
            {"id": "optA", "text": "0.8 < 0.74 because 8 is less than 74", "correct": False},
            {"id": "optB", "text": "0.8 = 0.74 because both have single digits", "correct": False},
            {"id": "optC", "text": "0.8 > 0.74 because 0.8 is 80 hundredths and 80 > 74", "correct": True},
            {"id": "optD", "text": "0.8 < 0.74 because hundredths are always larger than tenths", "correct": False}
        ],
        "answerKey": "optC", "formattedAnswer": "0.8 > 0.74 (0.80 > 0.74)",
        "hints": [
            "Think about money or hundredths: 0.8 = 0.80 (80 cents or 80 hundredths).",
            "Compare 80 hundredths with 74 hundredths.",
            "80 hundredths is greater than 74 hundredths, so 0.8 > 0.74."
        ],
        "explanation": "0.8 is equivalent to 80/100 or 0.80. Since 80 hundredths is greater than 74 hundredths, 0.8 > 0.74. Comparing '8 < 74' is a common whole-number mistake that ignores place value.",
        "misconception": "Whole-number bias: assuming 0.74 > 0.8 because 74 > 8"
    },
    {
        "id": "q2_c1_q08", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.6", "format": "dragdrop",
        "question": "Solve 4/10 + 35/100. Drag the equivalent converted fraction and final sum to complete the equation.",
        "dragData": {
            "items": [
                {"id": "f_40100", "text": "40/100"},
                {"id": "f_75100", "text": "75/100"},
                {"id": "f_39110", "text": "39/110"},
                {"id": "f_39100", "text": "39/100"}
            ],
            "slots": [
                {"id": "slot_conv", "label": "4/10 converted to hundredths", "accept": "f_40100"},
                {"id": "slot_total", "label": "Final Sum", "accept": "f_75100"}
            ]
        },
        "answerKey": {"slot_conv": ["f_40100"], "slot_total": ["f_75100"]},
        "formattedAnswer": "4/10 = 40/100, and 40/100 + 35/100 = 75/100",
        "hints": [
            "You cannot add tenths directly to hundredths without converting to a common denominator.",
            "Convert 4/10 to hundredths by multiplying numerator and denominator by 10: 4/10 = 40/100.",
            "Now add 40/100 + 35/100 = 75/100."
        ],
        "explanation": "4/10 is equivalent to 40/100. Adding 40/100 + 35/100 gives 75/100 (or 0.75 in decimal notation). Never add denominators together!",
        "misconception": "Adding numerators and denominators directly (4+35)/(10+100) = 39/110"
    },
    {
        "id": "q2_c1_q09", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.1", "format": "visual",
        "question": "Which visual grid shows a fraction equivalent to 3/10?",
        "visualCards": [
            {"id": "g1", "label": "Model A", "desc": "3 individual squares shaded out of 100 (3/100)", "svgType": "hundredths_grid", "shaded": 3, "total": 100},
            {"id": "g2", "label": "Model B", "desc": "30 individual squares shaded out of 100 (30/100)", "svgType": "hundredths_grid", "shaded": 30, "total": 100},
            {"id": "g3", "label": "Model C", "desc": "13 individual squares shaded out of 100 (13/100)", "svgType": "hundredths_grid", "shaded": 13, "total": 100},
            {"id": "g4", "label": "Model D", "desc": "70 individual squares shaded out of 100 (70/100)", "svgType": "hundredths_grid", "shaded": 70, "total": 100}
        ],
        "answerKey": "g2", "formattedAnswer": "Model B: 30/100 (30 shaded squares out of 100)",
        "hints": [
            "3/10 = (3 × 10) / (10 × 10) = 30/100.",
            "Each column of 10 on a hundredths grid is 1 tenth.",
            "3 tenths equals 3 full columns = 30 squares."
        ],
        "explanation": "3/10 is equivalent to 30/100. Model B shades 3 full columns of 10 squares each, totaling 30/100.",
        "misconception": "Equating 3/10 to 3/100"
    },
    {
        "id": "q2_c1_q10", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.6", "format": "mc",
        "question": "Find the sum: 6/10 + 28/100.",
        "options": [
            {"id": "optA", "text": "34/110", "correct": False},
            {"id": "optB", "text": "34/100", "correct": False},
            {"id": "optC", "text": "88/100", "correct": True},
            {"id": "optD", "text": "628/100", "correct": False}
        ],
        "answerKey": "optC", "formattedAnswer": "88/100 (0.88)",
        "hints": [
            "Convert 6/10 into hundredths first: 6/10 = 60/100.",
            "Add the numerators: 60 + 28 = 88.",
            "The common denominator remains 100."
        ],
        "explanation": "6/10 = 60/100. Adding 60/100 + 28/100 = 88/100 = 0.88.",
        "misconception": "Adding 6 + 28 = 34 without scaling tenths to hundredths"
    },
    {
        "id": "q2_c1_q11", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "numberline",
        "question": "Plot Point P at 0.75 (the benchmark fraction 3/4).",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.05, "answerKey": 0.75,
        "formattedAnswer": "Coordinate 0.75 (3/4 benchmark, midway between 0.7 and 0.8)",
        "hints": [
            "0.75 is three-quarters of the way from 0 to 1.",
            "It sits exactly halfway between 0.70 and 0.80.",
            "0.75 = 75/100 = 3/4."
        ],
        "explanation": "0.75 is equivalent to 75/100, which simplifies to 3/4. On the number line, it is positioned halfway between 0.70 and 0.80.",
        "misconception": "Confusing 0.75 with 0.075 or plotting at 0.7"
    },
    {
        "id": "q2_c1_q12", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "dragdrop",
        "question": "Drag the correct comparison symbol (>, <, or =) into each circle.",
        "dragData": {
            "items": [
                {"id": "sym_gt", "text": ">"},
                {"id": "sym_lt1", "text": "<"},
                {"id": "sym_lt2", "text": "<"},
                {"id": "sym_eq", "text": "="}
            ],
            "slots": [
                {"id": "slot1", "label": "0.5  O  0.50", "accept": "sym_eq"},
                {"id": "slot2", "label": "0.3  O  0.29", "accept": "sym_gt"},
                {"id": "slot3", "label": "0.09  O  0.1", "accept": "sym_lt1"},
                {"id": "slot4", "label": "0.64  O  0.7", "accept": "sym_lt2"}
            ]
        },
        "answerKey": {"slot1": ["sym_eq"], "slot2": ["sym_gt"], "slot3": ["sym_lt1"], "slot4": ["sym_lt2"]},
        "formattedAnswer": "0.5 = 0.50, 0.3 > 0.29, 0.09 < 0.1, 0.64 < 0.7",
        "hints": [
            "Write each decimal with 2 decimal places to compare easily.",
            "0.5 = 0.50; 0.3 = 0.30 (and 0.30 > 0.29).",
            "0.1 = 0.10 (and 0.09 < 0.10); 0.7 = 0.70 (and 0.64 < 0.70)."
        ],
        "explanation": "Padding with trailing zeros aligns place values: 0.50 = 0.50; 0.30 > 0.29; 0.09 < 0.10; 0.64 < 0.70.",
        "misconception": "Believing longer decimal strings are always greater (e.g. 0.29 > 0.3)"
    },
    {
        "id": "q2_c1_q13", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "mc",
        "question": "Which explanation mathematically proves that 0.4 is greater than 0.25?",
        "options": [
            {"id": "optA", "text": "4 is greater than 2, so tenths are always bigger than hundredths", "correct": False},
            {"id": "optB", "text": "0.4 = 40/100, and 40 hundredths is greater than 25 hundredths", "correct": True},
            {"id": "optC", "text": "0.25 has more digits, so 0.25 must be smaller", "correct": False},
            {"id": "optD", "text": "0.4 is closer to 0 than 0.25", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "0.4 = 40/100, and 40 hundredths > 25 hundredths",
        "hints": [
            "Convert both numbers to the same unit (hundredths).",
            "0.4 = 4/10 = 40/100.",
            "0.25 = 25/100. Compare 40 hundredths with 25 hundredths."
        ],
        "explanation": "By expressing 0.4 as 0.40 (40 hundredths), it is clear that 40 hundredths is greater than 25 hundredths (0.25).",
        "misconception": "Judging size based solely on the number of digits"
    },
    {
        "id": "q2_c1_q14", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "visual",
        "question": "Which pair of models correctly compares 0.3 and 0.03?",
        "visualCards": [
            {"id": "p1", "label": "Model A", "desc": "Model A shows 3 columns (0.3) > 3 squares (0.03)", "svgType": "tenths_hundredths_pair", "tShaded": 3, "hShaded": 3},
            {"id": "p2", "label": "Model B", "desc": "Model B shows 3 squares equal to 3 columns", "svgType": "equal_pair", "tShaded": 3, "hShaded": 30},
            {"id": "p3", "label": "Model C", "desc": "Model C shows 0.3 as 30 columns", "svgType": "overflow_pair", "tShaded": 10, "hShaded": 3},
            {"id": "p4", "label": "Model D", "desc": "Model D shows 0.03 as larger than 0.3", "svgType": "inverted_pair", "tShaded": 1, "hShaded": 10}
        ],
        "answerKey": "p1", "formattedAnswer": "Model A: 3 full columns (0.3 = 30 hundredths) > 3 small squares (0.03)",
        "hints": [
            "0.3 = 3 tenths = 3 full columns of 10.",
            "0.03 = 3 hundredths = only 3 tiny individual squares.",
            "3 full columns (30 squares) is 10 times larger than 3 squares."
        ],
        "explanation": "0.3 covers 3 full vertical columns (30 hundredths squares), while 0.03 covers only 3 individual hundredths squares. Model A accurately illustrates that 0.3 > 0.03.",
        "misconception": "Treating 0.3 and 0.03 as having identical values"
    },
    {
        "id": "q2_c1_q15", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.6", "format": "numberline",
        "question": "Locate 90/100 on the number line. What decimal value does Point P land on?",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.05, "answerKey": 0.9,
        "formattedAnswer": "Coordinate 0.90 (9/10 or 90/100)",
        "hints": [
            "90/100 simplifies to 9/10.",
            "In decimal form, 9/10 = 0.9 = 0.90.",
            "Drag the slider right next to 1.0 (at 0.9)."
        ],
        "explanation": "90/100 = 9/10 = 0.90 (or 0.9). On a number line from 0 to 1, it is located at 0.90.",
        "misconception": "Plotting 90/100 at 0.09"
    },
    {
        "id": "q2_c1_q16", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "medium",
        "standard": "NC.4.NF.7", "format": "dragdrop",
        "question": "Order these decimal cards from LEAST to GREATEST into the 4 slots.",
        "dragData": {
            "items": [
                {"id": "d_005", "text": "0.05"},
                {"id": "d_02", "text": "0.2"},
                {"id": "d_045", "text": "0.45"},
                {"id": "d_08", "text": "0.8"}
            ],
            "slots": [
                {"id": "slot_pos1", "label": "Least (1st)", "accept": "d_005"},
                {"id": "slot_pos2", "label": "2nd", "accept": "d_02"},
                {"id": "slot_pos3", "label": "3rd", "accept": "d_045"},
                {"id": "slot_pos4", "label": "Greatest (4th)", "accept": "d_08"}
            ]
        },
        "answerKey": {"slot_pos1": ["d_005"], "slot_pos2": ["d_02"], "slot_pos3": ["d_045"], "slot_pos4": ["d_08"]},
        "formattedAnswer": "0.05 < 0.2 < 0.45 < 0.8 (5 hundredths < 20 hundredths < 45 hundredths < 80 hundredths)",
        "hints": [
            "Align all decimals to hundredths: 0.05, 0.20, 0.45, 0.80.",
            "Compare the hundredths values: 5 < 20 < 45 < 80.",
            "Least is 0.05; greatest is 0.8."
        ],
        "explanation": "0.05 (5 hundredths) < 0.20 (20 hundredths) < 0.45 (45 hundredths) < 0.80 (80 hundredths).",
        "misconception": "Ordering by digit count or seeing 0.8 as smaller than 0.45"
    },

    # Hard (4 Items)
    {
        "id": "q2_c1_q17", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "hard",
        "standard": "NC.4.NF.3", "format": "mc",
        "question": "A pitcher contains 5/10 liter of juice. Maria pours in an additional 28/100 liter. What is the total volume of juice in the pitcher, expressed as a decimal?",
        "options": [
            {"id": "optA", "text": "0.33 liters", "correct": False},
            {"id": "optB", "text": "0.78 liters", "correct": True},
            {"id": "optC", "text": "0.528 liters", "correct": False},
            {"id": "optD", "text": "1.28 liters", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "0.78 liters (50/100 + 28/100 = 78/100 = 0.78 L)",
        "hints": [
            "Convert 5/10 liter into hundredths: 5/10 = 50/100.",
            "Add the hundredths: 50/100 + 28/100 = 78/100 liters.",
            "Convert 78/100 into decimal form: 0.78 liters."
        ],
        "explanation": "5/10 L = 50/100 L. Adding 50/100 + 28/100 = 78/100 = 0.78 liters. Adding 5 + 28 without converting creates the common 0.33 distractor error.",
        "misconception": "Direct addition of 5 + 28 = 33 without common denominator"
    },
    {
        "id": "q2_c1_q18", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "hard",
        "standard": "NC.4.NF.7", "format": "mc",
        "question": "In a 100-meter dash, runner times were recorded: Maya ran 12.4 seconds, Zoe ran 12.35 seconds, and Liam ran 12.08 seconds. Who won the race (fastest time)?",
        "options": [
            {"id": "optA", "text": "Liam (12.08 seconds)", "correct": True},
            {"id": "optB", "text": "Zoe (12.35 seconds)", "correct": False},
            {"id": "optC", "text": "Maya (12.4 seconds)", "correct": False},
            {"id": "optD", "text": "Maya and Zoe tied", "correct": False}
        ],
        "answerKey": "optA", "formattedAnswer": "Liam with 12.08 seconds (12.08 < 12.35 < 12.40)",
        "hints": [
            "In a race, the fastest runner has the LOWEST time.",
            "Compare: 12.40 vs 12.35 vs 12.08.",
            "12.08 has 0 tenths, while 12.35 has 3 tenths and 12.40 has 4 tenths. 12.08 is the lowest."
        ],
        "explanation": "To compare times, pad with hundredths: Maya = 12.40 s, Zoe = 12.35 s, Liam = 12.08 s. The lowest time wins: 12.08 < 12.35 < 12.40. Liam won the race.",
        "misconception": "Picking highest number for race winner or thinking 12.4 < 12.08"
    },
    {
        "id": "q2_c1_q19", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "hard",
        "standard": "NC.4.NF.6", "format": "numberline",
        "question": "A student starts at 0.3 on the number line and jumps forward +0.45. What point does the student land on?",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.05, "answerKey": 0.75,
        "formattedAnswer": "Coordinate 0.75 (0.30 + 0.45 = 0.75)",
        "hints": [
            "Rewrite 0.3 as 0.30 (30 hundredths).",
            "Add the jump: 0.30 + 0.45 = 0.75 (75 hundredths).",
            "Move Point P to 0.75."
        ],
        "explanation": "0.3 = 0.30. Adding a jump of 0.45 gives 0.30 + 0.45 = 0.75. The student lands on 0.75 (or 75/100).",
        "misconception": "Adding 0.3 + 0.45 = 0.48 by misaligning tenths and hundredths"
    },
    {
        "id": "q2_c1_q20", "cluster": "c1", "clusterTitle": "Fractions & Decimals", "tier": "hard",
        "standard": "NC.4.NF.6", "format": "dragdrop",
        "question": "Sort each equation card into the TRUE or FALSE container.",
        "dragData": {
            "items": [
                {"id": "eq_t1", "text": "7/10 + 5/100 = 75/100"},
                {"id": "eq_t2", "text": "2/10 + 30/100 = 50/100"},
                {"id": "eq_f1", "text": "4/10 + 3/100 = 43/110"},
                {"id": "eq_f2", "text": "0.6 = 0.06"}
            ],
            "slots": [
                {"id": "box_true", "label": "TRUE Equations", "accept": ["eq_t1", "eq_t2"]},
                {"id": "box_false", "label": "FALSE Equations", "accept": ["eq_f1", "eq_f2"]}
            ]
        },
        "answerKey": {"box_true": ["eq_t1", "eq_t2"], "box_false": ["eq_f1", "eq_f2"]},
        "formattedAnswer": "TRUE: 7/10 + 5/100 = 75/100 and 2/10 + 30/100 = 50/100 | FALSE: 4/10 + 3/100 = 43/110 and 0.6 = 0.06",
        "hints": [
            "7/10 = 70/100, so 70/100 + 5/100 = 75/100 (True).",
            "2/10 = 20/100, so 20/100 + 30/100 = 50/100 (True).",
            "You never add denominators (110 is wrong), and 6 tenths does not equal 6 hundredths."
        ],
        "explanation": "7/10 + 5/100 = 75/100 and 2/10 + 30/100 = 50/100 are mathematically true. 4/10 + 3/100 = 43/110 is false (sum is 43/100). 0.6 = 0.06 is false (0.6 is 10 times larger).",
        "misconception": "Believing denominators add together or 0.6 = 0.06"
    }
]

CLUSTER2_QUESTIONS = [
    # Easy (6 Items)
    {
        "id": "q2_c2_q01", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.OA.1", "format": "dragdrop",
        "question": "Sam has 8 trading cards. Maya has 4 times as many cards as Sam. Drag cards to build the multiplicative equation for Maya's cards (c).",
        "dragData": {
            "items": [
                {"id": "num_8", "text": "8"},
                {"id": "op_mult", "text": "×"},
                {"id": "num_4", "text": "4"},
                {"id": "ans_32", "text": "32"}
            ],
            "slots": [
                {"id": "slot_factor1", "label": "Sam's Cards", "accept": "num_8"},
                {"id": "slot_op", "label": "Multiplier Symbol", "accept": "op_mult"},
                {"id": "slot_factor2", "label": "Scale Factor", "accept": "num_4"},
                {"id": "slot_product", "label": "Total Cards (c)", "accept": "ans_32"}
            ]
        },
        "answerKey": {"slot_factor1": ["num_8"], "slot_op": ["op_mult"], "slot_factor2": ["num_4"], "slot_product": ["ans_32"]},
        "formattedAnswer": "8 × 4 = 32 cards",
        "hints": [
            "'4 times as many' means multiplication, not addition.",
            "Multiply Sam's 8 cards by 4.",
            "8 × 4 = 32 cards."
        ],
        "explanation": "Multiplicative comparison compares quantities through multiplication: 8 cards × 4 = 32 cards. Additive comparison would be '4 more than 8 = 12'.",
        "misconception": "Confusing '4 times as many' with '4 more than' (8 + 4 = 12)"
    },
    {
        "id": "q2_c2_q02", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.NBT.1", "format": "mc",
        "question": "In the number 55,555, how does the value of the 5 in the thousands place compare to the value of the 5 in the hundreds place?",
        "options": [
            {"id": "optA", "text": "It is equal to the 5 in the hundreds place", "correct": False},
            {"id": "optB", "text": "It is 10 times greater", "correct": True},
            {"id": "optC", "text": "It is 100 times greater", "correct": False},
            {"id": "optD", "text": "It is 5 times greater", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "10 times greater (5,000 vs 500)",
        "hints": [
            "The 5 in the thousands place has a value of 5,000.",
            "The 5 in the hundreds place has a value of 500.",
            "5,000 ÷ 500 = 10. Shifting one place value to the left multiplies by 10."
        ],
        "explanation": "In our base-ten number system, a digit in any place represents 10 times what it represents in the place to its right. 5,000 is 10 times 500.",
        "misconception": "Focusing only on face value (both digits are 5)"
    },
    {
        "id": "q2_c2_q03", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.NBT.5", "format": "visual",
        "question": "Which area model correctly shows 23 × 3 decomposed into partial products?",
        "visualCards": [
            {"id": "m1", "label": "Model A", "desc": "(20 × 3 = 60) and (3 × 3 = 9) -> Total = 69", "svgType": "area_2x1", "part1": 60, "part2": 9, "total": 69},
            {"id": "m2", "label": "Model B", "desc": "(20 × 3 = 23) and (3 × 3 = 9) -> Total = 32", "svgType": "area_2x1", "part1": 23, "part2": 9, "total": 32},
            {"id": "m3", "label": "Model C", "desc": "(2 × 3 = 6) and (3 × 3 = 9) -> Total = 15", "svgType": "area_2x1", "part1": 6, "part2": 9, "total": 15},
            {"id": "m4", "label": "Model D", "desc": "(20 × 30 = 600) and (3 × 3 = 9) -> Total = 609", "svgType": "area_2x1", "part1": 600, "part2": 9, "total": 609}
        ],
        "answerKey": "m1", "formattedAnswer": "Model A: (20 × 3 = 60) + (3 × 3 = 9) = 69",
        "hints": [
            "Decompose 23 by place value into expanded form: 20 + 3.",
            "Multiply each part by 3: 20 × 3 = 60 and 3 × 3 = 9.",
            "Sum the partial products: 60 + 9 = 69."
        ],
        "explanation": "23 × 3 = (20 × 3) + (3 × 3) = 60 + 9 = 69. Model A partitions the rectangle into 20 and 3, yielding the correct partial products.",
        "misconception": "Multiplying face values: 2 × 3 = 6 instead of 20 × 3 = 60"
    },
    {
        "id": "q2_c2_q04", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.NBT.2", "format": "mc",
        "question": "What is 43,805 written in expanded form?",
        "options": [
            {"id": "optA", "text": "40,000 + 3,000 + 80 + 5", "correct": False},
            {"id": "optB", "text": "4,000 + 300 + 80 + 5", "correct": False},
            {"id": "optC", "text": "40,000 + 3,000 + 800 + 5", "correct": True},
            {"id": "optD", "text": "43,000 + 805", "correct": False}
        ],
        "answerKey": "optC", "formattedAnswer": "40,000 + 3,000 + 800 + 5",
        "hints": [
            "Look at the place of each digit: 4 is in Ten-Thousands, 3 is in Thousands, 8 is in Hundreds, 0 is in Tens, 5 is in Ones.",
            "4 ten-thousands = 40,000; 3 thousands = 3,000; 8 hundreds = 800; 5 ones = 5.",
            "Sum = 40,000 + 3,000 + 800 + 5."
        ],
        "explanation": "43,805 decomposes into 40,000 + 3,000 + 800 + 0 + 5 = 40,000 + 3,000 + 800 + 5.",
        "misconception": "Misplacing place value for the hundreds or tens digits"
    },
    {
        "id": "q2_c2_q05", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.OA.1", "format": "numberline",
        "question": "Model 7 × 4 on the number line. What product does 4 equal jumps of 7 land on?",
        "nlMin": 0, "nlMax": 35, "step": 1, "answerKey": 28,
        "formattedAnswer": "Point at 28 (4 jumps of size 7: 7, 14, 21, 28)",
        "hints": [
            "Start at 0.",
            "Take 4 jumps of size 7: 0 -> 7 -> 14 -> 21 -> 28.",
            "Move Point P to 28."
        ],
        "explanation": "7 × 4 = 28. On a number line, 4 repeated jumps of 7 land squarely at 28.",
        "misconception": "Adding 7 + 4 = 11 instead of multiplying"
    },
    {
        "id": "q2_c2_q06", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "easy",
        "standard": "NC.4.OA.1", "format": "dragdrop",
        "question": "Match each multiplication fact card to its multiplicative comparison description.",
        "dragData": {
            "items": [
                {"id": "eq_35", "text": "35 = 5 × 7"},
                {"id": "eq_24", "text": "24 = 6 × 4"},
                {"id": "eq_18", "text": "18 = 9 × 2"}
            ],
            "slots": [
                {"id": "s_35", "label": "35 is 5 times as many as 7", "accept": "eq_35"},
                {"id": "s_24", "label": "24 is 6 times as many as 4", "accept": "eq_24"},
                {"id": "s_18", "label": "18 is 9 times as many as 2", "accept": "eq_18"}
            ]
        },
        "answerKey": {"s_35": ["eq_35"], "s_24": ["eq_24"], "s_18": ["eq_18"]},
        "formattedAnswer": "35 is 5 times as many as 7 (35 = 5 × 7), 24 is 6 times as many as 4 (24 = 6 × 4), 18 is 9 times as many as 2 (18 = 9 × 2)",
        "hints": [
            "Read 'a is n times as many as b' as equation a = n × b.",
            "35 = 5 × 7; 24 = 6 × 4; 18 = 9 × 2."
        ],
        "explanation": "Each equation expresses a multiplicative comparison between two numbers and their product.",
        "misconception": "Mixing up factor pairs and comparison statements"
    },

    # Medium (10 Items)
    {
        "id": "q2_c2_q07", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.1", "format": "mc",
        "question": "In the number 44,250, how does the value of the digit 4 in the ten-thousands place compare to the value of the digit 4 in the thousands place?",
        "options": [
            {"id": "optA", "text": "It is 4 times greater", "correct": False},
            {"id": "optB", "text": "It is 10 times greater", "correct": True},
            {"id": "optC", "text": "It is 100 times greater", "correct": False},
            {"id": "optD", "text": "It is 1,000 times greater", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "It is 10 times greater (40,000 vs 4,000)",
        "hints": [
            "Ten-thousands digit value: 40,000.",
            "Thousands digit value: 4,000.",
            "40,000 is 10 times 4,000. Moving 1 place to the left multiplies by 10."
        ],
        "explanation": "The 4 in the ten-thousands place is worth 40,000. The 4 in the thousands place is worth 4,000. 40,000 is 10 times 4,000.",
        "misconception": "Confusing digit value (4) with positional multiplier (10)"
    },
    {
        "id": "q2_c2_q08", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.5", "format": "visual",
        "question": "An area model for 36 × 4 is split into (30 + 6) × 4. What is the value of the partial product for 30 × 4?",
        "visualCards": [
            {"id": "c1", "label": "Model A", "desc": "Box has 12 (3 × 4 = 12)", "svgType": "area_error", "val": 12},
            {"id": "c2", "label": "Model B", "desc": "Box has 120 (30 × 4 = 120)", "svgType": "area_correct", "val": 120},
            {"id": "c3", "label": "Model C", "desc": "Box has 34 (30 + 4 = 34)", "svgType": "area_error", "val": 34},
            {"id": "c4", "label": "Model D", "desc": "Box has 144 (Total product)", "svgType": "area_error", "val": 144}
        ],
        "answerKey": "c2", "formattedAnswer": "Model B: 120 (3 tens × 4 = 12 tens = 120)",
        "hints": [
            "30 is 3 tens.",
            "3 tens × 4 = 12 tens.",
            "12 tens is 120 (include the place-value zero!)."
        ],
        "explanation": "30 × 4 = 120. Leaving out the zero (writing 12) is a common error caused by multiplying only the single digits.",
        "misconception": "Partial product zero omission: 3 × 4 = 12 instead of 120"
    },
    {
        "id": "q2_c2_q09", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.5", "format": "mc",
        "question": "Find the product of 312 × 4 using partial products.",
        "options": [
            {"id": "optA", "text": "1,248 (1,200 + 40 + 8)", "correct": True},
            {"id": "optB", "text": "128 (12 + 4 + 8)", "correct": False},
            {"id": "optC", "text": "1,288", "correct": False},
            {"id": "optD", "text": "1,240", "correct": False}
        ],
        "answerKey": "optA", "formattedAnswer": "1,248 (300 × 4 = 1,200; 10 × 4 = 40; 2 × 4 = 8)",
        "hints": [
            "Decompose 312: 300 + 10 + 2.",
            "Multiply each by 4: 300 × 4 = 1,200; 10 × 4 = 40; 2 × 4 = 8.",
            "Add together: 1,200 + 40 + 8 = 1,248."
        ],
        "explanation": "312 × 4 = (300 × 4) + (10 × 4) + (2 × 4) = 1,200 + 40 + 8 = 1,248.",
        "misconception": "Adding digits without accounting for place-value zeros"
    },
    {
        "id": "q2_c2_q10", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.6", "format": "dragdrop",
        "question": "Divide 158 by 4 using partial quotients. Drag the quotient chunks and remainder into place.",
        "dragData": {
            "items": [
                {"id": "chunk_30", "text": "30 (4 × 30 = 120)"},
                {"id": "chunk_9", "text": "9 (4 × 9 = 36)"},
                {"id": "rem_2", "text": "Remainder: 2"},
                {"id": "err_5", "text": "Remainder: 5"}
            ],
            "slots": [
                {"id": "slot_c1", "label": "1st Partial Quotient", "accept": "chunk_30"},
                {"id": "slot_c2", "label": "2nd Partial Quotient", "accept": "chunk_9"},
                {"id": "slot_rem", "label": "Leftover Remainder", "accept": "rem_2"}
            ]
        },
        "answerKey": {"slot_c1": ["chunk_30"], "slot_c2": ["chunk_9"], "slot_rem": ["rem_2"]},
        "formattedAnswer": "158 ÷ 4 = 39 with Remainder 2 (30 + 9 = 39, 158 - 156 = 2)",
        "hints": [
            "Take away 120 (which is 4 × 30). 158 - 120 = 38.",
            "From 38, take away 36 (which is 4 × 9). 38 - 36 = 2.",
            "Quotient is 30 + 9 = 39, remainder is 2."
        ],
        "explanation": "158 ÷ 4: 4 × 30 = 120 (leaves 38); 4 × 9 = 36 (leaves 2). Total quotient is 39 with a remainder of 2.",
        "misconception": "Stopping early with a remainder larger than the divisor"
    },
    {
        "id": "q2_c2_q11", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.2", "format": "numberline",
        "question": "Drag Point P to represent 60,000 on a number line from 0 to 100,000.",
        "nlMin": 0, "nlMax": 100000, "step": 10000, "answerKey": 60000,
        "formattedAnswer": "Coordinate 60,000 (6th ten-thousands tick mark)",
        "hints": [
            "The number line goes from 0 to 100,000 in steps of 10,000.",
            "Count 6 increments of 10,000 from 0.",
            "Position Point P at 60,000."
        ],
        "explanation": "60,000 is 6 ten-thousands along the number line between 0 and 100,000.",
        "misconception": "Confusing 60,000 with 6,000"
    },
    {
        "id": "q2_c2_q12", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.OA.2", "format": "mc",
        "question": "Leo scored 6 points in a basketball game. Mia scored 3 times as many points as Leo. How many points did Mia score?",
        "options": [
            {"id": "optA", "text": "9 points (6 + 3 = 9)", "correct": False},
            {"id": "optB", "text": "18 points (6 × 3 = 18)", "correct": True},
            {"id": "optC", "text": "2 points (6 ÷ 3 = 2)", "correct": False},
            {"id": "optD", "text": "24 points (6 × 4 = 24)", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "18 points (6 × 3 = 18)",
        "hints": [
            "'3 times as many' means multiply by 3.",
            "Multiply Leo's score (6) by 3.",
            "6 × 3 = 18."
        ],
        "explanation": "Multiplicative comparison uses multiplication: Mia's points = 6 × 3 = 18. An additive comparison error would be 6 + 3 = 9.",
        "misconception": "Adding instead of multiplying (6 + 3 = 9)"
    },
    {
        "id": "q2_c2_q13", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.5", "format": "visual",
        "question": "Which area model correctly calculates 2,413 × 3?",
        "visualCards": [
            {"id": "v1", "label": "Model A", "desc": "6,000 + 1,200 + 30 + 9 = 7,239", "svgType": "area_4x1", "sum": 7239},
            {"id": "v2", "label": "Model B", "desc": "6,000 + 120 + 30 + 9 = 6,159", "svgType": "area_4x1", "sum": 6159},
            {"id": "v3", "label": "Model C", "desc": "600 + 120 + 30 + 9 = 759", "svgType": "area_4x1", "sum": 759},
            {"id": "v4", "label": "Model D", "desc": "6,000 + 1,200 + 300 + 9 = 7,509", "svgType": "area_4x1", "sum": 7509}
        ],
        "answerKey": "v1", "formattedAnswer": "Model A: (2,000 × 3 = 6,000) + (400 × 3 = 1,200) + (10 × 3 = 30) + (3 × 3 = 9) = 7,239",
        "hints": [
            "Decompose 2,413: 2,000 + 400 + 10 + 3.",
            "Multiply each part by 3: 6,000, 1,200, 30, and 9.",
            "Sum = 7,239."
        ],
        "explanation": "2,413 × 3 = (2,000 × 3) + (400 × 3) + (10 × 3) + (3 × 3) = 6,000 + 1,200 + 30 + 9 = 7,239.",
        "misconception": "Miscalculating 400 × 3 as 120 instead of 1,200"
    },
    {
        "id": "q2_c2_q14", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.6", "format": "mc",
        "question": "What is 95 divided by 6?",
        "options": [
            {"id": "optA", "text": "15 R 5", "correct": True},
            {"id": "optB", "text": "16 R 1", "correct": False},
            {"id": "optC", "text": "14 R 11", "correct": False},
            {"id": "optD", "text": "15 R 0", "correct": False}
        ],
        "answerKey": "optA", "formattedAnswer": "15 R 5 (6 × 15 = 90, 95 - 90 = 5)",
        "hints": [
            "Think of multiples of 6: 6 × 10 = 60; 6 × 15 = 90.",
            "Subtract 90 from 95: 95 - 90 = 5 remaining.",
            "Since 5 is less than 6, 5 is the remainder: 15 R 5."
        ],
        "explanation": "6 × 15 = 90. 95 - 90 = 5 leftover. The quotient is 15 with remainder 5.",
        "misconception": "Leaving remainder larger than divisor or miscalculating 6 × 15"
    },
    {
        "id": "q2_c2_q15", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.6", "format": "numberline",
        "question": "Show 84 ÷ 7 by finding the quotient. How many equal jumps of 7 are needed to reach 84?",
        "nlMin": 0, "nlMax": 20, "step": 1, "answerKey": 12,
        "formattedAnswer": "Quotient = 12 (12 jumps of 7 equal 84)",
        "hints": [
            "Think: 7 × ? = 84.",
            "7 × 10 = 70. 84 - 70 = 14.",
            "7 × 2 = 14. Total jumps = 10 + 2 = 12."
        ],
        "explanation": "84 ÷ 7 = 12. 12 jumps of 7 cover exactly 84 units on the number line.",
        "misconception": "Stopping at 10 jumps (70) or counting error"
    },
    {
        "id": "q2_c2_q16", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "medium",
        "standard": "NC.4.NBT.1", "format": "dragdrop",
        "question": "Classify each place-value statement as TRUE or FALSE.",
        "dragData": {
            "items": [
                {"id": "pv_t1", "text": "70,000 is 10 times greater than 7,000"},
                {"id": "pv_t2", "text": "500 is 10 times greater than 50"},
                {"id": "pv_f1", "text": "3,000 is 10 times greater than 30"},
                {"id": "pv_f2", "text": "40,000 is 100 times greater than 400"}
            ],
            "slots": [
                {"id": "slot_t", "label": "TRUE Statements", "accept": ["pv_t1", "pv_t2", "pv_f2"]},
                {"id": "slot_f", "label": "FALSE Statements", "accept": ["pv_f1"]}
            ]
        },
        "answerKey": {"slot_t": ["pv_t1", "pv_t2", "pv_f2"], "slot_f": ["pv_f1"]},
        "formattedAnswer": "TRUE: 70,000 is 10 × 7,000; 500 is 10 × 50; 40,000 is 100 × 400 | FALSE: 3,000 is 10 × 30 (it is 100 × 30)",
        "hints": [
            "Moving 1 place left multiplies by 10.",
            "Moving 2 places left multiplies by 100.",
            "3,000 has two more zeros than 30, so it is 100 times greater, not 10 times."
        ],
        "explanation": "Shifting 1 column left is × 10; shifting 2 columns left is × 100. 3,000 is 100 times 30, making that statement false.",
        "misconception": "Confusing 10x and 100x place value multipliers"
    },

    # Hard (4 Items)
    {
        "id": "q2_c2_q17", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "hard",
        "standard": "NC.4.OA.3", "format": "mc",
        "question": "A total of 125 fourth-graders are going on a science field trip. Each van can carry up to 8 students. How many vans are needed so that EVERY student has a seat?",
        "options": [
            {"id": "optA", "text": "15 vans (125 ÷ 8 = 15)", "correct": False},
            {"id": "optB", "text": "15 R 5 vans", "correct": False},
            {"id": "optC", "text": "16 vans (round up so 5 students are not left behind)", "correct": True},
            {"id": "optD", "text": "14 vans", "correct": False}
        ],
        "answerKey": "optC", "formattedAnswer": "16 vans (125 ÷ 8 = 15 R 5, must round up to 16)",
        "hints": [
            "Divide 125 by 8: 125 ÷ 8 = 15 with a remainder of 5.",
            "15 vans will carry 15 × 8 = 120 students.",
            "5 students still need a ride! An extra van is required: 15 + 1 = 16 vans."
        ],
        "explanation": "125 ÷ 8 = 15 R 5. In real-world transportation, you cannot leave remaining students behind. You must round up to 16 vans.",
        "misconception": "Remainder truncation: discarding the remainder instead of rounding up in context"
    },
    {
        "id": "q2_c2_q18", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "hard",
        "standard": "NC.4.OA.3", "format": "mc",
        "question": "A school bakery made 144 blueberry muffins. They packed them into boxes of 6 muffins each and sold each box for $8. How much total money did the bakery make?",
        "options": [
            {"id": "optA", "text": "$144 total", "correct": False},
            {"id": "optB", "text": "$192 total", "correct": True},
            {"id": "optC", "text": "$240 total", "correct": False},
            {"id": "optD", "text": "$1,152 total", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "$192 total (144 ÷ 6 = 24 boxes; 24 boxes × $8 = $192)",
        "hints": [
            "Step 1: Find how many boxes were packed (144 ÷ 6).",
            "144 ÷ 6 = 24 boxes.",
            "Step 2: Multiply boxes by cost per box: 24 × $8 = $192."
        ],
        "explanation": "Step 1: 144 muffins ÷ 6 muffins/box = 24 boxes. Step 2: 24 boxes × 8 dollars/box = $192 total.",
        "misconception": "Multiplying total muffins by price directly (144 × 8 = 1,152)"
    },
    {
        "id": "q2_c2_q19", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "hard",
        "standard": "NC.4.NBT.5", "format": "visual",
        "question": "Q3 Readiness Extension: Which 2-digit by 2-digit area model correctly calculates 24 × 13?",
        "visualCards": [
            {"id": "am1", "label": "Model A", "desc": "200 + 60 + 40 + 12 = 312", "svgType": "area_2x2", "sum": 312},
            {"id": "am2", "label": "Model B", "desc": "200 + 12 = 212", "svgType": "area_2x2_err", "sum": 212},
            {"id": "am3", "label": "Model C", "desc": "20 + 6 + 4 + 12 = 42", "svgType": "area_2x2_err", "sum": 42},
            {"id": "am4", "label": "Model D", "desc": "240 + 130 = 370", "svgType": "area_2x2_err", "sum": 370}
        ],
        "answerKey": "am1", "formattedAnswer": "Model A: (20 × 10 = 200) + (20 × 3 = 60) + (4 × 10 = 40) + (4 × 3 = 12) = 312",
        "hints": [
            "Split 24 into 20 + 4, and 13 into 10 + 3.",
            "Calculate all 4 sub-areas: 20 × 10 = 200; 20 × 3 = 60; 4 × 10 = 40; 4 × 3 = 12.",
            "Add all 4 partial products: 200 + 60 + 40 + 12 = 312."
        ],
        "explanation": "24 × 13 decomposed: (20 × 10) + (20 × 3) + (4 × 10) + (4 × 3) = 200 + 60 + 40 + 12 = 312. Model A correctly displays all four partial products.",
        "misconception": "Multiplying only tens with tens and ones with ones (200 + 12 = 212)"
    },
    {
        "id": "q2_c2_q20", "cluster": "c2", "clusterTitle": "Place Value & Operations", "tier": "hard",
        "standard": "NC.4.OA.3", "format": "dragdrop",
        "question": "Classify each word problem card into its mathematical operation category.",
        "dragData": {
            "items": [
                {"id": "wp1", "text": "Emma has 7 pencils. David has 5 times as many pencils."},
                {"id": "wp2", "text": "Emma has 7 pencils. David has 5 more pencils than Emma."},
                {"id": "wp3", "text": "73 eggs are packed into cartons of 6. How many cartons are needed?"}
            ],
            "slots": [
                {"id": "cat_mult_comp", "label": "Multiplicative Comparison", "accept": "wp1"},
                {"id": "cat_add_comp", "label": "Additive Comparison", "accept": "wp2"},
                {"id": "cat_rem_context", "label": "Division with Remainder Rounding", "accept": "wp3"}
            ]
        },
        "answerKey": {"cat_mult_comp": ["wp1"], "cat_add_comp": ["wp2"], "cat_rem_context": ["wp3"]},
        "formattedAnswer": "Multiplicative: 5 times as many (7 × 5) | Additive: 5 more than (7 + 5) | Division with Remainder: 73 ÷ 6 (round up to 13)",
        "hints": [
            "'Times as many' = Multiplicative Comparison.",
            "'More than' = Additive Comparison.",
            "Packing into cartons with leftovers = Division with Remainder."
        ],
        "explanation": "'5 times as many' is multiplicative; '5 more than' is additive; packing 73 items in boxes of 6 requires 73 ÷ 6 = 12 R 1, needing 13 cartons.",
        "misconception": "Confusing additive and multiplicative comparison terminology"
    }
]

CLUSTER3_QUESTIONS = [
    # Easy (6 Items)
    {
        "id": "q2_c3_q01", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.3", "format": "visual",
        "question": "A rectangular garden has a length of 8 feet and a width of 5 feet. How many feet of fencing are needed to go completely around the border?",
        "visualCards": [
            {"id": "perim_26", "label": "Model A", "desc": "Perimeter = 8 + 5 + 8 + 5 = 26 feet", "svgType": "rect_perimeter", "l": 8, "w": 5, "val": 26},
            {"id": "area_40", "label": "Model B", "desc": "Area = 8 × 5 = 40 square feet", "svgType": "rect_area", "l": 8, "w": 5, "val": 40},
            {"id": "half_13", "label": "Model C", "desc": "8 + 5 = 13 feet (Only two sides)", "svgType": "rect_half", "l": 8, "w": 5, "val": 13},
            {"id": "double_80", "label": "Model D", "desc": "40 × 2 = 80 feet", "svgType": "rect_error", "l": 8, "w": 5, "val": 80}
        ],
        "answerKey": "perim_26", "formattedAnswer": "Model A: 26 feet (8 + 5 + 8 + 5 = 26 ft)",
        "hints": [
            "Fencing goes along the outside border, which is PERIMETER.",
            "A rectangle has 4 sides: two lengths (8 ft) and two widths (5 ft).",
            "P = 8 + 5 + 8 + 5 = 26 feet. 40 sq ft is the area, not the fence length!"
        ],
        "explanation": "Perimeter measures the distance around the boundary: P = 2l + 2w = 2(8) + 2(5) = 16 + 10 = 26 feet. Calculating 8 × 5 = 40 gives area in square feet, a classic mistake.",
        "misconception": "Calculating Area (8 × 5 = 40) when Perimeter is requested"
    },
    {
        "id": "q2_c3_q02", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.3", "format": "mc",
        "question": "What is the area of a rectangle with a length of 9 meters and a width of 6 meters?",
        "options": [
            {"id": "optA", "text": "30 meters", "correct": False},
            {"id": "optB", "text": "54 square meters", "correct": True},
            {"id": "optC", "text": "15 square meters", "correct": False},
            {"id": "optD", "text": "108 square meters", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "54 square meters (9 × 6 = 54 m²)",
        "hints": [
            "Formula for Area of a rectangle: Area = length × width.",
            "Multiply 9 meters by 6 meters.",
            "9 × 6 = 54 square meters."
        ],
        "explanation": "Area = length × width = 9 m × 6 m = 54 square meters. 30 meters is the perimeter (2×9 + 2×6 = 30).",
        "misconception": "Confusing area (multiplication) with perimeter (addition)"
    },
    {
        "id": "q2_c3_q03", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.1", "format": "dragdrop",
        "question": "Complete the metric length conversion table (1 kilometer = 1,000 meters).",
        "dragData": {
            "items": [
                {"id": "m_3000", "text": "3,000 m"},
                {"id": "m_5000", "text": "5,000 m"},
                {"id": "m_8000", "text": "8,000 m"}
            ],
            "slots": [
                {"id": "slot_3km", "label": "3 km =", "accept": "m_3000"},
                {"id": "slot_5km", "label": "5 km =", "accept": "m_5000"},
                {"id": "slot_8km", "label": "8 km =", "accept": "m_8000"}
            ]
        },
        "answerKey": {"slot_3km": ["m_3000"], "slot_5km": ["m_5000"], "slot_8km": ["m_8000"]},
        "formattedAnswer": "3 km = 3,000 m, 5 km = 5,000 m, 8 km = 8,000 m",
        "hints": [
            "Kilo means 1,000. 1 km = 1,000 meters.",
            "Multiply kilometers by 1,000.",
            "3 × 1,000 = 3,000; 5 × 1,000 = 5,000; 8 × 1,000 = 8,000."
        ],
        "explanation": "Since 1 km = 1,000 m, multiply each kilometer amount by 1,000: 3 km = 3,000 m, 5 km = 5,000 m, 8 km = 8,000 m.",
        "misconception": "Multiplying by 100 instead of 1,000"
    },
    {
        "id": "q2_c3_q04", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.4", "format": "numberline",
        "question": "A plant seedling measured 3/8 inch. Drag Point P to plot this data point on the fractional line plot.",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.125, "answerKey": 0.375,
        "formattedAnswer": "Coordinate 3/8 (0.375, 3rd tick mark on eighths ruler)",
        "hints": [
            "The line plot is partitioned into eighths: 0/8, 1/8, 2/8, 3/8, 4/8...",
            "Count 3 tick marks from 0.",
            "3/8 = 0.375."
        ],
        "explanation": "3/8 is located at the 3rd tick mark on an eighths scale (0.375).",
        "misconception": "Plotting at 3/4 instead of 3/8"
    },
    {
        "id": "q2_c3_q05", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.1", "format": "mc",
        "question": "A recipe calls for 4 liters of water. How many milliliters of water is this? (1 liter = 1,000 milliliters)",
        "options": [
            {"id": "optA", "text": "400 mL", "correct": False},
            {"id": "optB", "text": "4,000 mL", "correct": True},
            {"id": "optC", "text": "40,000 mL", "correct": False},
            {"id": "optD", "text": "40 mL", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "4,000 mL (4 × 1,000 = 4,000 mL)",
        "hints": [
            "1 liter = 1,000 milliliters.",
            "Multiply liters by 1,000: 4 × 1,000.",
            "4 × 1,000 = 4,000 mL."
        ],
        "explanation": "To convert from a larger unit (liters) to a smaller unit (milliliters), multiply by the conversion factor 1,000: 4 L × 1,000 = 4,000 mL.",
        "misconception": "Multiplying by 100 instead of 1,000 (400 mL)"
    },
    {
        "id": "q2_c3_q06", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "easy",
        "standard": "NC.4.MD.3", "format": "dragdrop",
        "question": "Match each geometric and measurement term to its definition.",
        "dragData": {
            "items": [
                {"id": "term_area", "text": "Area"},
                {"id": "term_perim", "text": "Perimeter"},
                {"id": "term_time", "text": "Elapsed Time"}
            ],
            "slots": [
                {"id": "s_area", "label": "Surface coverage inside a 2D shape (l × w in sq units)", "accept": "term_area"},
                {"id": "s_perim", "label": "Total boundary distance around the outside edge (2l + 2w)", "accept": "term_perim"},
                {"id": "s_time", "label": "Total duration between a start time and end time", "accept": "term_time"}
            ]
        },
        "answerKey": {"s_area": ["term_area"], "s_perim": ["term_perim"], "s_time": ["term_time"]},
        "formattedAnswer": "Area = inside surface coverage; Perimeter = outside boundary length; Elapsed Time = duration between times",
        "hints": [
            "Area is measured in square units inside a shape.",
            "Perimeter is the rim or border outside.",
            "Elapsed time measures how much time has passed."
        ],
        "explanation": "Area measures internal 2D coverage; perimeter measures boundary length; elapsed time measures duration.",
        "misconception": "Confusing area and perimeter definitions"
    },

    # Medium (10 Items)
    {
        "id": "q2_c3_q07", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.3", "format": "visual",
        "question": "An L-shaped room is decomposed into two rectangles: Rectangle A (6 m × 4 m) and Rectangle B (3 m × 2 m). What is the total area of the room?",
        "visualCards": [
            {"id": "l_30", "label": "Model A", "desc": "Area = 24 + 6 = 30 sq meters", "svgType": "rectilinear_l", "a1": 24, "a2": 6, "total": 30},
            {"id": "l_144", "label": "Model B", "desc": "Area = 24 × 6 = 144 sq meters", "svgType": "rectilinear_l", "a1": 24, "a2": 6, "total": 144},
            {"id": "l_20", "label": "Model C", "desc": "Area = 24 - 4 = 20 sq meters", "svgType": "rectilinear_l", "a1": 24, "a2": 6, "total": 20},
            {"id": "l_15", "label": "Model D", "desc": "6 + 4 + 3 + 2 = 15 sq meters", "svgType": "rectilinear_l", "a1": 24, "a2": 6, "total": 15}
        ],
        "answerKey": "l_30", "formattedAnswer": "Model A: 30 sq meters (Area A = 24 m² + Area B = 6 m² = 30 m²)",
        "hints": [
            "Calculate Area of Rectangle A: 6 m × 4 m = 24 sq meters.",
            "Calculate Area of Rectangle B: 3 m × 2 m = 6 sq meters.",
            "Add the non-overlapping sub-areas together: 24 + 6 = 30 sq meters."
        ],
        "explanation": "Total rectilinear area = Area A + Area B = (6 × 4) + (3 × 2) = 24 + 6 = 30 square meters. Never multiply sub-areas together!",
        "misconception": "Multiplying the two sub-areas (24 × 6 = 144) instead of adding"
    },
    {
        "id": "q2_c3_q08", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.3", "format": "mc",
        "question": "A rectangular rug has an area of 48 square feet. Its length is 8 feet. What is the width of the rug?",
        "options": [
            {"id": "optA", "text": "40 feet (48 - 8 = 40)", "correct": False},
            {"id": "optB", "text": "6 feet (48 ÷ 8 = 6)", "correct": True},
            {"id": "optC", "text": "16 feet", "correct": False},
            {"id": "optD", "text": "384 feet (48 × 8 = 384)", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "6 feet (Width = Area ÷ Length = 48 ÷ 8 = 6 ft)",
        "hints": [
            "Area = length × width.",
            "48 = 8 × width.",
            "To find the missing width, divide: 48 ÷ 8 = 6 feet."
        ],
        "explanation": "Since Area = l × w, w = Area ÷ l = 48 ÷ 8 = 6 feet. Checking: 8 ft × 6 ft = 48 sq ft.",
        "misconception": "Subtracting 48 - 8 = 40 instead of dividing"
    },
    {
        "id": "q2_c3_q09", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.4", "format": "numberline",
        "question": "On a line plot of plant heights, the tallest plant is 7/8 inch and the shortest is 2/8 inch. Plot the difference in height (7/8 - 2/8) on the number line.",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.125, "answerKey": 0.625,
        "formattedAnswer": "Coordinate 5/8 (0.625, difference between 7/8 and 2/8)",
        "hints": [
            "Difference means subtraction: 7/8 - 2/8.",
            "Subtract numerators, keep denominator: (7 - 2)/8 = 5/8.",
            "5/8 = 0.625. Move Point P to 5/8."
        ],
        "explanation": "7/8 - 2/8 = 5/8 inch = 0.625. When subtracting like fractions, subtract only the numerators.",
        "misconception": "Subtracting denominators (8 - 8 = 0) leading to 5/0"
    },
    {
        "id": "q2_c3_q10", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.1", "format": "mc",
        "question": "A student's backpack weighs 3 kilograms and 450 grams. What is the total weight of the backpack in grams? (1 kg = 1,000 g)",
        "options": [
            {"id": "optA", "text": "345 grams", "correct": False},
            {"id": "optB", "text": "750 grams", "correct": False},
            {"id": "optC", "text": "3,450 grams", "correct": True},
            {"id": "optD", "text": "30,450 grams", "correct": False}
        ],
        "answerKey": "optC", "formattedAnswer": "3,450 grams (3 × 1,000 g + 450 g = 3,450 g)",
        "hints": [
            "Convert 3 kg into grams: 3 × 1,000 = 3,000 g.",
            "Add the extra grams: 3,000 g + 450 g.",
            "Total = 3,450 grams."
        ],
        "explanation": "3 kg = 3,000 g. Adding 3,000 g + 450 g = 3,450 grams.",
        "misconception": "Treating 1 kg as 100 g (yielding 300 + 450 = 750 g)"
    },
    {
        "id": "q2_c3_q11", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.2", "format": "dragdrop",
        "question": "Soccer practice runs from 10:45 AM to 1:15 PM. Drag the correct timeline interval jumps to calculate the total elapsed time.",
        "dragData": {
            "items": [
                {"id": "j_15m_1", "text": "+15 mins (10:45 -> 11:00 AM)"},
                {"id": "j_2h", "text": "+2 hours (11:00 AM -> 1:00 PM)"},
                {"id": "j_15m_2", "text": "+15 mins (1:00 -> 1:15 PM)"},
                {"id": "err_90m", "text": "90 mins (Base-10 error)"}
            ],
            "slots": [
                {"id": "step1", "label": "Jump 1 (To next hour)", "accept": "j_15m_1"},
                {"id": "step2", "label": "Jump 2 (Hour interval)", "accept": "j_2h"},
                {"id": "step3", "label": "Jump 3 (Final minutes)", "accept": "j_15m_2"}
            ]
        },
        "answerKey": {"step1": ["j_15m_1"], "step2": ["j_2h"], "step3": ["j_15m_2"]},
        "formattedAnswer": "15 mins + 2 hours + 15 mins = 2 hours 30 minutes",
        "hints": [
            "10:45 AM to 11:00 AM is 15 minutes.",
            "11:00 AM to 1:00 PM is 2 full hours.",
            "1:00 PM to 1:15 PM is 15 minutes. Total: 2 hrs + 30 mins."
        ],
        "explanation": "Breaking elapsed time into chunks: 15 min + 2 hr + 15 min = 2 hours 30 minutes. Time is base-60, so standard decimal subtraction fails across hour marks.",
        "misconception": "Base-10 clock subtraction (1:15 - 10:45 = 90 mins or 2.70 hrs)"
    },
    {
        "id": "q2_c3_q12", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.3", "format": "visual",
        "question": "A rectangle has a perimeter of 30 cm and a length of 9 cm. Which model correctly finds the missing width?",
        "visualCards": [
            {"id": "w_6", "label": "Model A", "desc": "Width = 6 cm (9 + 6 + 9 + 6 = 30 cm)", "svgType": "rect_missing_w", "l": 9, "w": 6, "p": 30},
            {"id": "w_21", "label": "Model B", "desc": "Width = 21 cm (30 - 9 = 21)", "svgType": "rect_missing_w_err", "l": 9, "w": 21, "p": 60},
            {"id": "w_12", "label": "Model C", "desc": "Width = 12 cm (30 - 18 = 12, forgot to halve)", "svgType": "rect_missing_w_err", "l": 9, "w": 12, "p": 42},
            {"id": "w_3", "label": "Model D", "desc": "Width = 3 cm", "svgType": "rect_missing_w_err", "l": 9, "w": 3, "p": 24}
        ],
        "answerKey": "w_6", "formattedAnswer": "Model A: Width = 6 cm (Two lengths = 18 cm; Remaining 12 cm ÷ 2 = 6 cm)",
        "hints": [
            "Perimeter = 2 × length + 2 × width.",
            "Two lengths = 9 + 9 = 18 cm.",
            "Remaining perimeter for two widths = 30 - 18 = 12 cm.",
            "Each width = 12 ÷ 2 = 6 cm."
        ],
        "explanation": "P = 2l + 2w. 30 = 2(9) + 2w = 18 + 2w. 2w = 12 -> w = 6 cm. Model A verifies 9 + 6 + 9 + 6 = 30 cm.",
        "misconception": "Subtracting 30 - 9 = 21 or forgetting to divide the remaining perimeter by 2"
    },
    {
        "id": "q2_c3_q13", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.4", "format": "mc",
        "question": "On a fractional line plot, 3 students each grew seedlings that measured 1/4 inch. What is the combined total length of these 3 seedlings?",
        "options": [
            {"id": "optA", "text": "3/12 inch", "correct": False},
            {"id": "optB", "text": "3/4 inch", "correct": True},
            {"id": "optC", "text": "1 whole inch", "correct": False},
            {"id": "optD", "text": "4/3 inch", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "3/4 inch (1/4 + 1/4 + 1/4 = 3 × 1/4 = 3/4 in)",
        "hints": [
            "There are 3 seedlings, each measuring 1/4 inch.",
            "Repeated addition: 1/4 + 1/4 + 1/4 = 3/4.",
            "Or multiplication: 3 × (1/4) = 3/4 inch."
        ],
        "explanation": "3 × 1/4 = 3/4 inch. When multiplying a whole number by a unit fraction, multiply the whole number by the numerator and keep the denominator constant.",
        "misconception": "Multiplying denominator by whole number (3/12)"
    },
    {
        "id": "q2_c3_q14", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.2", "format": "numberline",
        "question": "A movie starts at 2:20 PM and runs for 1 hour and 45 minutes. Drag Point P on the timeline to show what time the movie ends (expressed in minutes after 2:00 PM).",
        "nlMin": 0, "nlMax": 180, "step": 5, "answerKey": 125,
        "formattedAnswer": "4:05 PM (125 minutes after 2:00 PM: 20 min + 105 min = 125 min)",
        "hints": [
            "Start: 2:20 PM.",
            "Add 1 hour: 3:20 PM (80 minutes after 2:00 PM).",
            "Add 40 minutes to reach 4:00 PM (120 minutes after 2:00 PM).",
            "Add remaining 5 minutes to reach 4:05 PM (125 minutes after 2:00 PM)."
        ],
        "explanation": "2:20 PM + 1 hr = 3:20 PM. 3:20 PM + 45 min = 4:05 PM. 4:05 PM is 2 hours and 5 minutes (125 minutes) after 2:00 PM.",
        "misconception": "Adding 20 + 45 = 65 and writing 3:65 PM instead of carrying over 60 minutes to 4:05 PM"
    },
    {
        "id": "q2_c3_q15", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.3", "format": "dragdrop",
        "question": "A compound rectilinear hallway is made of two non-overlapping sections: Hallway 1 is 10 m × 3 m; Hallway 2 is 8 m × 2 m. Drag the partial areas and total area.",
        "dragData": {
            "items": [
                {"id": "a_30", "text": "30 m² (10 × 3)"},
                {"id": "a_16", "text": "16 m² (8 × 2)"},
                {"id": "a_46", "text": "Total = 46 m²"},
                {"id": "a_480", "text": "480 m² (Multiplied)"}
            ],
            "slots": [
                {"id": "s_h1", "label": "Area of Hallway 1", "accept": "a_30"},
                {"id": "s_h2", "label": "Area of Hallway 2", "accept": "a_16"},
                {"id": "s_htot", "label": "Total Combined Floor Area", "accept": "a_46"}
            ]
        },
        "answerKey": {"s_h1": ["a_30"], "s_h2": ["a_16"], "s_htot": ["a_46"]},
        "formattedAnswer": "Hallway 1 = 30 m², Hallway 2 = 16 m², Total = 30 + 16 = 46 m²",
        "hints": [
            "Section 1: 10 × 3 = 30 m².",
            "Section 2: 8 × 2 = 16 m².",
            "Sum = 30 + 16 = 46 m²."
        ],
        "explanation": "Total floor area = (10 × 3) + (8 × 2) = 30 + 16 = 46 square meters.",
        "misconception": "Multiplying the two sub-areas (30 × 16 = 480)"
    },
    {
        "id": "q2_c3_q16", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "medium",
        "standard": "NC.4.MD.1", "format": "mc",
        "question": "A runner ran 4 kilometers on Monday and 2,500 meters on Tuesday. How many total METERS did she run over both days? (1 km = 1,000 m)",
        "options": [
            {"id": "optA", "text": "2,504 meters", "correct": False},
            {"id": "optB", "text": "6,500 meters", "correct": True},
            {"id": "optC", "text": "4,500 meters", "correct": False},
            {"id": "optD", "text": "65,000 meters", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "6,500 meters (4 km = 4,000 m; 4,000 + 2,500 = 6,500 m)",
        "hints": [
            "Convert 4 km to meters: 4 × 1,000 = 4,000 m.",
            "Add Tuesday's meters: 4,000 m + 2,500 m.",
            "Total = 6,500 meters."
        ],
        "explanation": "4 km = 4,000 m. Adding 4,000 m + 2,500 m = 6,500 meters. Adding 4 + 2,500 directly ignores unit conversions.",
        "misconception": "Adding numbers without converting units (4 + 2,500 = 2,504)"
    },

    # Hard (4 Items)
    {
        "id": "q2_c3_q17", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "hard",
        "standard": "NC.4.MD.3", "format": "mc",
        "question": "A rectangular dog pen must have an area of exactly 36 square feet. Which whole-number dimensions give the MINIMUM (smallest) perimeter for the fence?",
        "options": [
            {"id": "optA", "text": "1 ft × 36 ft (Perimeter = 74 ft)", "correct": False},
            {"id": "optB", "text": "2 ft × 18 ft (Perimeter = 40 ft)", "correct": False},
            {"id": "optC", "text": "4 ft × 9 ft (Perimeter = 26 ft)", "correct": False},
            {"id": "optD", "text": "6 ft × 6 ft (Perimeter = 24 ft)", "correct": True}
        ],
        "answerKey": "optD", "formattedAnswer": "6 ft × 6 ft (Perimeter = 24 ft, minimum for 36 sq ft area)",
        "hints": [
            "Find factor pairs of 36: 1×36, 2×18, 3×12, 4×9, 6×6.",
            "Calculate perimeters: P = 2l + 2w.",
            "1×36 -> P = 74; 2×18 -> P = 40; 4×9 -> P = 26; 6×6 -> P = 24.",
            "A square (6×6) gives the smallest perimeter for a fixed area!"
        ],
        "explanation": "For any fixed rectangular area, the shape closest to a square yields the smallest perimeter. 6 ft × 6 ft gives P = 2(6) + 2(6) = 24 ft, which is less than 26, 40, or 74 ft.",
        "misconception": "Assuming longer rectangles require less perimeter"
    },
    {
        "id": "q2_c3_q18", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "hard",
        "standard": "NC.4.MD.2", "format": "mc",
        "question": "Recess started at 11:35 AM and lasted 40 minutes, followed immediately by 30 minutes of lunch. At what time did lunch finish?",
        "options": [
            {"id": "optA", "text": "12:15 PM", "correct": False},
            {"id": "optB", "text": "12:45 PM", "correct": True},
            {"id": "optC", "text": "1:05 PM", "correct": False},
            {"id": "optD", "text": "12:35 PM", "correct": False}
        ],
        "answerKey": "optB", "formattedAnswer": "12:45 PM (Recess ends 12:15 PM; Lunch ends 12:45 PM; Total duration = 70 mins)",
        "hints": [
            "Total time = 40 mins recess + 30 mins lunch = 70 minutes (1 hr 10 mins).",
            "11:35 AM + 25 mins = 12:00 PM (Noon).",
            "Remaining time = 70 - 25 = 45 mins after 12:00 PM = 12:45 PM."
        ],
        "explanation": "Total elapsed time = 40 + 30 = 70 minutes. 11:35 AM + 25 mins = 12:00 PM. 12:00 PM + 45 mins = 12:45 PM.",
        "misconception": "Adding minutes as base-10 decimals or omitting lunch duration"
    },
    {
        "id": "q2_c3_q19", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "hard",
        "standard": "NC.4.MD.4", "format": "numberline",
        "question": "A science class recorded pencil lengths on a line plot: the longest pencil is 7/8 foot and the shortest is 1/8 foot. Plot the range (difference) of pencil lengths.",
        "nlMin": 0.0, "nlMax": 1.0, "step": 0.125, "answerKey": 0.75,
        "formattedAnswer": "Coordinate 6/8 = 3/4 foot (0.75, range between 7/8 and 1/8)",
        "hints": [
            "Range = Maximum - Minimum.",
            "7/8 - 1/8 = 6/8.",
            "6/8 simplifies to 3/4 = 0.75.",
            "Move Point P to 6/8 (0.75)."
        ],
        "explanation": "Range = 7/8 - 1/8 = 6/8 = 3/4 foot = 0.75.",
        "misconception": "Adding 7/8 + 1/8 = 1 whole instead of finding the difference"
    },
    {
        "id": "q2_c3_q20", "cluster": "c3", "clusterTitle": "Area, Perimeter & Data", "tier": "hard",
        "standard": "NC.4.MD.1", "format": "dragdrop",
        "question": "Sort each measurement statement into TRUE or FALSE.",
        "dragData": {
            "items": [
                {"id": "ms_t1", "text": "5 kg is greater than 4,500 g"},
                {"id": "ms_t2", "text": "A 10 m × 4 m rectangle has an area of 40 m²"},
                {"id": "ms_t3", "text": "A 7 cm × 3 cm rectangle has a perimeter of 20 cm"},
                {"id": "ms_f1", "text": "1 hour and 15 minutes is equal to 115 minutes"}
            ],
            "slots": [
                {"id": "box_m_true", "label": "TRUE Statements", "accept": ["ms_t1", "ms_t2", "ms_t3"]},
                {"id": "box_m_false", "label": "FALSE Statements", "accept": ["ms_f1"]}
            ]
        },
        "answerKey": {"box_m_true": ["ms_t1", "ms_t2", "ms_t3"], "box_m_false": ["ms_f1"]},
        "formattedAnswer": "TRUE: 5 kg (5,000 g) > 4,500 g; Area of 10×4 = 40 m²; Perimeter of 7×3 = 2(7)+2(3) = 20 cm | FALSE: 1 hr 15 min = 75 min (not 115 min)",
        "hints": [
            "5 kg = 5,000 g > 4,500 g (True).",
            "Area = 10 × 4 = 40 m² (True).",
            "Perimeter = 7 + 3 + 7 + 3 = 20 cm (True).",
            "1 hour = 60 minutes. 60 + 15 = 75 minutes, NOT 115 minutes (False)."
        ],
        "explanation": "1 hr 15 min = 75 minutes because hours are base-60. Writing 1 hr 15 min = 115 min is a classic base-10 misconception.",
        "misconception": "Treating hours as having 100 minutes (1 hr 15 min = 115 min)"
    }
]

ALL_Q2_QUESTIONS = CLUSTER1_QUESTIONS + CLUSTER2_QUESTIONS + CLUSTER3_QUESTIONS

if __name__ == '__main__':
    print(f"Total Quarter 2 questions: {len(ALL_Q2_QUESTIONS)}")
    print(f"Cluster 1: {len(CLUSTER1_QUESTIONS)}")
    print(f"Cluster 2: {len(CLUSTER2_QUESTIONS)}")
    print(f"Cluster 3: {len(CLUSTER3_QUESTIONS)}")
