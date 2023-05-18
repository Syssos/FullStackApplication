const URL_PARAMS = new URLSearchParams(window.location.search); // Grabs window location, used for determining data displayed on page
const PRODUCT = URL_PARAMS.get('platform'); // This value represents a category the user is searching through
const SUBCATEGORY = URL_PARAMS.get('sub'); // This value represents a subcategory the user is searching through
const QUERY_STR = URL_PARAMS.get('search'); //This value represents a string of text the user is looking for

/**
* Loads and formats data from cache for specified items
*/
if ('caches' in window){
    caches.open(HOCUS_CACHE).then(cache => {
        cache.match(HOCUS_API).then(cacheData => {
            if (cacheData) {
                cacheData.json().then(data => {
                    // Code for initial page load goes here
                    updateListing(data)
                });
            } else {
                // collects cache and reloads
                collectCacheData();
                location.reload();
                document.getElementById("product-list").innerHTML = "Loading Cached Data";
            }
        })
    });
}