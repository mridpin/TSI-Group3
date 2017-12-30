
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################


{
    "name": "Paqueteria Express",
    "version": "1.1",
    "depends": ["base"],
    "author": "Victor Martinelli, Manuel Ridao Pineda, Stefano Marzo",
    "category": "paqueteria",
    "description": """
    Aplicacion para una empresa de paqueteria express
    """,
    "init_xml": [],
    'data' : ['persona_view.xml','articulo_view.xml', 'paquete_view.xml', 'cliente_view.xml','empleado_view.xml','direccion_view.xml','queja_view.xml','eventoqueja_view.xml','workflow/paquete_workflow.xml','workflow/queja_workflow.xml'],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}