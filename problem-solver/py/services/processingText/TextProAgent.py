from typing_extensions import Self
from common import ScModule, ScAgent, ScEventParams
from sc import *

def printInfo():
  print("this function information!!!")
class TextProAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("sucessfuly generation natural language text")
        # param = ""         
        src, questionNode = self.module.ctx.GetEdgeInfo(evt.edge_addr)         
        #answer = self.module.ctx.CreateNode(ScType.NodeConstStruct)         
        it_3 = self.module.ctx.Iterator3(questionNode, ScType.EdgeAccessConstPosPerm, ScType.Unknown)         
        if it_3.Next():             
          param = it_3.Get(2)
          print("###################################")
        key_relation1 = self.module.ctx.HelperResolveSystemIdtf("nrel_sc_text_translation", ScType.NodeConstNoRole)
        print("key_relation1")
          # it_findSentence_step1 = self.module.ctx.Iterator3(ScType.NodeConstTuple, ScType.EdgeDCommonConst, param)
        it_findSentence_step1 = self.module.ctx.Iterator5(ScType.NodeConstTuple, ScType.EdgeDCommonConst, param, ScType.EdgeAccessConstPosPerm, key_relation1)
        if it_findSentence_step1.Next():
          print("-------------------------------------")
          temp_sentence = it_findSentence_step1.Get(0)
        key_relation2 = self.module.ctx.HelperResolveSystemIdtf("rrel_example", ScType.NodeConstRole)
        it_findSentence_step2 = self.module.ctx.Iterator5(
          temp_sentence, 
          ScType.EdgeAccessConstPosPerm,
          ScType.Unknown, 
          ScType.EdgeAccessConstPosPerm, 
          key_relation2)
        if it_findSentence_step2.Next():
          print("============================================")
          input_example_sentence_link = it_findSentence_step2.Get(2)
          input_example_sentence = self.module.ctx.GetLinkContent(input_example_sentence_link)
          if input_example_sentence:
            print(input_example_sentence.AsString())

                   
          #self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, answer, param)
        return ScResult.Ok
    def printParamValue(self, param):
        paramValue = self.module.ctx.HelperGetSystemIdtf(param)
        print(paramValue)
