md
# Freelancer Business Activities Interactive Platform

## Overview
This repository provides the code for creating an interactive platform to explore the Freelancer Business Activities Dataset from Abu Dhabi. The platform allows users to search, filter, and analyze the data in a user-friendly web interface with support for English and Arabic.

## Features
- Search for specific freelancer business activities.
- Filter activities by category.
- View detailed information about each activity (ID, English Name, Arabic Name).
- Multi-language support (English and Arabic).
- Interactive data visualizations.
- Bookmark favorite activities.
- Share insights on social media.
- Subscribe to updates for specific activity categories.

## Requirements
- Python 3.8+
- Flask
- Pandas
- Jinja2

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/freelancer-business-activities.git
   
2. Navigate to the project directory:
   bash
   cd freelancer-business-activities
   
3. Install the dependencies:
   bash
   pip install flask pandas
   
4. Download the dataset from the [Abu Dhabi Open Data Platform](https://data.abudhabi/dataset/Freelancer_Business_Activities.xlsx) and save it in the project directory.

## Usage
1. Start the Flask server:
   bash
   python app.py
   
2. Open your browser and navigate to `http://127.0.0.1:5000/`.
3. Use the search and filter functionalities to explore the dataset.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   bash
   git checkout -b feature-name
   
3. Commit your changes:
   bash
   git commit -m "Description of changes"
   
4. Push to the branch:
   bash
   git push origin feature-name
   
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Support
For any issues or questions, please contact [Abu Dhabi Open Data Platform Support](mailto:opendata@abudhabi.gov.ae).
