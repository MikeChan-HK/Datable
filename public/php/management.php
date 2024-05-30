<?php
require 'db_connection.php';

$action = $_GET['action'];
$response = '';

switch ($action) {
    case 'itemLoanReturn':
        $response = getItemLoanReturnForm();
        break;
    case 'userManagement':
        $response = getUserManagementForm();
        break;
    case 'viewAllRecords':
        $response = getAllRecords();
        break;
    default:
        $response = 'Invalid action';
}

echo $response;

function getItemLoanReturnForm() {
    // Generate form for Item Loan and Return Registration
    return '<form>
                <!-- Form content here -->
            </form>';
}

function getUserManagementForm() {
    // Generate form for User Management
    return '<form>
                <!-- Form content here -->
            </form>';
}

function getAllRecords() {
    // Fetch and display all records from log table
    global $conn;
    $sql = "SELECT * FROM log";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $output = "<table class='table'>";
        $output .= "<thead><tr>";
        $fields = $result->fetch_fields();
        foreach ($fields as $field) {
            $output .= "<th>{$field->name}</th>";
        }
        $output .= "</tr></thead><tbody>";
        while ($row = $result->fetch_assoc()) {
            $output .= "<tr>";
            foreach ($row as $data) {
                $output .= "<td>{$data}</td>";
            }
            $output .= "</tr>";
        }
        $output .= "</tbody></table>";
        return $output;
    } else {
        return "No records found.";
    }
}

$conn->close();
?>
