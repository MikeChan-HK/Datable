<?php
require 'db_connection.php';

$table = $_GET['table'];
$sql = "SELECT * FROM $table";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table class='table'>";
    echo "<thead><tr>";
    $fields = $result->fetch_fields();
    foreach ($fields as $field) {
        echo "<th>{$field->name}</th>";
    }
    echo "</tr></thead><tbody>";
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        foreach ($row as $data) {
            echo "<td>{$data}</td>";
        }
        echo "</tr>";
    }
    echo "</tbody></table>";
} else {
    echo "No records found.";
}

$conn->close();
?>
