<?php
session_start();

$host = 'sql6.freesqldatabase.com';
$db_name = 'sql6703448';
$db_user = 'sql6703448';
$db_password = 't181ZZyQ5m';
$port = 3306;

$mysqli = new mysqli($host, $db_user, $db_password, $db_name, $port);

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $userID = $_POST['userID'];
    $password = $_POST['password'];
    $sql = "SELECT ID, Password FROM user WHERE ID = ?";
    if ($stmt = $mysqli->prepare($sql)) {
        $stmt->bind_param("s", $param_id);
        $param_id = $userID;
        if ($stmt->execute()) {
            $stmt->store_result();
            if ($stmt->num_rows == 1) {
                $stmt->bind_result($id, $hashed_password);
                if ($stmt->fetch()) {
                    if (password_verify($password, $hashed_password)) {
                        $_SESSION["loggedin"] = true;
                        $_SESSION["id"] = $id;
                        header("location: work.html");
                    } else {
                        echo "The password you entered was not valid.";
                    }
                }
            } else {
                echo "No account found with that userID.";
            }
        } else {
            echo "Oops! Something went wrong. Please try again later.";
        }
        $stmt->close();
    }
}

$mysqli->close();
?>