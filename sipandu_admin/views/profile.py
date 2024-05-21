from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sipandu_app.models import Master_user


def IndexProfile(request):
    # Mendapatkan objek User yang sedang login
    user = request.user

    # Jika user tidak anonim dan objek Master_user-nya ada, ambil informasinya
    if not user.is_anonymous:
        try:
            master_user = Master_user.objects.get(user_email=user.user_email)
            first_name = master_user.user_first_name
            last_name = master_user.user_last_name
            email = master_user.user_email
            # Tambahkan atribut lainnya sesuai kebutuhan
        except Master_user.DoesNotExist:
            # Jika tidak ada objek Master_user yang sesuai dengan email pengguna, atur nilai None
            master_user = None
            first_name = None
            last_name = None
            email = None
            # Tambahkan atribut lainnya sesuai kebutuhan
    else:
        # Jika user anonim, atur nilai None untuk semua informasi
        master_user = None
        first_name = None
        last_name = None
        email = None
        # Tambahkan atribut lainnya sesuai kebutuhan

    # Siapkan context untuk dikirim ke template
    context = {
        'master_user': master_user,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        # Tambahkan atribut lainnya sesuai kebutuhan
    }

    return render(request, 'admin/profile/profile.html', context)


