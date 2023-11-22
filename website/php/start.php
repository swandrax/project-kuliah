<!-- index.html -->
<?php
    session_start();

    // Fungsi contoh untuk mendapatkan username
    function get_username() {
        return isset($_SESSION['username']) ? $_SESSION['username'] : null;
    }
?>

<!-- ... (kode sebelumnya) -->

<div class="container mt-4">
    <?php if (get_username()): ?>
        <h2>Welcome, <?php echo get_username(); ?>!</h2>
        <a href="logout.php" class="btn btn-danger btn-logout">Logout</a>
    <?php else: ?>
        <h2>Welcome to Warung Usaha</h2>
        <p>Explore our products and services.</p>
        <a href="login.php" class="btn btn-primary">Login</a>
    <?php endif; ?>
</div>
