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

class paquete(osv.Model):

    _name = 'paquete'
    _description = 'Paquete con el que trabaja la empresa'
 
    _columns = {
            #Aclaración: id_paquete es un campo autonumérico. Se ha definido como char de manera temporal.
            'name':fields.char('ID Paquete', size=64, required=True, readonly=False),
            #Aclaración: tarifa es un campo funcional, calculado a partir de otros parámetros. Se ha como float de manera temporal.
            'tarifa':fields.float('Tarifa', readonly=True),
            'fechaEntrega':fields.datetime('Fecha de entrega', autodate=True),
            'remitente':fields.many2one('cliente', 'Remitente', required=True),
            'destinatario':fields.many2one('cliente', 'Destinatario', required=True),
            'isUrgente':fields.boolean('Urgente'),
            #Aclaración: tarifa es un campo funcional, calculado a partir de la fecha de entrega. Se ha como booleano de manera temporal.
            'isEntregado':fields.boolean('Entregado', readonly=True),
            'isAdminPublica':fields.boolean('Administración pública'),
            'isInternacional':fields.boolean('Internacional'),
            'dimension':fields.integer('Volumen', readonly=False),
            'peso':fields.integer('Peso', readonly=True),
            #Aclaración: valor es un campo funcional, calculado a partir de los artículos. Se ha como integer de manera temporal.
            'valor':fields.integer('Valor', readonly=True),
            'isAsegurado':fields.boolean('Asegurado'),
            'articulos':fields.many2many('articulo', 'paquete_articulo_rel', 'id_paquete', 'id_articulo', 'Artículos incluídos', required=True),
            'quejas':fields.many2one('queja', 'Quejas'),
        }
paquete()
