<?php
// php/process_login.php

require 'db_connection.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Validate input
    if (empty($username) || empty($password)) {
        echo "Username and password are required.";
        exit;
    }

    // Protect against SQL injection
    $username = $conn->real_escape_string($username);
    $password = $conn->real_escape_string($password);

    // Check credentials
    $sql = "SELECT * FROM user WHERE User_Name = '$username'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        // Verify password
        if (password_verify($password, $user['Password'])) {
            // Password is correct
            session_start();
            $_SESSION['user_id'] = $user['ID'];
            $_SESSION['username'] = $user['User_Name'];
            $_SESSION['access_level'] = $user['Access_Level'];
            header("Location: work.html");
        } else {
            // Password is incorrect
            echo "Invalid password.";
        }
    } else {
        // User not found
        echo "User not found.";
    }
}

$conn->close();
?>