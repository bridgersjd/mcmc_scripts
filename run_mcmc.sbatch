#!/bin/bash
 
#SBATCH --mem=2g
#SBATCH --time=5:00:00

CLADE="$CLADE"
MUT="$MUT"
ALPHA="$ALPHA"
BETA="$BETA"
INPUT="$INPUT"
SAMPLES="$SAMPLES"
TREES="$TREES"
 
source myconda
mamba activate partition

python /home/bridgersjd/trisicell/scripts_new/mcmc_scripts/partf_sample_provided.py --num_samples ${SAMPLES} -C "${CELLS}" -m ${MUT} -a ${ALPHA} -b ${BETA} -pe ${INPUT} -pt ${TREES}
