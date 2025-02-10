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
    cantidad_animales_en_peligro = fields.Integer(string='Cantidad de Animales en Peligro', compute='_compute_cantidad_animales_en_peligro', store=True)
    zoo_animal_ids = fields.One2many('zoo.animal', 'zoo_id', string='Animales')
    zoo_habitat_ids = fields.One2many('zoo.habitat', 'zoo_id', string='Hábitats')
    tag_ids = fields.Many2many('zoo.tags', 'tag_id', string='Tags')
    imagen = fields.Binary()
     
    @api.depends('zoo_animal_ids')
    def _compute_cantidad_animales(self):
        for zoo in self:
            zoo.cantidad_animales = len(zoo.zoo_animal_ids)
    
    @api.depends('zoo_animal_ids.especie')
    def _compute_cantidad_animales_en_peligro(self):
        for zoo in self:
            zoo.cantidad_animales_en_peligro = len(
                zoo.zoo_animal_ids.filtered(lambda a: a.especie.en_peligro)
            )

    @api.constrains('cantidad_animales')
    def _check_cantidad_animales(self):
        if self.cantidad_animales < 0:
            raise models.ValidationError('La cantidad de animales no puede ser negativa!')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre del Zoo debe ser unico!'),
        ('extension', 'CHECK(extension > 0)', 'La extension debe ser mayor a 0!'),
    ]