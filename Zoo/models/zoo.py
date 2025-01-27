from odoo import fields, models, api

class Zoo(models.Model):
    _name = 'zoo.zoo'
    _description = 'Zoo'

    name = fields.Char(string='Name', required=True)
    extension = fields.Integer(string='Extensión', required=True)
    pais_id = fields.Many2one('res.country', string='País')
    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    ciudad = fields.Char(string='Ciudad')
    codigo_postal = fields.Char(string='Código Postal')
    cantidad_animales = fields.Integer(string='Cantidad de Animales', compute='_compute_cantidad_animales', store=True)
    zoo_animal_ids = fields.One2many('zoo.animal', 'zoo_id', string='Animales')
    zoo_habitat_ids = fields.One2many('zoo.habitat', 'zoo_id', string='Hábitats')

    # Zoo estara relacionado con animal, donde obtendra el total de animales ademas de sus datos
    # Tambien estara relacionado con habitat para poder dividir el zoo en diferentes sectores
    # añadir tags, por ejemplo, eventos que hace el zoo como restaurantes, espectaculos, etc.
    # añadir un campo imagen para la imagen del zoo
    # una barra de estado donde indique la cantidad de animales, la cantidad de animales peligrosos o en peligro de extincion
        
    @api.depends('zoo_animal_ids')
    def _compute_cantidad_animales(self):
        for zoo in self:
            zoo.cantidad_animales = len(zoo.zoo_animal_ids)
    
    @api.constrains('cantidad_animales')
    def _check_cantidad_animales(self):
        if self.cantidad_animales < 0:
            raise models.ValidationError('La cantidad de animales no puede ser negativa!')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre del Zoo debe ser unico!'),
        ('extension', 'CHECK(extension > 0)', 'La extension debe ser mayor a 0!'),
    ]