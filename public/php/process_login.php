<?php
// Include database connection file
include('db_connection.php');

// Start session
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get userID and password from the form
    $userID = $_POST['userID'];
    $password = $_POST['password'];

    // Prepare and bind
    $stmt = $conn->prepare("SELECT ID, password FROM user_table WHERE ID = ?");
    $stmt->bind_param("s", $userID);
    $stmt->execute();
    $stmt->store_result();
    
    // Check if the user exists
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($id, $hashed_password);
        $stmt->fetch();

        // Verify password
        if (password_verify($password, $hashed_password)) {
            // Password is correct, start a new session
            $_SESSION['userID'] = $id;
            echo json_encode(['status' => 'success']);
        } else {
            // Password is incorrect
            echo json_encode(['status' => 'error', 'message' => 'Invalid userID or password']);
        }
    } else {
        // User does not exist
        echo json_encode(['status' => 'error', 'message' => 'Invalid userID or password']);
    }

    // Close statement
    $stmt->close();
} else {
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method']);
}

// Close connection
$conn->close();
?>