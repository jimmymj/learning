import sys
sys.path.insert(0, '.')
from scratch.q1_5th_aig_questions import ALL_Q1_5TH_AIG_QUESTIONS

errors = []
latex_markers = ['$', '\\frac', '\\times', '\\cdot', '\\le', '\\ge', '\\sqrt', '\\pm']

for i, q in enumerate(ALL_Q1_5TH_AIG_QUESTIONS):
    # Check options count
    if len(q['options']) != 4:
        errors.append(f"Q{i+1} ({q['id']}): options length is {len(q['options'])}")
    
    # Check correctIndex matches formattedAnswer
    correct_opt = q['options'][q['correctIndex']]
    if correct_opt != q['formattedAnswer']:
        errors.append(f"Q{i+1} ({q['id']}): correctIndex ({q['correctIndex']}) gives '{correct_opt}' but formattedAnswer is '{q['formattedAnswer']}'")
    
    # Check options are unique
    if len(set(q['options'])) != 4:
        errors.append(f"Q{i+1} ({q['id']}): duplicate options found in {q['options']}")
        
    # Check for latex markers
    diag = q.get('diagnostic', {})
    full_text = q['question'] + ' ' + ' '.join(q['options']) + ' ' + ' '.join(q.get('socraticHints', [])) + ' ' + diag.get('stepByStep', '')
    for m in latex_markers:
        if m in full_text:
            errors.append(f"Q{i+1} ({q['id']}): found LaTeX marker '{m}'")

print(f"Total questions: {len(ALL_Q1_5TH_AIG_QUESTIONS)}")
if errors:
    print(f"Found {len(errors)} issues:")
    for e in errors:
        print("  -", e)
else:
    print("SUCCESS: All 60 questions passed syntax, answer matching, and zero-LaTeX validation!")
