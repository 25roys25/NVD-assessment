# CVE Information Fetcher & Visualizer

## Project Overview

This project provides an interface to fetch, store, and display CVE (Common Vulnerabilities and Exposures) data from the **National Vulnerability Database (NVD)** using their official **CVE API**. It allows users to retrieve, view, and filter vulnerability details in a structured and interactive web interface. The backend is built using **Python Flask**, and the frontend uses **HTML**, **CSS**, and **JavaScript**.

### Core Features:
- Fetch CVE data from NVD using paginated API calls.
- Data is displayed in a table format on the frontend.
- Support for filtering by CVE ID, CVSS score, modification date, and year.
- Simple frontend with options for sorting and pagination.
- API to retrieve filtered CVE data based on user parameters.

---

## Features

### 1. **API Integration**
   - Fetch CVE information from NVD API (https://services.nvd.nist.gov/rest/json/cves/2.0).
   - Paginate through CVE data using the `startIndex` and `resultsPerPage` parameters.
   - Display detailed CVE information (such as CVE ID, Description, CVSS score, etc.).

### 2. **Filtering and Search**
   - Filter CVEs by:
     - **CVE ID**
     - **CVE Year**
     - **CVSS Score** (based on **CVSS v2** or **CVSS v3**)
     - **Last Modified Date** (within a specific number of days)

### 3. **User Interface**
   - Display CVE entries in a table format with paginated results.
   - Allow the user to choose how many results per page (options for 10, 50, or 100).
   - Option to paginate through results with "Previous" and "Next" buttons.

---

## Installation

### Prerequisites
1. **Python 3.x** (for backend development using Flask)
2. **pip** (Python package installer)
3. **Flask** (Python web framework)
4. **requests** (for making HTTP requests to the NVD API)

### Steps to Install and Run

#### 1. Clone the repository:

```bash
https://github.com/25roys25/NVD-assessment.git
cd SECURIN
