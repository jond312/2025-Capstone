import pandas as pd

HGSVC_file = "HGSVC2_sample_list.txt"
HPRC_file = "HPRC_PacBio_HiFi.sample.index.csv.1"
ONEKG_file = "20130606_sample_info.txt"

onekg = pd.read_csv(ONEKG_file, sep='\t')
onekg_samples = set(onekg['Sample'])

hgsvc = pd.read_csv(HGSVC_file, sep='\t', header=None, names=["sra", "sample", "population"])
hgsvc_samples = set(hgsvc['sample'])

hprc = pd.read_csv(HPRC_file)
hprc_samples = set(hprc['sample_ID'].astype(str).str.strip())

common_hgsvc = sorted(onekg_samples.intersection(hgsvc_samples))
common_hprc = sorted(onekg_samples.intersection(hprc_samples))

with open("overlap_1KG_HGSVC.txt", "w") as f:
        f.write("\n".join(common_hgsvc))

with open("overlap_1KG_HPRC.txt", "w") as f:
        f.write("\n".join(common_hprc))

print(f"Found {len(common_hgsvc)} overlapping samples with HGSVC")
print(f"Found {len(common_hprc)} overlapping samples with HPRC")
