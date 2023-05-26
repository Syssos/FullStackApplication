const HOCUS_CACHE = 'hocus-pocus'; // cache name to use for site data
const HOCUS_API = 'http://localhost:5000/api/v1/items'; // link holding response of data being cached

// Checks if caches is in window, if present loads cache
if ('caches' in window){
    checkCache();
    // DeleteCache();
}

// Utilized for converting class names into usable text through out the site.
const pretifyThis = {
    Desktop : "Desktop",
    Laptop: "Laptop's",
    Other : "Other Device's",
    Cable : "Cable's",
    Ram : "Ram",
    CPU : "CPU's",
    Case: "Case's",
    GPU : "Graphic Card's",
    Monitor : "Monitor's",
    Motherboard : "Motherboard's",
    PSU : "Powersupply's",
    SSD : "Solid State Drive's"
}

/**
* Checks if user has site data cached, if not, caches needed site data.
*/
async function checkCache() {
    caches.open(HOCUS_CACHE).then((cache) => { 
        cache.keys().then( (arrayOfRequest) => { 
            if (arrayOfRequest.length == 0) {
                collectCacheData();
            }
        });
    });
}

/**
* Fetchs site data and caches it
*/
async function collectCacheData() {
    const newCache = await caches.open(HOCUS_CACHE);
    const options = {
        method: "GET",
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
    }
    newCache.add(new Request(HOCUS_API, options));
}

/**
* Deletes current cache
*/
async function DeleteCache() {
    caches.delete(HOCUS_CACHE).then(() => {
        console.log('Cache successfully deleted!');
    })
}

/**
* Searches for "querystr" within cached data
* @param {string} querystr - The string being searched for
* @return {array} - an array of product items, each item containing some kind an instance of querystr
*/
async function searchCache(querystr) {
    newCacheList = []
    return caches.open(HOCUS_CACHE).then(cache => {
        return cache.match(HOCUS_API).then(data => {
            if (data) {
                return data.json().then(cacheData => {
                    for (const item of cacheData) {
                        for (const property in item) {
                            if (typeof(item[property]) == "string" && item[property].toLowerCase().includes(querystr.toLowerCase()) && !newCacheList.includes(item)) {
                                newCacheList.push(item)
                            }
                        }
                    }
                    return newCacheList
                })
            } else {
                // cache not loaded clause
                collectCacheData()
                return searchCache(querystr)
            }
        })
    })
}

/**
* Used for redirecting traffic based on input from the search form
* @param {object} form - The HTML form element that calls the function
*/
async function Search(form) {
    var inputValue = form.inputBox.value;
    location.assign(`http://localhost:5001/browse?search=${inputValue}`)
}