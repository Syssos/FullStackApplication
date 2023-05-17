// Gather user security credentials and retreive security token to store as cookie for authentication for settings and the shopping cart.

// Gather users current shopping carts contents stored on api via authenticated route.

 // Create method of interacting with cache for cart data, due to options being allowed experiment with caching the cart, then purging and re-caching upon making changes. ie re-cache upon commit.
    // retreive security token in cookie
    // if shopping cart cache exists delete and reload.
    // when item added to cart, submit post request to backend with changes, clear cache, and pull in changes.
    // when item is removed from the cart, submit post request to backend with changes, clear cache, and pull in changes.