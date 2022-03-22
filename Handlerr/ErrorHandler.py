from enum import Enum

class ErrorHandler:

    ErrorCodeSuffix = ""
    ErrorCollapse = None

    class ErrorTypes(Enum):
        ERROR = 0
        WARNING = 1
        INFO = 2 
        WRONG = 3

    __Instance = None

    @staticmethod
    def get_instance():
        if ErrorHandler.__Instance == None:
            ErrorHandler()
        return ErrorHandler.__Instance

    def __init__(self , ErrorCodeSuffix: str = "" , ErrorCollapse: bool = True) -> None:
        if ErrorHandler.__Instance != None: raise Exception()
        else: ErrorHandler.__Instance = self
        
        ErrorHandler.__Instance.ErrorCodeSuffix = ErrorCodeSuffix
        ErrorHandler.__Instance.ErrorCollapse = ErrorCollapse

    class Error:
        def __init__(self , ErrorType: int = 0 , Sentence: str = "Basic Error" , ErrorCode: int = 0) -> None:           
            self.errorType = ErrorType; self.sentence = Sentence; self.errorCode = ErrorCode
            raise Exception(ErrorHandler.ErrorTypes(self.errorType).name + " | " + ErrorHandler.get_instance().ErrorCodeSuffix + str(self.errorCode )+ " | " + self.sentence)

def main():
    ErrorHandler("CFG").Error(2 , "Big mistake" , 3)

if __name__ == "__main__":
    main()