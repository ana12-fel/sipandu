def global_var():
    data = {
<<<<<<< HEAD
        'jenjang': 'sd',
        'template_name': 'sd_01',

        'jenjang': 'smp',
        'template_name': 'smp_01'
=======
        'jenjang': 'sma',
        'template_name': 'sma_01'
>>>>>>> 0406747ed168ec3b8846a292e9325f0564a80c6f
    }
    return data

JENJANG = global_var()['jenjang']
TEMPLATE_NAME = global_var()['template_name']