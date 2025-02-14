from odoo import fields, models, api

class ZooHabitat(models.Model):
    _name = 'zoo.habitat'
    _description = 'Hábitat'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    tipo_habitat = fields.Selection(
        [('selva', 'Selva'), 
         ('desierto', 'Desierto'), 
         ('sabana', 'Sabana'), 
         ('montaña', 'Montaña'), 
         ('acuario', 'Acuario')], string='Tipo de hábitat')
    capacidad = fields.Integer(string='Capacidad')
    superficie = fields.Float(string='Superficie')
    temperatura = fields.Float(string='Temperatura')
    humedad = fields.Float(string='Humedad')
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    animal_ids = fields.One2many('zoo.animal', 'habitat_id', string='Animales')

    cantidad_actual_animales = fields.Integer(string='Cantidad Actual de Animales', compute='_compute_cantidad_actual_animales', store=True)
    is_full = fields.Boolean(string='Está lleno', compute='_compute_is_full', store=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre del hábitat debe ser unico!'),
        ('zoo_habitat_uniq', 'unique(zoo_id, name)', 'El hábitat ya está registrado en otro zoo!')
    ]

    @api.depends('animal_ids')
    def _compute_cantidad_actual_animales(self):
        for habitat in self:
            habitat.cantidad_actual_animales = len(habitat.animal_ids)

    @api.depends('cantidad_actual_animales', 'capacidad')
    def _compute_is_full(self):
        for habitat in self:
            habitat.is_full = habitat.cantidad_actual_animales >= habitat.capacidad