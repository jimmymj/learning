import sys
sys.path.insert(0, '.')
import scratch.questions_data as qd

data = qd.get_questions_data()
for q in data:
    print(f"{q['id']} | {q['format']} | {repr(q.get('answerKey'))[:60]}")
