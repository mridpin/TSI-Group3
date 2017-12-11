
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

from osv import osv
from osv import fields

class articulo(osv.Model):
    
    _name = 'articulo'
    _description = 'Articulo de un paquete'
 
    _columns = {
            'name':fields.char('ID Articulo', size=64, required=True, readonly=False),
            'descripcion':fields.char('Descripcion', size=90, required=True, readonly=False),
            'peso':fields.float("Peso",digits=(5,2)),
            'valor':fields.float("Valor",digits=(5,2)),
            'isComercial': fields.boolean('Es comercial?'),
            'paquetes':fields.many2many('paquete', 'paquete_articulo_rel', 'id_articulo', 'id_paquete','Artículos incluídos', required=True),
        }
articulo()