## Handl-Err .Py
*Python error handler for debugging.*

## Installation
```python
  pip install Handlerrpy
```

## Using
Create an instance
```python
  from ErrorHandler import *
  handler = ErrorHandler("MX",True) # Args: ErrorCodeSuffix , ErrorCollapse
  handler.Error(1 , " Basic Error " , 0) # Args: ErrorType , Sentence , ErrorCode
```

## Error Types
```python
  ERROR = 0
  WARNING = 1
  INFO = 2
  WRONG = 3
```

## For help
==FatihFruktoz#0649==
