from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html

from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure

import crystal_toolkit.components as ctc

url_base = '/dash_app/'

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    structure = Structure(Lattice.cubic(4.2), ["Na", "K"], [[0, 0, 0], [0.5, 0.5, 0.5]])

    structure_component = ctc.StructureMoleculeComponent(structure, id="hello_structure")

    app.layout = html.Div([structure_component.layout()])
    return app.server