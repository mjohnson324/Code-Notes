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
