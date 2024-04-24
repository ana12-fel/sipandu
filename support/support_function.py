def global_var():
    data = {
<<<<<<< HEAD
        # 'jenjang': 'smp',
        # 'template_name': 'smp_01'

        'jenjang': 'sd',
        'template_name': 'sd_01'
=======
        'jenjang': 'smp',
        'template_name': 'smp_01'
>>>>>>> 8c572642e01f286113ca6e9fb2b062878fc5cfc3
    }
    return data

JENJANG = global_var()['jenjang']
TEMPLATE_NAME = global_var()['template_name']