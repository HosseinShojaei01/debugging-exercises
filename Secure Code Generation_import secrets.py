Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/University/SaX/Portfolio/Python Password Generator.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\hosse\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py", line 1962, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "C:/University/SaX/Portfolio/Python Password Generator.py", line 12, in Random
    replace_index = random.randrange(len(new_password)//2)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\hosse\AppData\Local\Programs\Python\Python312\Lib\random.py", line 309, in randrange
    raise ValueError("empty range for randrange()")
ValueError: empty range for randrange()
>>> 
======= RESTART: C:/University/SaX/Portfolio/Python Password Generator.py ======
