
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

class declaracionaduana(osv.Model):
    
    _name = 'declaracionaduana'
    _description = 'Declaracion de aduana de un articluo'
 
    _columns = {
            'declaracionAduana':fields.char('Declaracion aduana', size=128, required=True, readonly=False),
            'tasaAduana':fields.integer('Tasa aduana %', required=True, size=2),
            'articulo':fields.many2one('articulo', 'Articulo', required=True),
        }
declaracionaduana()