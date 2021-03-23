# PasswordManager
This is a Python Tool that encodes Passwords and Usernames twice.
First into base64 string and then the whole File into bytes and sha256 unbypassed encoding variant.
So you can say, your Passwords are secure than.
It also has a Module to generate Random 40 digit Passwords with a great unbrutforceable entropy.

# Installation:
```ruby
pip install requirements.txt
```
# troubleshooting 
if you get a no module named "Crypto" - Error:

exectue `troubleshoot_crypto/fix_Crypto_not _found_error.bat` on win.
You have to give in the Version of Python like a Directory-name [For example: Python 3.9.4 gets to Python39 and Python 3.8.xy gets to Python38]
This will change the Directory Name of the Crypto-Module in the site-packages folder of your Pythons environmental path from "crypto" to "Crypto".
If you are on osx, please do this by hand.




