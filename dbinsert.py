from ase import io
import ase.db

db = ase.db.connect('structures.db')

images = io.read('test.traj', index=slice(None))

for image in images:
    db.write(image)