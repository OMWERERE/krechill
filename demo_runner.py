import sys
sys.path.append(r'C:\Users\joels\Projects\kira-agriculture\shared')
from kira_bioelectric_generator import generate_bioelectric_scenario
from krechill import ColdVeritas

csv, x, y = generate_bioelectric_scenario(scenario='depolarization')
cv = ColdVeritas(csv, sampling_hz=100)
cv.cell_x = x
cv.cell_y = y

print("Viability score:", cv.cold_chain_viability())
print("Hardening score:", cv.cold_hardening_priming())
