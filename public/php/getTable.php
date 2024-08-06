<?php
$servername = "aws-0-ap-northeast-1.pooler.supabase.com";
$username = "postgres.zscwjnenquldkaooixnf";
$password = "datable2024ictsba";
$port = 6543
$dbname = "postgres";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$table = $_GET['table'];
$sql = "SELECT * FROM $table";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  echo "<table border='1'>";
  while($row = $result->fetch_assoc()) {
    echo "<tr>";
    foreach ($row as $cell) {
      echo "<td>" . htmlspecialchars($cell) . "</td>";
    }
    echo "</tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}

$conn->close();
?>