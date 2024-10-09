import pandas as pd
import os

def main():
    folder = "/home/bridgersjd/trisicell/scripts_new/partf_scripts/Sep9Matrices/"

    files_raw = [
        "D-no_correction.tsv",
        "D-C19_corrected.tsv",
        "D-C19_and_C2C5_corrected.tsv"
    ]

    files_corrected = [
        "E-no_correction-fp_0.001-fn_0.075.tsv", 
        "E-C19_corrected-fp_0.001-fn_0.075.tsv", 
        "E-C19_and_C2C5_corrected-fp_0.0001-fn_0.075.tsv"
    ]

    folder_trees = "/home/bridgersjd/trisicell/scripts_new/mcmc_scripts/trees/"

    files_trees = [
        "no_correction_newicks_all",
        "C19_corrected_newicks_all",
        "both_corrected_newicks_all"
    ]

    num_samples = 10
    alphas = [0.0001]
    betas = [0.075]
    for i in [0,1,2]:
        path_raw = folder + files_raw[i]
        path_trees = folder_trees + files_trees[i]
        path_corrected = folder + files_corrected[i]

        df_corrected = pd.read_csv(path_corrected, sep="\t", index_col=[0]).sort_values(by=["cell_id_x_mut_id"])

        for mut in df_corrected.columns:
            col = df_corrected[mut]
            clade = sorted([c for c in col.keys() if col[c] == 1])
            cells = "_".join(clade)
            for alpha in alphas:
                for beta in betas:
                    cmd = "sbatch"
                    cmd += ' --job-name="' + 'job_mcmc.' + str(i) + "." + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '"'
                    cmd += ' --output="' + 'job_mcmc.' + str(i) + "." + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '.%j.out"'
                    cmd += ' --error="' + 'job_mcmc.' + str(i) + "." + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '.%j.err"'
                    cmd += ' --export=CELLS="' + cells + '"'
                    cmd += ',MUT="' + mut + '"'
                    cmd += ',ALPHA="' + str(alpha) + '"'
                    cmd += ',BETA="' + str(beta) + '"'
                    cmd += ',INPUT="' + path_raw + '"'
                    cmd += ',TREES="' + path_trees + '"'
                    cmd += ',SAMPLES="' + str(num_samples) + '"'
                    cmd += ' run_mcmc.sbatch'
                    os.system(cmd)
                    print(cmd)

if __name__ == "__main__":
    main()
