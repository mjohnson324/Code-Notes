# React

A frontend library that simplifies composing views.

Organize files by feature for less folder opening
Imports:
1. From node libraries
2. From directories higher up
3. From same directory

Organize components by feature.
todos/
  components/
  actions.js
  actionTypes.js
  constants.js
  index.js
  reducer.js
index.js
rootReducer.js

Key Technical Information:
-State is local to its component
-Parents interact with children via props
-Re-rendering a parent re-render's children
-List elements require unique keys, don't use array indices
-Refs can modify children in special cases

Terms:
Higher-Order Component- A component that wraps around components without modifying them, such as containers and routes
Prop-threading- When props are passed down to deeply-nested children
State- non-static data, props passed to children, or derived from component props or state
ownProps- Parent props
Component- A function which returns HTML
Reconciliation- React compares objects between events to update page views
Change Handler- A function for changing state via setstate
Lifecycle Methods- Methods used to handle and trigger component updates

Design Approach:
-Separate visual and functional concerns (render control via callback)
-It shouldn't be in state if not used in render
-UI and data models adhere to same information architecture
-Prefer functions to classes

Workflow:
1. Start with a mock
2. Establish a component hierarchy. Components should have single responsibilities
3. Make a static version in React
4. Identify the minimal (complete) representation of UI state
5. Add inverse data flow so children can update parent via callbacks

# Redux

Flux- A design pattern architecture implementing one-way data flow

Flow of Data in Redux:
Action > Dispatcher > (register, middleware) > Store > View > Action

-State is immutable in Redux and must be treated as such to update properly
-Pure functions allow developers to reverse states for easier debugging

Action- Object specifying state change and the payload used to enact change
Dispatcher- Function with callbacks that dispatches actions to the store
Reducers- Functions specifying how state changes in response to actions
Store- The app's state; registers callbacks with dispatchers; passes state to View via listeners
Selectors- Functions that take Redux state as an argument and return data to pass to a component

Reducer Composition- When a reducer is split to handle multiple slices of state
Action Creator- Dynamic payload creators that return action objects. Debugging is easy; testing is hard.

-Use Providers to avoid prop-threading in React, adding data as a store prop
-Normalize reducers to reduce complexity (don't nest data)
