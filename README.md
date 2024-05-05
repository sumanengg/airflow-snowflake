# Airflow-Snowflake Integration Project

This project provides an Airflow setup, complete with the necessary plugins to establish a connection to a Snowflake data source.

## Project Description

The Airflow-Snowflake Integration Project is designed to facilitate the seamless integration of Airflow with Snowflake. This is achieved through the use of specific plugins that enable the connection to the Snowflake source. For more detailed information about the project, please refer to our blog article on Medium.

### Medium Article

The article can be found [here](https://msvithushan.medium.com/simplified-guide-integrating-snowflake-with-airflow-0ae970b265cf).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/products/docker-desktop).

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Setup

To set up the project, follow these steps:

1. Initialize Airflow:
   ```
   docker compose up airflow-init
   ```
2. Start the project:
   ```
   docker compose up
   ```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
