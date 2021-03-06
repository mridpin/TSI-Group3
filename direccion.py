
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

class direccion(osv.Model):

    _name = 'direccion'
    _description = 'Direccion de los clientes'
 
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'direccion.code')        
        return super(direccion, self).create(cr, uid, vals, context=context)
 
    _columns = {
            'name':fields.char('ID', size=8, readonly=True),
            'calle':fields.char('Calle', size=64, required=True, readonly=False),
            'codigoPostal':fields.char('Codigo Postal', size=64, required=True, readonly=False),
            'pais': fields.many2one('res.country', 'Pais'),
            'cliente_id':fields.many2one('cliente','Cliente'),
        }
direccion()