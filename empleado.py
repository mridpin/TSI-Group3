
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
    
    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]    
        res = []
        for empleado in self.browse(cr, uid, ids, context=context):
            name = empleado.idEmpleado
            res.append((empleado.id, name))    
        return res
    
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'persona.code') 
        vals['idEmpleado'] = self.pool.get('ir.sequence').get(cr, uid,'empleado.code')      
        return super(empleado, self).create(cr, uid, vals, context=context)
        
    _columns = {
            'idEmpleado':fields.char('ID Empleado', size=8, readonly=True),
            'isGestorQuejas': fields.boolean('Gestiona Quejas?'),
            'isManager': fields.boolean('Es Manager?'),
            'oficina':fields.char('Oficina', size=64, required=False, readonly=False),
            'eventoqueja':fields.one2many('eventoqueja', 'empleado', 'Eventos Queja'),
        }
empleado()
