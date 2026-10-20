import sys
sys.path.insert(0, '.')
import scratch.questions_data as qd

data = qd.get_questions_data()
for q in data:
    ans = q.get('answerKey')
    ans_text = ''
    if q['format'] == 'mc':
        for o in q.get('options', []):
            if o.get('correct') or o.get('id') == ans:
                ans_text = f"Option {o['id']}: {o['text']}"
    elif q['format'] == 'visual':
        for c in q.get('visualCards', []):
            if c.get('id') == ans:
                ans_text = f"{c['label']} - {c.get('desc', '')}"
    elif q['format'] == 'numberline':
        ans_text = str(ans)
    elif q['format'] == 'dragdrop':
        ans_text = str(ans)
    print(f"{q['id']} | {q['format']} | {ans_text[:70]}")
