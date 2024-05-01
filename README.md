# School Resources Management System

This is a school resource management system developed as an ICT SBA (School-Based Assessment) project. The system allows schools to effectively manage and monitor their assets, such as furniture, equipment, and other resources.

## Key Features

- **Systematic Data Storage**: The system provides an organized way to store and manage information about the school's resources, including details such as supplier, price, and other relevant data.
- **Accurate Resource Monitoring**: The system keeps track of resource modifications, replacement records, and maintenance schedules. It also provides alerts for overdue returns and allows for discrepancy handling during stock-taking.
- **Flexible User Permissions**: The system supports flexible assignment of resource management responsibilities to different departments and staff members, ensuring proper stewardship and maintenance of the school's assets.
- **Single and Bulk Item Handling**: The system can handle the recording of both individual resources (e.g., digital cameras, pianos) and large quantities of the same type of resource (e.g., student desks, chairs), allowing the school to have a comprehensive overview of its asset dynamics.

## System Design

The system uses a relational database design to ensure data integrity and consistency. The main entities include:

- **Item**: Represents the school's resources
- **Category**: Categorizes the resources
- **Log**: Records the borrowing and returning of resources
- **User**: Stores information about the system users
- **Department**: Describes the school's organizational structure

The system also incorporates features like data rollback, data privacy and access control, and data normalization to ensure data integrity and efficient management.

## Technologies Used

- **Database**: MySQL (standalone version)
- **Web Server**: XAMPP (Apache, PHP)
- **Programming Language**: PHP

## How to Run the System

1. Install XAMPP (or any other similar web server stack) on your local machine.
2. Clone the project repository to the `htdocs` folder of your XAMPP installation.
3. Start the Apache and MySQL services in XAMPP.
4. Open a web browser and navigate to `http://localhost/student-resources-management-system`.
5. The system should be up and running, and you can explore its features.

## Conclusion

The Student Resources Management System provides a practical solution for schools to effectively manage and monitor their assets. By leveraging a relational database and modern web technologies, the system ensures data integrity, user-friendly experience, and efficient resource management.