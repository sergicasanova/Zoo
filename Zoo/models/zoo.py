from odoo import fields, models, api

class Zoo(models.Model):
    _name = 'zoo.zoo'
    _description = 'Zoo'

    name = fields.Char(string='Name', required=True)
    id_zoo = fields.Integer(string='ID', required=True)
    grandaria = fields.Integer(string='Grandaria', required=True)
    pais_id = fields.Many2one('res.country', string='País')
    ciudad_id = fields.Many2one('res.city', string='Ciudad')
    codigo_postal = fields.Char(string='Código Postal')
    # Este campo lo relacionaremos con animales para obtener el total de animales
    cantidad_animales = fields.Integer(string='Cantidad de Animales', required=True)

    # Zoo estara relacionado con animal, donde obtendra el total de animales ademas de sus datos
    # Tambien estara relacionado con habitat para poder dividir el zoo en diferentes sectores

    @api.onchange('pais_id')
    def onchange_pais_id(self):
        if self.pais_id:
            return {'domain': {'ciudad_id': [('pais_id', '=', self.pais_id.id)]}}