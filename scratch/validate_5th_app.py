import re
import subprocess

html_path = 'apps/math/5th_grade_aig_math_volume_operations_decimals_q1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract script content
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} inline script tag(s)")

for i, s in enumerate(scripts):
    js_filename = f'scratch/temp_app_script_{i}.js'
    with open(js_filename, 'w', encoding='utf-8') as jf:
        jf.write(s)
    res = subprocess.run(['node', '-c', js_filename], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script {i} syntax validation: PASS (node -c exited 0)")
    else:
        print(f"Script {i} syntax validation: FAIL!")
        print(res.stderr)

# Check for LaTeX commands in entire HTML
latex_commands = [r'\frac', r'\cdot', r'\times', r'\leq', r'\geq', r'\pm', r'\sqrt', r'\Delta']
found_latex = [cmd for cmd in latex_commands if cmd in content]
print(f"Raw LaTeX commands found: {found_latex}")

# Check questions count in JSON
matches = re.findall(r'"id":\s*"M[1-3]_T\d+_Q\d+"', content)
print(f"Question IDs embedded in HTML: {len(matches)}")
