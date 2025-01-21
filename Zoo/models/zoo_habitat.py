from odoo import fields, models, api

class ZooHabitat(models.Model):
    _name = 'zoo.habitat'
    _description = 'Hábitat'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    tipo_habitat = fields.Selection([('selva', 'Selva'), ('desierto', 'Desierto'), ('sabana', 'Sabana'), ('montaña', 'Montaña'), ('acuario', 'Acuario')], string='Tipo de hábitat')
    capacidad = fields.Integer(string='Capacidad')
    superficie = fields.Float(string='Superficie')

    # habitat lo relacionaremos con zoo, para poder dividir el zoo en diferentes sectores donde residiran los animales,
    # y para poder identificar el habitat en el que se encuentra el animal