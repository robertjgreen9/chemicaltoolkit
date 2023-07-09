import pubchempy as pcp
import json

smile_json = "001 Chemistry\smiles.json"

def get_smiles(name):
    compound = pcp.get_compounds(name, 'name')[0]
    smiles = compound.isomeric_smiles
    x = {"name": name, "smiles": smiles}
    return x

def load_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def write_to_json(data, x, file):
    data.append(x)
    with open(file, 'w') as f:
        json.dump(data, f, indent = 2)
    return data

def iterate_json(prefix, suffix):
    for substance in prefix:
        substance = f"{substance}{suffix}"
        smile = get_smiles(substance)
        write_to_json(data, smile, smile_json)

alkanes = ["prop", "but", "pent", "hex", "hept", "oct"]

data = load_json(smile_json)

def main(file, suffix):
    data = load_json(file)
    iterate_json(data, suffix)

main(smile_json, "")