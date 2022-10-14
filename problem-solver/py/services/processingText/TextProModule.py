from common import ScModule, ScKeynodes, ScPythonEventType
from keynodes import Keynodes
from TextProAgent import TextProAgent

from sc import *


class TextProModule(ScModule):

    def __init__(self):
        ScModule.__init__(
            self,
            ctx=__ctx__,
            cpp_bridge=__cpp_bridge__,
            keynodes=[
            ],
            )

    def OnInitialize(self, params):
        print('Initialize Text processing module')
        agent = TextProAgent(self)         
        fa_addr = self.ctx.HelperResolveSystemIdtf("question_processing_text", ScType.NodeConstClass)         
        agent.Register(fa_addr, ScPythonEventType.AddOutputEdge) 

    def OnShutdown(self):        
        print('Shutting down Text processing module')  


service = TextProModule()
service.Run()
