
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
    
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'articulo.code')        
        return super(articulo, self).create(cr, uid, vals, context=context)
    
    def _check_valor(self, cr, uid, ids):
        # No puede ser un valor negatico
        for articulo in self.browse(cr, uid, ids):
            if articulo.valor <= 0:
                return False
        return True
    
    def _check_peso(self, cr, uid, ids):
        # No puede ser un valor negatico
        for articulo in self.browse(cr, uid, ids):
            if articulo.peso <= 0:
                return False
        return True
 
    _columns = {
            'name':fields.char('ID Articulo', size=8, readonly=True),
            'descripcion':fields.char('Descripcion', size=90, required=True, readonly=False),
            'peso':fields.float("Peso",digits=(5,2)),
            'valor':fields.float("Valor", digits=(5, 2)),
            'isComercial': fields.boolean('Es comercial?'),
            'paquetes':fields.many2many('paquete', 'paquete_articulo_rel', 'id_articulo', 'id_paquete','Artículos incluídos', required=True),
            'declaracionAduana':fields.many2one('declaracionaduana', 'Declaracion Aduana'),
        }
    
    _constraints = [(_check_valor, 'VALOR INCORRECTO, el valor no puede ser menor o igual a 0' , [ 'valor' ]),
                    (_check_peso, 'VALOR INCORRECTO, el peso no puede ser menor o igual a 0' , [ 'peso'])] 
articulo()
