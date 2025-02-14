from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Gestió de Propietats Immobiliàries'

    name = fields.Char('Nom de la Propietat', required=True)
    zip_code = fields.Char('Codi Postal', required=True)
    expected_price = fields.Float('Preu Esperat', required=True)
    final_sale_price = fields.Float('Preu Final', readonly=True, copy=False)
    total_area = fields.Float('Mida (m²)', required=True)
    status = fields.Selection(
        [
            ('new', 'Nova'),
            ('offer_received', 'Oferta Rebuda'),
            ('offer_accepted', 'Oferta Acceptada'),
            ('sold', 'Venuda'),
            ('canceled', 'Cancel·lada'),
        ],
        default='new', string="Estat"
    )
    property_type = fields.Many2one('estate.property.type', string="Tipus de Propietat")
    property_tags = fields.Many2many('estate.property.tag', string="Etiquetes")

    @api.depends('expected_price', 'total_area')
    def _calculate_price_m2(self):
        for record in self:
            record.price_per_square_meter = record.expected_price / record.total_area if record.total_area else 0
