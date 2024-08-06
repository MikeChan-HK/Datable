<?php
$servername = "aws-0-ap-northeast-1.pooler.supabase.com";
$username = "postgres.zscwjnenquldkaooixnf";
$password = "datable2024ictsba";
$port = 6543
$dbname = "postgres";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
