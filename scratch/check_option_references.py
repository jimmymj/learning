import sys
sys.path.insert(0, '.')
import scratch.questions_data as qd

data = qd.get_questions_data()
for q in data:
    for h in q.get('hints', []):
        if any(w in h.lower() for w in ['option a', 'option b', 'option c', 'option d', 'model a', 'model b', 'model c', 'model d']):
            print(f"{q['id']} hint: {h}")
    for step, text in q.get('explanation', {}).items():
        if any(w in text.lower() for w in ['option a', 'option b', 'option c', 'option d', 'model a', 'model b', 'model c', 'model d']):
            print(f"{q['id']} exp {step}: {text}")
