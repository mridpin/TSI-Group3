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
    
    # Tarifa base para un articulo de 1 litro x 1 kilo
    TARIFA_BASE = 2.0
    # Incremento por estar asegurado
    INCREMENTO_SEGURO = 0.10
    # Incremento por envio urgente
    INCREMENTO_URGENTE = 0.20
    # Incremento por envio internacional
    INCREMENTO_INTERNACIONAL = 0.25
    # Incremento por ser publico (en este caso es un descuento)
    INCREMENTO_ADMIN_PUBLICA = -0.25
    
    _name = 'paquete'
    _description = 'Paquete con el que trabaja la empresa'
    
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid,'paquete.code')        
        return super(paquete, self).create(cr, uid, vals, context=context)
 
    def eliminarArticulos(self,cr,uid,ids,context=None):
        res = self.write(cr,uid,ids,{'articulos':[ (5, ) ]}, context=None)        
        return res
    
    def _get_valor (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for paquete in self.browse(cr, uid, ids):
            valor = sum([articulo.valor for articulo in paquete.articulos])
            res[paquete.id] = valor
        return res
    
    def _get_peso (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for paquete in self.browse(cr, uid, ids):
            peso = sum([articulo.peso for articulo in paquete.articulos])
            res[paquete.id] = peso
        return res
    
    def _calcular_tarifa (self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for paquete in self.browse(cr, uid, ids):
            # calculamos la media entre peso y volumen
            tarifa = (paquete.dimension + paquete.peso) / 2
            tarifa *= self.TARIFA_BASE
            # Sumamos todos los incrementos
            incrementoTotal = 0.0
            if paquete.isUrgente == True:
                incrementoTotal += self.INCREMENTO_URGENTE
            if paquete.isInternacional == True:
                incrementoTotal += self.INCREMENTO_INTERNACIONAL  
            if paquete.isAsegurado == True:
                incrementoTotal += self.INCREMENTO_SEGURO
            if paquete.isAdminPublica == True:
                incrementoTotal += self.INCREMENTO_ADMIN_PUBLICA
            #Aplicamos el incremento total a la tarifa base
            tarifa += tarifa * incrementoTotal
            res[paquete.id] = tarifa                
        return res
    
    _columns = {
            #Aclaración: id_paquete es un campo autonumérico. Se ha definido como char de manera temporal.
            'name':fields.char('ID Paquete', size=8, readonly=True),
            'tarifa':fields.function(_calcular_tarifa, 
                                    type='float',
                                    method=True,
                                    store=True,
                                    string='Tarifa'),
            'fechaEntrega':fields.datetime('Fecha de entrega', autodate=True),
            'remitente':fields.many2one('cliente', 'Remitente', required=True),
            'destinatario':fields.many2one('cliente', 'Destinatario', required=True),
            'isUrgente':fields.boolean('Urgente'),
            'isAdminPublica':fields.boolean('Administración pública'),
            'isInternacional':fields.boolean('Internacional'),
            'dimension':fields.integer('Volumen', readonly=False),
            'peso':fields.function(_get_peso, 
                                    type='float',
                                    method=True,
                                    store=True,
                                    string='Peso'),
            'valor':fields.function(_get_valor, 
                                    type='float',
                                    method=True,
                                    store=True,
                                    string='Valor'),
            'state':fields.selection([
            ('iniciado','Iniciado'),
            ('aceptado','Aceptado'),
            ('enviado','Enviado'),
            ('cancelado','Cancelado'),
            ('devuelto','Devuelto al Remitente'),
            ('entregado','Entregado'),
             ],    'Estado', select=True, readonly=True),
            'isAsegurado':fields.boolean('Asegurado'),
            'articulos':fields.many2many('articulo', 'paquete_articulo_rel', 'id_paquete', 'id_articulo', 'Artículos incluídos', required=True),
            'quejas':fields.many2one('queja', 'Quejas'),
        }
     
    _sql_constraints = [('dimension_minima', 'CHECK(dimension>0)', 'VALOR INCORRECTO, la dimension no puede ser menor o igual a 0')]
    
    _defaults =  {'state':'iniciado', }
    
paquete()
