from odoo import models, fields, api

class Habitaciones(models.Model):
     _name = 'reserva.habitaciones'

     tipo = fields.Char(string="Tipo Habitacion", required=True)
     numero = fields.Integer(string="Numero Habitacion", required=True)
     cantidad_camas = fields.Integer(string="Cantidad Camas", required=True)
     precio = fields.Float(string="Precio Día", required=True)

class ClienteReserva(models.Model):
     _name = 'reserva.cliente_reserva'

     nombre = fields.Char(string="Cliente", required=True)
     rut = fields.Char(string="Rut", required=True)
     fecha_desde = fields.Date(string="Fecha Reserva", required=True)
     fecha_hasta = fields.Date(string="Fecha Termino", required=True)

     habitacion_id = fields.Many2one('reserva.habitaciones',string="Habitacion")


class Servicio(models.Model):
     _name = 'reserva.servicio'

     servicio =fields.Char(string="Nombre Servicio", required=True)
     capacidad = fields.Integer(string="Capacidad", required=True)
     valor_hora = fields.Float(string="Valor x Hora", required=True)

class ServicioReserva(models.Model):
     _name = 'reserva.servicio_reserva'

     nombre = fields.Char(string="Cliente", required=True)
     empresa =fields.Char(string="Nombre Empresa")
     fecha = fields.Date(string="Fecha Reserva", required=True)
     hora_desde = fields.Datetime(string="Hora Inicio", required=True)
     num_horas = fields.Integer(string="Cantidad Horas", required=True)

