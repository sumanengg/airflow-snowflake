# /*
#  * File: Dockerfile
#  * Project: airflow-docker
#  * File Created: Sunday, 5th May 2024 5:37:28 pm
#  * Author: Vithushan Sylvester (https://www.linkedin.com/in/msvithushan/)
#  * -----
#  * Last Modified: Sunday, 5th May 2024 5:43:19 pm
#  * Modified By: Vithushan Sylvester (https://www.linkedin.com/in/msvithushan/>)
#  * -----
#  * Copyright 2024 - 2024 Vithushan Sylvester
#  */

FROM apache/airflow:2.0.1
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
