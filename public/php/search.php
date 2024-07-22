<?php
require 'db_connection.php';

$sqlQuery = $_GET['sql'];
$simpleSearch = $_GET['simple'];
$response = '';

if (!empty($sqlQuery)) {
    // Execute the SQL query provided by the user
    $result = $conn->query($sqlQuery);
    if ($result) {
        $response .= "<table class='table'><thead><tr>";
        $fields = $result->fetch_fields();
        foreach ($fields as $field) {
            $response .= "<th>{$field->name}</th>";
        }
        $response .= "</tr></thead><tbody>";
        while ($row = $result->fetch_assoc()) {
            $response .= "<tr>";
            foreach ($row as $data) {
                $response .= "<td>{$data}</td>";
            }
            $response .= "</tr>";
        }
        $response .= "</tbody></table>";
    } else {
        $response .= "Error: " . $conn->error;
    }
} elseif (!empty($simpleSearch)) {
    // Perform a simple search across relevant tables
    
    $response .= "Simple search results for: " . htmlspecialchars($simpleSearch);
}

echo $response;

$conn->close();
?>
