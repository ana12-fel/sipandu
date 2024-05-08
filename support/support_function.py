def global_var():
    data = {
         #'jenjang': 'smp',
         #'template_name': 'smp_01'

        # 'jenjang': 'sd',
        # 'template_name': 'sd_01'

         'jenjang': 'sd',
         'template_name': 'sd_01'
    }
    return data

JENJANG = global_var()['jenjang']
TEMPLATE_NAME = global_var()['template_name']