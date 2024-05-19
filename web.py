import streamlit as st
import todosUtils

todos = todosUtils.getTodos()


def add_todo():
    _todo = st.session_state["new_todo"] + '\n'
    todos.append(_todo)
    todosUtils.writeTodos(todos)


st.title("My Todo App")
st.write('This app is to increase  productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todosUtils.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo :',
              placeholder="Add new todo",
              on_change=add_todo, key='new_todo'
              )

st.write(st.session_state)
