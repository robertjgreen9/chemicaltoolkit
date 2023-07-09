from rdkit import Chem
from rdkit.Chem import Draw
import json
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
svg_directory = f"{current_directory}\skeletal-svgs"
png_directory = f"{current_directory}\skeletal-pngs"

def draw_single_molecule_svg(molecule_dict):
    smiles_key = molecule_dict['smiles']
    name_key = molecule_dict['name']
    file_name = f"{name_key}.svg"
    mol = Chem.MolFromSmiles(smiles_key)
    Draw.MolToFile(mol, f"{svg_directory}\{file_name}", imageType="svg")

def main():
    with open("001 Chemistry\smiles.json","r") as f:
        data = json.load(f)
        data = data['substances']

    for substance in data:
        draw_single_molecule_svg(substance)

if __name__ == "__main__":
    main()