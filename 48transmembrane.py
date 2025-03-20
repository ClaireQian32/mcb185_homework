import sys
import mcb185

'''
kd_scale = {
	'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
	'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}
'''

def avg_kd(seq):
	kd_sum = 0
	for aa in seq:
		kd_sum += kd_scale[aa]
	return kd_sum/len(seq)
		
def is_hydrophobic(seq, w, t):
	for i in range(len(seq) - w + 1):
		pep = seq[i:i+w]
		if avg_kd(pep) >= t and 'P' not in pep:
			return True
	return False

file = sys.argv[0]

for name, seq in mcb185.read_fasta(file):
	print(seq)
	if is_hydrophobic(seq[:30], 8, 2.5) and is_hydrophobic(seq[30:], 11, 2.0):
		print(name)