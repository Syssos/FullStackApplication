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

/**
* Sets breadcrumb path, responsible for sorting data that gets displayed to user
* @param {object} data - This variable holds the data set being worked with
*/
async function updateListing(data) {
    document.getElementById("product-list").innerHTML = "";

    if (PRODUCT && SUBCATEGORY && !QUERY_STR) {
        document.getElementById("Category").innerHTML = pretifyThis[PRODUCT];
        document.getElementById("Category").href = `/browse?platform=${PRODUCT}`;
        document.getElementById("Subcategory").innerHTML = pretifyThis[SUBCATEGORY];

        for (const thing of data) {
            if (thing.__class__ == SUBCATEGORY && thing.Platform == PRODUCT) {
                updateDisplay(thing)
            }
        }
    } else if (PRODUCT && !SUBCATEGORY && !QUERY_STR) {
        // Unknown category or subcategory clause
        document.getElementById("Category").innerHTML = pretifyThis[PRODUCT];
        document.getElementById("Category").href = `/browse?platform=${PRODUCT}`;
        document.getElementById("Subcategory").style.display = 'none';
        for (const thing of data) {
            if (thing.Platform == PRODUCT) {
                updateDisplay(thing)
            }
        }
    } else if (!PRODUCT && SUBCATEGORY && !QUERY_STR) {
        document.getElementById("Category").innerHTML = pretifyThis[SUBCATEGORY];
        document.getElementById("Category").href = `/browse?sub=${SUBCATEGORY}`;
        document.getElementById("Subcategory").style.display = 'none';
        for (const thing of data) {
            if (thing.__class__ == SUBCATEGORY) {                
                updateDisplay(thing)
            }
        }
    } else if (!PRODUCT && !SUBCATEGORY && QUERY_STR) {
        document.getElementById("Category").innerHTML = QUERY_STR;
        document.getElementById("Category").href = `/browse?search=${QUERY_STR}`;
        document.getElementById("Subcategory").style.display = 'none';
        var data = searchCache(QUERY_STR);
        data.then(x => {
            for (const thing of x) {
                updateDisplay(thing)
            }
        });
    }
}

/**
* Updates front end elements to display results
* @param {object} obj - This variable holds the data set being worked with
*/
async function updateDisplay(obj) {
    document.getElementById("product-list").innerHTML += `<div class=\"product-list-item\">\
                                                            <div class=\"product-item-image\"><a href=\"/view?item=${obj.SKU}\"><img src="${obj.ProductImage}" width="90%" height="90%" /></a></div>\
                                                            <div class=\"product-details\">\
                                                                <div class=\"product-detail-title\"><a href=\"/view?item=${obj.SKU}\">${obj.ProductName}</a></div>\
                                                                <div class=\"product-detail-price\"><a href=\"/view?item=${obj.SKU}\">$${obj.Price}</a></div>\
                                                                <div class=\"product-detail-description\">${obj.ProductDescription}</div>\
                                                            </div>\
                                                          </div>`
}