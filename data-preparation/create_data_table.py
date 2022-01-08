import os, glob, json
import pandas as pd

def convert_brainstem_stats_to_dict(brainstemFile):
    stats = {}
    with open(brainstemFile, "r") as f:
        for line in f.readlines():
            row = line.split()
            stats[row[0]] = row[1]
    return stats

def create_brainstem_stats(brainstemFile):
    stats = convert_brainstem_stats_to_dict(brainstemFile)
    with open("brainstem.csv", "w") as f:
        keys = list(stats.keys())
        for key in keys[:-1]:
            f.write(f"{key}\t")
        f.write(f"{keys[-1]}\n")

        for key in keys[:-1]:
            f.write(f"{stats[key]}\t")
        f.write(f"{stats[keys[-1]]}")

def convert_stats_to_csv(statsFile: str, outputCsvFile: str):
    '''
    Converts the aseg.stats file produced from recon-all to a CSV file
    '''
    os.system(f"singularity exec freesurfer-freesurfer-7.1.1.simg asegstats2table -i {statsFile} --meas volume --tablefile {outputCsvFile}")

def create_csv(subjectDirectory, subIdDict):
    # Convert stats to CSV
    convert_stats_to_csv(f"{subjectDirectory}/aseg.stats", "stats.csv")
    stats_df = pd.read_csv("stats.csv", sep="\t")

    # Convert brainstem stats to CSV
    create_brainstem_stats(f"{subjectDirectory}/brainstemSsVolumes.v10.txt")
    brainstem_df = pd.read_csv("brainstem.csv", sep="\t")

    # Create DF
    df = stats_df.join(brainstem_df)

    # Convert CSV to DF and add subject ID column
    subject = subjectDirectory.split("/")[2]
    subjectId = subIdDict[subject]
    df.insert(0, column="subjectId", value=[subjectId])

    # Remove temp files
    os.system(f"rm stats.csv")
    os.system(f"rm brainstem.csv")

    return df

if __name__ == '__main__':
    df_list = []
    with open("data/subId.json") as f:
        subIdDict = json.load(f)

    for subjectDirectory in glob.glob("data/fsstats/*"):
        print(subjectDirectory)
        df = create_csv(subjectDirectory, subIdDict)
        df_list.append(df)

    final_df = pd.concat(df_list, ignore_index=True)
    final_df.to_csv("volumes.csv")