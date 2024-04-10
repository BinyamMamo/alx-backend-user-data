# 🧬 0x00. Personal data

![](https://www.radicalcompliance.com/wp-content/uploads/2024/02/meme-data.jpg)

## Project Overview 🪶
This project 📚 focuses on implementing secure 🔒 handling of personal data 📂 in a Python 🐍 application. 
It covers concepts such as:
- encrypting passwords 🔑, 
- obfuscating Personally Identifiable Information (PII) 🕵️‍♂️, and 
- authenticating to a database 🗄️ securely 🔐.

## 🔧 Requirements and Dependencies:
----------------------------------------------
- Python 3.7 🐍
- Required libraries:
  - bcrypt 🔐
  - mysql-connector-python 💽

## 📚 Tasks:
### 0. Regex-ing
---------------------
**📜 Task requirements:** Implement a function called `filter_datum` to obfuscate PII fields in log messages using regex.

**🗂️ Files:** 
- **[filtered_logger.py](filtered_logger.py)**

**🗒️ Description:** 
- `filtered_logger.py` contains the implementation of the `filter_datum` function using regular expressions to obfuscate PII fields in log messages.

### 1. Log formatter
---------------------
**📜 Task requirements:** Implement a custom log formatter class `RedactingFormatter` that filters values in log records using `filter_datum`.

**🗂️ Files:** 
- **[filtered_logger.py](filtered_logger.py)**

**🗒️ Description:** 
- `filtered_logger.py` contains the implementation of the `RedactingFormatter` class, which formats log records to filter PII fields using the `filter_datum` function.

### 2. Create logger
---------------------
**📜 Task requirements:** Implement a function `get_logger` to create a logger object with specific configurations, including a custom log formatter.

**🗂️ Files:** 
- **[filtered_logger.py](filtered_logger.py)**

**🗒️ Description:** 
- `filtered_logger.py` contains the implementation of the `get_logger` function to create a logger with customized settings for PII filtering.

### 3. Connect to secure database
---------------------
**📜 Task requirements:** Implement a function `get_db` to connect securely to a database using environment variables for credentials.

**🗂️ Files:** 
- **[filtered_logger.py](filtered_logger.py)**

**🗒️ Description:** 
- `filtered_logger.py` contains the implementation of the `get_db` function to establish a secure connection to a MySQL database using environment variables.

### 4. Read and filter data
---------------------
**📜 Task requirements:** Implement a function to retrieve and display data from a database while filtering PII fields in the output log.

**🗂️ Files:** 
- **[filtered_logger.py](filtered_logger.py)**

**🗒️ Description:** 
- `filtered_logger.py` contains the implementation of the main function to retrieve and display data from a database with filtered PII fields in the log output.

### 5. Encrypting passwords
---------------------
**📜 Task requirements:** Implement a function `hash_password` to securely hash passwords using bcrypt.

**🗂️ Files:** 
- **[encrypt_password.py](encrypt_password.py)**

**🗒️ Description:** 
- `encrypt_password.py` contains the implementation of the `hash_password` function to securely hash passwords using bcrypt.

### 6. Check valid password
---------------------
**📜 Task requirements:** Implement a function `is_valid` to validate passwords against their hashed counterparts using bcrypt.

**🗂️ Files:** 
- **[encrypt_password.py](encrypt_password.py)**

**🗒️ Description:** 
- `encrypt_password.py` contains the implementation of the `is_valid` function to validate passwords against their hashed counterparts using bcrypt.

## 🎓 Key Takeaways
In this project 📚, I learned:

- how to securely 🔒 handle personal data 📂 in Python 🐍 applications, including techniques for
  - obfuscating PII 🕵️‍♂️, 
  - encrypting passwords 🔑, and 
  - connecting to databases 🗄️ securely. 

 - I gained a deeper understanding 🧠 of the importance of protecting sensitive information 🛡️ and 
 - best practices for data security 🔐 in software development 💻.

 ## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.github.io)

<pre id="banner" style="color: teal" align="center">


 █████╗ ██╗     ██╗  ██╗    ███████╗██╗    ██╗███████╗
██╔══██╗██║     ╚██╗██╔╝    ██╔════╝██║    ██║██╔════╝
███████║██║      ╚███╔╝     ███████╗██║ █╗ ██║█████╗  
██╔══██║██║      ██╔██╗     ╚════██║██║███╗██║██╔══╝  
██║  ██║███████╗██╔╝ ██╗    ███████║╚███╔███╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚══════╝
                                                      
</pre>