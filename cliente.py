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

class cliente(osv.Model):
    
    _name = 'cliente'
    _description = 'Cliente de un paquete'
    _inherit = "persona"
    
    # Funcion que se ejecuta al pulsar el boton de recalcular. 
    # Aunque parezca que los va a poner a 0, lo que hace es llamar a la función _calcular_puntos para recalcularlos
    def calcular_puntos_button(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'puntos':'0'})
    
    # Funcion que calcula los puntos de los clientes
    def _calcular_puntos (self, cr, uid, ids, field, arg, context=None):
        res = {}
        for cliente in self.browse(cr, uid, ids):
            puntos = sum([paquete.tarifa for paquete in cliente.paquetes_enviados])
            res[cliente.id] = puntos / 10
        return res
 
    _columns = {
            'email':fields.char('Email', size=64, required=True, readonly=False),
            'direccion_ids': fields.one2many('direccion','cliente_id','Direcciones'),
            'telefono':fields.char('Telefono', size=20, required=True, readonly=False),
            'puntos':fields.function(_calcular_puntos,
                                    type='float',
                                    method=True,
                                    store=True,
                                    string='Puntos'),
            'paquetes_enviados':fields.one2many('paquete', 'remitente', 'Paquetes Enviados'),
            'paquetes_recebidos':fields.one2many('paquete', 'destinatario', 'Paquetes Recibidos'),
            'quejas':fields.one2many('queja', 'cliente', 'Quejas'),
        }
cliente()
