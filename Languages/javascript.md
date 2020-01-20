# JavaScript

The dominant language of the web, so we're basically stuck with it.

## Key Features

- Primitive Types- numbers, strings, booleans, NaN, and null
- Falsy Values: 0, "", null, false, NaN, undefined
- bind() - Function used to bind a function to its current context
- apply and call- Functions used to apply a different object to this.

-NaN is not equal to itself
-Stick with const by default; let otherwise
-JavaScript frequently coerces other data types into strings
-`this` is a keyword defined by the context where it is invoked. Makes object-oriented programming in JavaScript a real pain!

Promise- JS object which permits async chaining. Promises are either fulfilled or rejected
AJAX- Asynchronous JavaScript and XML
	An HTTP request where you keep the current resources on a page and update it via a JSON string. Integral to single-page applications
	+ Increases interactivity of a website and reduces page loads by permitting loading of individual assets.
	- Single-page apps generally have higher initial loading times for the sake of smaller subsequents loads
Hoisting- The key to understanding the JavaScript execution context. Variable and function declarations are put into memory during the compilation phase. This means you can execute functions and initialize varialbles before declaring them (via the function and var keywords)
Event delegation- Binding an event handler to a parent container that triggers on children
Bubbling- An event triggered on an element propogates ("bubbles") up to parents

Current Target vs Target: The target is the deepest triggering element while `current targert` is the element with the event handler.

-Use /* eslint rule: setting */ to add custom eslint rules to specific documents