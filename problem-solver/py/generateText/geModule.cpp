/*
* This source file is part of an OSTIS project. For the latest info, see http://ostis.net
* Distributed under the MIT License
* (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
*/

#include "geModule.hpp"

SC_IMPLEMENT_MODULE(TextGenAgentModule)

sc_result TextGenAgentModule::InitializeImpl()
{
  m_geService.reset(new TextGenAgentPythonService("generateText/TextGenModule.py"));
  m_geService->Run();
  return SC_RESULT_OK;
}

sc_result TextGenAgentModule::ShutdownImpl()
{
  m_geService->Stop();
  m_geService.reset();
  return SC_RESULT_OK;
}
