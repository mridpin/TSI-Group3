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

class queja(osv.Model):

    _name = 'queja'
    _description = 'queja'
 
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'queja.code')        
        return super(queja, self).create(cr, uid, vals, context=context)
    
    def on_change_checkDate(self, cr, uid, vals, start,end,context=None):
        warning={'title':'Fecha Incorrecto',
                  'message':'La fecha final no puede ser anterior a la fecha de inicio'}
        
        if end < start:
            return {'value':{'end': None }, 'warning':warning}
        else:
            return {}
    
    _columns = {
            'name':fields.char('ID Queja', size=8, readonly=True),
            'descripcion':fields.text('Descripción'),
            'start':fields.date('Fecha Inicio'),
            'end':fields.date('Fecha Resolucion'),
            'cliente':fields.many2one('cliente', 'Cliente', required=True),
            'paquete':fields.many2one('paquete', 'Paquete', required=True),
            'state':fields.selection([
            ('iniciado','Iniciada'),
            ('abierta','Abierta'),
            ('resuelta','Resuelta'),
             ],    'Estado', select=True, readonly=True),
            'eventosqueja':fields.one2many('eventoqueja', 'queja', 'Eventos Queja'),            
        }
    
    _defaults =  {'state':'iniciado', }
queja()