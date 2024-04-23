def global_var():
    data = {
        'jenjang': 'sma',
        'template_name': 'sma_01'
    }
    return data

JENJANG = global_var()['jenjang']
TEMPLATE_NAME = global_var()['template_name']