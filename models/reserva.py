from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Habitaciones(models.Model):
    _name = 'reserva.habitaciones'

    name = fields.Integer(string="Numero Habitacion", required=True)
    tipo = fields.Selection(
        [('1', 'Simple'), ('2', 'Doble'), ('3', 'Triple'), ('4', 'Cuadruple')], default='1')
    descripcion = fields.Text(string="Descripcion Habitacion")
    precio = fields.Float(string="Valor Día", required=True)
    clientereserva_ids = fields.One2many(
        'reserva.cliente_reserva', 'habitacion_id', string="Reservas")


class ClienteReserva(models.Model):
    _name = 'reserva.cliente_reserva'

    name = fields.Char(string="Cliente", required=True)
    rut = fields.Char(string="Rut", required=True)
    fecha_desde = fields.Date(string="Fecha Reserva", required=True)
    fecha_hasta = fields.Date(string="Fecha Termino", required=True)

    habitacion_id = fields.Many2one(
        'reserva.habitaciones', string="Habitacion")

#    @api.onchange('habitacion_id', 'fecha_desde', 'fecha_hasta')
#    def valida_reserva(self):
#        if self.habitacion_id and self.fecha_desde and self.fecha_hasta:
#            for reg in self:
#                if reg.habitacion_id == self.habitacion_id:
#                     if reg.fecha_desde <= self.fecha_desde <= reg.fecha_hasta:
#                       raise ValidationError(
#                        'Habitacion Ocupada en las fechas seleccionadas, Verifique')
#                     elif reg.fecha_desde <= self.fecha_hasta <= reg.fecha_hasta:
#                        raise ValidationError(
#                                'Habitacion Ocupada en las fechas seleccionadas, Verifique')
#       return {}
#


class Servicio(models.Model):
    _name = 'reserva.servicio'

    name = fields.Char(string="Nombre Servicio", required=True)
    capacidad = fields.Integer(string="Capacidad", required=True)
    valor_hora = fields.Float(string="Valor x Hora", required=True)
    servicio_reservas_ids = fields.One2many(
        'reserva.servicio_reserva', 'servicio_id', string='Reservas')


class ServicioReserva(models.Model):
    _name = 'reserva.servicio_reserva'

    name = fields.Char(string="Cliente", required=True)
    observacion = fields.Char(string="Observaciones")
    fecha = fields.Date(string="Fecha Reserva", required=True)
    hora_desde = fields.Selection(
        [('8', '08:00'), ('9', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00')], default='8')
    num_horas = fields.Integer(string="Cantidad Horas", required=True)

    servicio_id = fields.Many2one('reserva.servicio', string="Servicio")
