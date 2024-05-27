<?php
header('Content-Type: application/json');

// Database configuration
$servername = "localhost";
$username = "your_db_username";
$password = "your_db_password";
$dbname = "your_db_name";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    echo json_encode(['status' => 'error', 'message' => 'Connection failed: ' . $conn->connect_error]);
    exit();
}

// Get user input from form
$userID = $_POST['userID'];
$password = $_POST['password'];

// Prepare and bind
$stmt = $conn->prepare("SELECT * FROM users WHERE userID = ? AND password = ?");
$stmt->bind_param("ss", $userID, $password);

// Execute statement
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    // Login successful
    echo json_encode(['status' => 'success']);
} else {
    // Login failed
    echo json_encode(['status' => 'fail']);
}

$stmt->close();
$conn->close();
?>