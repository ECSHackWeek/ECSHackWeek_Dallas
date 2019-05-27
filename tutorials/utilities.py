import os
import pandas as pd

def build_dataset():
    full_df = pd.DataFrame(columns=["frequencies", "z_real", "z_imag", "test", "chem", "cell", "temp"])

    directory = "./data/eis/"
    filenames = os.listdir(directory)
    for filename in filenames:
        if 'NCA' not in filename and 'Pristine' not in filename and '_1_' not in filename:
            data = pd.read_csv(directory + filename, skiprows=123, delimiter="\t", header=None, 
                               usecols=[0,4,5], names=["frequencies", "z_real", "z_imag"])

            mask = data["z_imag"] < 0
            data = data[mask]

            data['z_imag'] = -1*data['z_imag']

            data["test"] = filename
            data["chem"] = filename.split("_")[0]
            data["cell"] = filename.split("_")[1]
            data["temp"] = try_convert_float(filename.split("_")[-1].split(".")[0].split("C")[0])

            full_df = full_df.append(data)
        
    return full_df


def try_convert_float(a):
    try:
        return float(a)
    except ValueError:
        return a
    
    
def get_ranges(data, y_scale=1):
    range_x = max(data['z_real']) - min(data['z_real'])
    range_y = max(data['z_imag']) - min(data['z_imag'])

    rng = max(range_x, range_y)

    min_x = min(data['z_real'])
    max_x = min(data['z_real']) + rng
    min_y = min(data['z_imag'])
    max_y = min(data['z_imag']) + rng/y_scale
    
    return min_x, max_x, min_y, max_y