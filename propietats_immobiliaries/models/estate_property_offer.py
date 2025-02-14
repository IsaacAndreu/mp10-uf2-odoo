from odoo import models, fields

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Gestió d’Ofertes de Propietats'

    offer_price = fields.Float('Import de l’Oferta', required=True)
    status = fields.Selection(
        [('accepted', 'Aprovada'), ('rejected', 'Denegada'), ('pending', 'Pendent')],
        default='pending', string="Estat de l’Oferta"
    )
    customer_id = fields.Many2one('res.partner', string="Interessat")
    related_property = fields.Many2one('estate.property', string="Propietat Associada", readonly=True)
