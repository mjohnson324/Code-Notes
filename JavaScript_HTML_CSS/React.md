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
