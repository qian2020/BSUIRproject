/*
* This source file is part of an OSTIS project. For the latest info, see http://ostis.net
* Distributed under the MIT License
* (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
*/

#include "proModule.hpp"

SC_IMPLEMENT_MODULE(TextProAgentModule)

sc_result TextProAgentModule::InitializeImpl()
{
  m_proService.reset(new TextProAgentPythonService("processingText/TextProModule.py"));
  m_proService->Run();
  return SC_RESULT_OK;
}

sc_result TextProAgentModule::ShutdownImpl()
{
  m_proService->Stop();
  m_proService.reset();
  return SC_RESULT_OK;
}
