# -*- coding: utf-8 -*-
{
    'name': "reserva",

    'summary': """
        Sistema de Control de reserva de habitaciones, y Servicios""",

    'description': """
        Reserva de habitaciones, sauna, gimnacio, salon tanto para los pasajeros del hotel como para empresas
    """,

    'author': "PABAKA",
    'website': "http://www.pabaka.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reserva.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
}