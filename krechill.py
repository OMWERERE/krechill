import sys
sys.path.append(r'C:\Users\joels\Projects\kira-agriculture\shared')
from veritas_bioelectric_adapter import BioelectricVeritas
import numpy as np

class ColdVeritas(BioelectricVeritas):
    def cold_chain_viability(self):
        wnci = self.run_wnci_on_each_node()
        H = self.compute_spatial_entropy()
        viability = np.mean(wnci) * (1 - np.mean(H) / 4.0)
        return max(0, min(1, viability))
    
    def cold_hardening_priming(self):
        vmem_mean = np.mean(self.vmem, axis=1)
        grad = self.compute_spatial_gradient(self.cell_x, self.cell_y)
        score = (vmem_mean[-1] + 120) / 80
        score *= 1 - grad.mean() / 1e6
        return np.clip(score, 0, 1)

if __name__ == "__main__":
    print("krechill module ready.")
