const URL_PARAMS = new URLSearchParams(window.location.search); // Grabs window location, used for determining data displayed on page
const PRODUCT = URL_PARAMS.get('item'); // Product user is attempting to view
const DEFAULT_ATR = ["SKU", "ProductName", "ProductImage", "ProductDescription", "Price", "Amount", "Platform", "__class__"]; // attributes excluded from details list

/**
* Loads and formats data from cache for item specified by "PRODUCT" value
*/
if ('caches' in window){    
    caches.open(HOCUS_CACHE).then(cache => {
        cache.match(HOCUS_API).then(cacheData => {
            if (cacheData && PRODUCT) {
                cacheData.json().then(data => {
                    for (const thing of data) {
                        if (thing.SKU == PRODUCT) {                            
                            setBreadcrumbPaths(thing);

                            const element = createElementView(thing);                            
                            document.getElementById('item-container').innerHTML = element;
                            
                            for (const property in thing) {
                                if (!DEFAULT_ATR.includes(property)) {
                                    document.getElementById('item-details').innerHTML += `<div class="item-detials-bullet"><b>${property}</b>: ${thing[property]}</div>`;
                                }
                            }
                        }
                    }
                })
            } else {
                // No item in url
                console.log("no item found");
            }
        })
    })
}