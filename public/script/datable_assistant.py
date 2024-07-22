<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Datable</title>
  <style>
    /* Add your styles here */
  </style>
  <script>
    function openModal(table) {
      // Make an AJAX call to fetch the table data
      fetch(`/getTable.php?table=${table}`)
        .then(response => response.text())
        .then(data => {
          document.getElementById("modalContent").innerHTML = data;
          document.getElementById("modal").style.display = "block";
        });
    }

    function closeModal() {
      document.getElementById("modal").style.display = "none";
    }
  </script>
</head>
<body>
  <!-- Your existing content -->
  
  <div id="modal" style="display: none;">
    <div>
      <span onclick="closeModal()">Close</span>
      <div id="modalContent"></div>
    </div>
  </div>

  <button onclick="openModal('log')">Log</button>
  <button onclick="openModal('item')">Item</button>
  <button onclick="openModal('user')">User</button>
  <button onclick="openModal('category')">Category</button>
  <button onclick="openModal('department')">Department</button>
</body>
</html>