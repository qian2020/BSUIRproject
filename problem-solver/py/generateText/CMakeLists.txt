file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (TextGenModule SHARED ${SOURCES})

target_include_directories(TextGenModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(TextGenModule sc-memory)

add_dependencies(TextGenModule sc-memory)

sc_codegen(TextGenModule ${CMAKE_CURRENT_LIST_DIR})
