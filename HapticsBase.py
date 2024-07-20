import abc

class HapticsBase:
    def __init__(self) -> None:
        pass
    
    @abc.abstractmethod
    def GetPattern(self) -> dict:
        '''
        Returns a dictionary with the affected haptic dots
        
        Keys:
        - "front": dots at the front of the haptic vest
        - "back": dots at the back of the haptic vest

        More keys can be added for more haptic areas (face cover, gloves, etc)
        '''
        pass