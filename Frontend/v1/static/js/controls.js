// below are comments outlining the attended approach to handling user and cart additions. These are not perminant plans, just a way of keeping track of how it may work while the backend is being developed.

// Gather user security credentials (login menu), use cookie for authentication for caching settings and the shopping cart.

// Create method of interaction with cache for cart data, and settings. Purging and re-caching after making changes may be to either required. ie re-cache upon commit.
    // retreive "security" cookie
    // if shopping cart cache exists, or the settings cache exists, delete and reload.
    // when an item is added/removed from the cart or a setting is changed, submit post request to backend with changes, clear cache, then cache new changes from api.
         // POST method function for submitting data
         // Clear cache function for removing current data
         // GET requests through caching library to save new data
         // method of retreiving data from cache for use