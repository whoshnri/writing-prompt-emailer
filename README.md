# writing-prompt-emailer
A service that emails me prompts to write articles about every day to build my writing habit (I just had to build one myself)

So basically the flow of this project is simple >> The prompts are generated >> The result is returned into the email file >> The email is constructed and sent to the recipient email

Server credentials are stored in the .env file

## Automating the Task

To repeat the prompt-emailing task every time you run a bash script, you can create a shell script that runs the python file in a loop

```bash
#!/bin/bash
while true; do
    python emailer.py
    sleep 86400  # Waits for a day from the current time
done
```
Ai generated:
# Also :
If you want the task to run once per script execution, simply call your main script in the bash file:

```bash
#!/bin/bash
python send_prompt.py
```

**Note:**  
- Make sure to activate your virtual environment and install required modules (like `smtplib`, `dotenv`, etc.)

**Please feel free to add stuff to this and comment appropriate**
----Committed changes here----
