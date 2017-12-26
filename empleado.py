
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

class empleado(osv.Model):

    _name = 'empleado'
    _description = 'Empleado de la empresa'
    _inherit = "persona"
    
    _columns = {
            'idEmpleado':fields.char('ID Empleado', size=64, required=False, readonly=False),
            'isGestorQuejas': fields.boolean('Gestiona Quejas?'),
            'isManager': fields.boolean('Es Manager?'),
            'oficina':fields.char('Oficina', size=64, required=False, readonly=False),
            'eventoqueja':fields.one2many('eventoqueja', 'empleado', 'Eventos Queja'),
        }
empleado()
