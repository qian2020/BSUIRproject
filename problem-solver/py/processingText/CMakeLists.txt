file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (TextProModule SHARED ${SOURCES})

target_include_directories(TextProModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(TextProModule sc-memory)

add_dependencies(TextProModule sc-memory)

sc_codegen(TextProModule ${CMAKE_CURRENT_LIST_DIR})
