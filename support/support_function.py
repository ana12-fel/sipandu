from sipandu_app.models import Data_link as dt_link

def global_var(request):
    data_link_footer = dt_link.objects.filter(link_sekolah = request.sekolah)

    print('cekcok', request.sekolah, data_link_footer)
    data = {
         'data_link_footer': data_link_footer,
    }
    return data

# JENJANG = global_var()['jenjang']
# TEMPLATE_NAME = global_var()['template_name']