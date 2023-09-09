# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'GPSMap SolesGPS',
    'price' : '0.0',
    'currency' : 'EUR',
    'license' : 'LGPL-3',
    'images': ['static/description/map_online.png'],    
    'author': "SolesGPS :: Eduardo Vizcaino",
    'category': 'fleet, GPS, Geolocation',
    "version": "15.0.0.0.1",
    'website' : 'https://solesgps.com',
    'summary' : 'Locate the satellite coordinates that your GPS devices throw. Save that information here and see it on the map.',
    'description' : """
Vehicle, leasing, insurances, cost
==================================
With this module, Odoo helps you managing all your vehicles, the
contracts associated to those vehicle as well as services, fuel log
entries, costs and many other features necessary to the management 
of your fleet of vehicle(s)

Main Features
-------------
* Add vehicles to your fleet
* Manage contracts for vehicles
* Reminder when a contract reach its expiration date
* Add services, fuel log entry, odometer values for all vehicles
* Show all costs associated to a vehicle or to a type of service
* Analysis graph for costs
""",
    'depends': [
        'gpsmap',        
        #'website_crm',
    ],
    'data': [
        'data/ir_config_parameter.xml',
        'data/ir_attachment.xml',
        
        'data/res_company_data.xml',
        'data/res_config_settings.xml',
        
        'data/res_partner.xml',
        'data/res_users.xml',
        'data/gps_geofences.xml',

        'data/gps_devices.xml',
        'data/fleet_vehicle.xml',
        'data/gps_alerts.xml',
        'data/gps_mirror.xml',
        
        'security/security.xml',
        'views/views.xml',
        'views/website_aboutus.xml',
        'views/website_contactus_thanks.xml',
        'views/website_contactus.xml',
        'views/website_footer_custom.xml',
        'views/homepage.xml',
    ],

    'installable': True,
    'application': True,
}
