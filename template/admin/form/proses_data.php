<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proses Data Sekolah</title>
</head>
<body>
    <h2>Data Jenjang Pendidikan</h2>
    <?php
    // Mengecek apakah data telah dikirim melalui metode POST
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Mendapatkan nilai jenjang dan status dari form
        $jenjang = $_POST["jenjang"];
        $status = $_POST["status"];
        
        // Menampilkan data yang diterima
        echo "<p>Jenjang: $jenjang</p>";
        echo "<p>Status Aktif: $status</p>";
        
        // Anda juga dapat menyimpan data ini ke database atau melakukan tindakan lainnya di sini
    } else {
        // Jika tidak ada data yang dikirim melalui metode POST, maka tampilkan pesan kesalahan
        echo "<p>Data tidak ditemukan.</p>";
    }
    ?>
</body>
</html>
