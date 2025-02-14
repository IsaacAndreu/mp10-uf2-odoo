{
    'name': 'Propietats Immobiliàries',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Isaac Andreu',
    'category': 'Real Estate',
    'summary': 'Gestió de propietats i ofertes a Odoo',
    'description': """
        Aquest mòdul permet la gestió de propietats immobiliàries amb funcionalitats com:
        - Creació i edició de propietats
        - Gestió d’ofertes i clients
        - Càlcul automàtic del preu per m² i millor oferta
        - Assignació automàtica del comprador
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True
}
