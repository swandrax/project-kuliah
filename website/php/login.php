<!-- login.php -->

<?php
    session_start();

    // Fungsi contoh untuk login (gantilah dengan validasi sesuai kebutuhan)
    function login($username, $password) {
        // Validasi contoh, gantilah dengan validasi sesuai kebutuhan
        if ($username === 'user' && $password === 'password') {
            $_SESSION['username'] = $username;
            return true;
        }
        return false;
    }

    // Jika formulir login dikirim
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Lakukan validasi login
        if (login($username, $password)) {
            header('Location: index.html');
            exit;
        } else {
            $error_message = 'Invalid username or password.';
        }
    }
?>