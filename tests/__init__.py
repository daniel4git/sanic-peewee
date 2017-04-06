class Config:
    def __init__(self,**kws):
        if kws:
            for k,v in kws.items():
                self.k = v


class FakeSanis:
    def __init__(self):
        self.config = Config()
