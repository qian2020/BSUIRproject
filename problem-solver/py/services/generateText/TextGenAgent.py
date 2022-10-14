from typing_extensions import Self
from common import ScModule, ScAgent, ScEventParams
from sc import *

def printInfo():
  print("this function information!!!")
class TextGenAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("sucessfuly init text generation module")
        # param = ""         
        src, questionNode = self.module.ctx.GetEdgeInfo(evt.edge_addr)         
        #answer = self.module.ctx.CreateNode(ScType.NodeConstStruct)         
        it_3 = self.module.ctx.Iterator3(questionNode, ScType.EdgeAccessConstPosPerm, ScType.Unknown)         
        if it_3.Next():             
          param = it_3.Get(2)
          print("###################################")
        determine_relation = self.module.ctx.Iterator3(param, ScType.EdgeAccessConstPosPerm, ScType.Unknown)
        num_element = 0
        while determine_relation.Next():
          print("------------------------")
          num_element += 1
        if num_element == 3:
          print("this is 3 element structure")
        return ScResult.Ok
    def printParamValue(self, param):
        paramValue = self.module.ctx.HelperGetSystemIdtf(param)
        print(paramValue)