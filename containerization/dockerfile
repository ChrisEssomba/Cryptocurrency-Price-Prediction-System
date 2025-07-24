# Set the programming language #type python version in your venv and copy what you see (all in lower case)
FROM python:3.12.1

#Set the working directory
WORKDIR /app

#Copy the requirements
COPY requirements.txt .

#Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

#Copy everything into the 
COPY . .

#Set the port 
EXPOSE 5000

#Set the command to run the script
CMD ["python", "app.py"]

