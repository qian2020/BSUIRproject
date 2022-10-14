from common import ScModule, ScKeynodes, ScPythonEventType
from keynodes import Keynodes
from TextGenAgent import TextGenAgent

from sc import *


class TextGenModule(ScModule):

    def __init__(self):
        ScModule.__init__(
            self,
            ctx=__ctx__,
            cpp_bridge=__cpp_bridge__,
            keynodes=[
            ],
            )

    def OnInitialize(self, params):
        print('Initialize Text generation module')        
        print('text generation Chinese')
        agent = TextGenAgent(self)         
        fa_addr = self.ctx.HelperResolveSystemIdtf("question_generate_text", ScType.NodeConstClass)         
        agent.Register(fa_addr, ScPythonEventType.AddOutputEdge) 

    def OnShutdown(self):        
        print('Shutting down Text generation module')  


service = TextGenModule()
service.Run()
