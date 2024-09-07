# Dashboard Application

## Overview

This project is a dashboard application that displays various charts including Line, Bar, Pie, and Candlestick charts. It uses NextJs for the frontend and communicates with a Django backend to fetch data.

## Installation

To set up the project, follow these steps:

### Using Docker

1. **Build and start Docker containers**:

   ```bash
   docker-compose up --build
   ```

2. **Access the application**:

   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:8000`

3. **Stop Docker containers**:
   ```bash
   docker-compose down
   ```

### Without Docker

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Run the backend server**:
   Ensure your Django backend server is running at `http://127.0.0.1:8000`.

4. **Start the frontend application**:
   ```bash
   npm run dev
   ```

## Project Structure

- `app/front-end/` - Contains the frontend React application.
- `app/back-end/` - Contains the Django backend (not included in this repo).

## Usage

### Frontend

1. Navigate to the frontend directory:

   ```bash
   cd app/front-end
   ```

2. Start the development server:

   ```bash
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:3000` to view the dashboard.

## Running Tests

This project uses [Jest](https://jestjs.io/) for testing. Follow the steps below to set up the testing environment and run the test cases.

### Dependencies

Ensure you have the following dependencies installed:

- **Node.js**: Ensure you have [Node.js](https://nodejs.org/) installed. The LTS version is recommended.
- **Jest**: The testing framework used in this project.

### Installation

1. **Install Jest** (if not already installed):

   ```bash
   npm install --save-dev jest
   ```

2. **Install TypeScript support for Jest** (if you are using TypeScript):
   ```bash
   npm install --save-dev ts-jest @types/jest
   ```

To run the test cases:

1. **Run Jest**:

   ```bash
   npm test
   ```

2. **Run Jest with a watch mode** (to watch for changes and rerun tests automatically):
   ```bash
   npm test --watch
   ```

### Backend Tests

Ensure you have the following dependencies installed:

#### Installation

1. **Install Python dependencies** (assuming you have a `requirements.txt` file):

   ```bash
   pip install -r requirements.txt
   ```

2. **Install pytest**:
   ```bash
   pip install pytest
   ```

#### Running Tests

To run the backend test cases:

1. **Navigate to the backend directory**:

   ```bash
   cd app/back-end
   ```

2. **Run pytest**:

   ```bash
   pytest
   ```

3. **Run pytest with a watch mode** (using `pytest-watch` for automatic test reruns):
   ```bash
   pip install pytest-watch
   ptw
   ```

### Troubleshooting

- **Frontend Test Issues**:

  - **Unexpected reserved word 'interface'**: If you encounter errors related to TypeScript syntax, ensure that your Jest configuration is set up to handle TypeScript.
  - **ESM (ECMAScript Modules) Issues**: If you are using ECMAScript modules and facing issues, ensure that your Jest configuration includes settings for ES modules.

- **Backend Test Issues**:
  - **Database Migrations**: Ensure all migrations are applied before running tests.
    ```bash
    python manage.py migrate
    ```

## Docker Commands

- **Build Docker images and start containers**:

  ```bash
  docker-compose up --build
  ```

- **Stop and remove Docker containers**:

  ```bash
  docker-compose down
  ```

- **View Docker container logs**:

  ```bash
  docker-compose logs
  ```

- **Access a running Docker container**:
  ```bash
  docker-compose exec <service-name> /bin/sh
  ```
  Replace `<service-name>` with the name of the service you want to access (e.g., `frontend` or `backend`).

## Contact

For any questions or issues, please contact [Manvi Kishore] at [manvi.kishore07@gmail.com].

## Aproach

To create the dashboard application, I began by defining the requirements and chose NextJs framework with Typescript for the frontend. For data visualization, I utilized `recharts` and `react-apexcharts` to render Line, Bar, Pie, and Candlestick charts.These charts are completely responsive. The frontend interacts with the Django backend through RESTful APIs to fetch and display data. In the backend, I built APIs using Django and Django REST framework, ensuring robust data handling and error management.

I employed dynamic imports and React hooks for state management to optimize performance. Testing was a key focus; I set up Jest to test React components and TypeScript code. For backend testing, I used Django's test framework to ensure API endpoints were functioning correctly. Docker was used to containerize both the frontend and backend, streamlining development and deployment. The README was updated with comprehensive instructions for setup, testing (both frontend and backend), and Docker commands to ensure a smooth workflow.
