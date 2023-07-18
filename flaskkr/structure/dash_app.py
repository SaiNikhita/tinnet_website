from dash import Dash, dcc, html, callback
from dash.dependencies import Input, State, Output
from dash.exceptions import PreventUpdate

from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor

import crystal_toolkit.components as ctc
import ase.db
from ase.symbols import Symbols

url_base = '/dash_app/'
options = []

def configDB():
    return ase.db.connect('structures.db')

def buildSearchComponent():
    return html.Div([
        dcc.Dropdown(id="search")
    ])

def buildTableComponent():
    return html.Div()

def buildDashboardComponent():
    tableComponent = buildTableComponent()
    structure = Structure(Lattice.cubic(4.2), ["Na", "K"], [[0, 0, 0], [0.5, 0.5, 0.5]])
    structureComponent = html.Div(children=[ctc.StructureMoleculeComponent(structure, id="structure").layout()], id="viz")
    return html.Div(children=[tableComponent, structureComponent], id="dashboard")

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    global db
    db = configDB()
    for row in db.select():
        option = {}
        option['label'] = row.toatoms().get_chemical_formula()
        option['value'] = row.toatoms().get_chemical_formula()
        options.append(option)

    search_component = buildSearchComponent()
    dashboard_component = buildDashboardComponent()

    app.layout = html.Div(children=[search_component, dashboard_component])
    return app.server

@callback(
    Output("search", "options"),
    Input("search", "search_value")
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]

@callback(
    Output('viz', 'children'),
    Input('search', 'value')
)
def update_output(value):
    if not value:
        raise PreventUpdate
    ans = db.get_atoms('formula=' + value)
    structure = AseAtomsAdaptor.get_structure(ans)
    return ctc.StructureMoleculeComponent(structure, id="structure").layout()