<!-- logout.php -->

<?php
    session_start();

    // Hapus semua variabel sesi
    session_unset();

    // Hancurkan sesi
    session_destroy();

    // Redirect ke halaman login atau halaman lainnya jika diperlukan
    header('Location: login.php');
    exit;
?>
