class ErrorHandler:
    def __init__(self, retry) -> None:
        self.retry = retry

    def execute(self, callback, args, retry=0):
        try:
            return callback(args)
        except Exception as e:
            if retry == self.retry:
                raise e
            
            print(f'Error ({retry + 1}):', args)
            return self.execute(callback, args, retry + 1)
