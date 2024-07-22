// Function to open a table for viewing and editing
function openTable(tableName) {
    fetch(`php/getTable.php?table=${tableName}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('modalLabel').innerText = `View and Edit ${tableName}`;
            document.getElementById('modalBody').innerHTML = data;
            new bootstrap.Modal(document.getElementById('modal')).show();
        })
        .catch(error => console.error('Error:', error));
}

// Function to open management functions
function openManagement(action) {
    fetch(`php/management.php?action=${action}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('modalLabel').innerText = action.replace(/([A-Z])/g, ' $1');
            document.getElementById('modalBody').innerHTML = data;
            new bootstrap.Modal(document.getElementById('modal')).show();
        })
        .catch(error => console.error('Error:', error));
}

// Function to perform search
function performSearch() {
    let sqlSearch = document.getElementById('sqlSearch').value;
    let simpleSearch = document.getElementById('simpleSearch').value;
    let query = `sql=${encodeURIComponent(sqlSearch)}&simple=${encodeURIComponent(simpleSearch)}`;
    
    fetch(`php/search.php?${query}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('modalLabel').innerText = 'Search Results';
            document.getElementById('modalBody').innerHTML = data;
            new bootstrap.Modal(document.getElementById('modal')).show();
        })
        .catch(error => console.error('Error:', error));
}

// Function to check user access level
function checkAccessLevel(requiredLevel) {
    // Placeholder function. Implement actual access level check here.
    let userAccessLevel = getUserAccessLevel(); // Assume this function gets the user's access level
    return userAccessLevel >= requiredLevel;
}

// Placeholder function to get user access level
function getUserAccessLevel() {
    // Implement actual logic to get user access level
    return 2; // Example: return 2 as an access level
}

// Placeholder function to save changes
function saveChanges() {
    // Implement save changes logic
    console.log('Save changes clicked');
}