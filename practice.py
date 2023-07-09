from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from PIL import Image

rxn = AllChem.ReactionFromSmarts('CCO>>CC(O)=O',useSmiles=True)
d2d = Draw.MolDraw2DCairo(400,150)
d2d.DrawReaction(rxn)
png = d2d.GetDrawingText()
open('reaction1.png', 'wb+').write(png)