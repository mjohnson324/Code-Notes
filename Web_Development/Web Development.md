# Web Development

* Server-Side Rendering- When web pages are rendered by the server instead of the browser

## MVC

Key Components:
Database <-> Model <-> Controller <-> View
Browser <-> Server -> Router/Dispatcher -> Controller -> Server

Model connects to Controller connects to Views, then Controller delivers assets to Server

Model validations prevent database errors

API- Server that provides non-UI information
Endpoint- A view that produces JSON

Uniform Resource Identifier- The identifier of a primary resource
Fragment Identifier- A string of characters referring to a resource subordinate to a primary resource.

Cross Site Request Forgery- When a malicious site attempts to hijack another website
Sandboxing- when the browser hides site cookies from different sites from each other, preventing CSRF tokens from being copied

HTTP is stateless because it doesn't record or preserve transactions across connections. Thus requests are independent of one another
Cookies- data snippets sent to the client; a hashmap. Cookies are a client-side example of session data and can track state
Session Token- A cookie used to verify and persist login status

Router:
checks routes
initializes controllers
call the right action in a controller
error raised if no appropriate controller found

Strong Params: When only certain params are accepted in a query
