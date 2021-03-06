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
from empleado import empleado

class eventoqueja(osv.Model):

    _name = 'eventoqueja'
    _description = 'Evento de una queja'
 
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'eventoqueja.code')        
        return super(eventoqueja, self).create(cr, uid, vals, context=context) 
    
    def on_change_isQueja(self,cr,uid,ids,emp,context=None):
        warning={'title':'Empleado Incorrecto',
                  'message':'El empleado debe ser gestor de quejas'}
        
        empleado = self.pool.get('empleado')
        empleado_data = empleado.browse(cr, uid, emp, context=context)
        
        if empleado_data.isGestorQuejas!=True:
            return {'value':{'empleado': False }, 'warning':warning}
        else:
            return {}
 
    _columns = {
            'name':fields.char('ID Evento', size=8, readonly=True),
            'mensaje':fields.text('Mensaje'),
            'queja':fields.many2one('queja', 'ID Queja', required=True),
            'empleado':fields.many2one('empleado', 'ID Empleado', required=True),
        }
eventoqueja()