const HOCUS_CART = 'hocus-cart'; // cache name for cart object
const HOCUS_CACHE = 'hocus-pocus'; // cache name to use for site data
const HOCUS_API = 'http://localhost:5000/api/v1/items'; // link holding response of data being cached
const CART_API = 'http://localhost:5000/api/v1/cart'; // link holding response of data being cached

isAuthenticated().then(status => {
    if (status) {
        getCart();
        document.getElementById('signin-menu').style.display = "none";
        document.getElementById('user-control-menu').style.display = "block";
    } else {
        document.getElementById('signin-menu').style.display = "block";
        document.getElementById('user-control-menu').style.display = "none";
    }
});

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
* Used for redirecting traffic based on input from the search form
* @param {object} form - The HTML form element that calls the function
*/
async function Search(form) {
    var inputValue = form.inputBox.value;
    location.assign(`http://localhost:5001/browse?search=${inputValue}`)
}

async function SignIn(form) {
    var user = form.usernameInput.value;
    var pwd = form.passwordInput.value;
    try {
        const response = await fetch("http://localhost:5000/api/v1/autherize", {
          method: "POST", // or 'PUT'
          credentials: 'include',
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Credentials": true
          },
          body: JSON.stringify({"username": user, "password": pwd}),
        });
    
        const result = await response.json();
        if (result.login == "failure") {
            console.log("error occured, update alerts here")
        } else if (result.login == "success") {
            // location.assign("http://localhost:5001")
        }
    } catch (error) {
        console.error("Error:", error);
    }
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
* Fetchs cart data and caches it, requires authetication cookie
*/
async function collectCartData() {
    const newCache = await caches.open(HOCUS_CART);
    const options = {
        method: "GET",
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }
    newCache.add(new Request(CART_API, options));
}

function getCart() {
    var data = fetch("http://localhost:5000/api/v1/cart", {
        method: "GET", 
        credentials: 'include',
        headers: {
            "Access-Control-Allow-Credentials": true
          },
    }).then(x => {return x.text()});
    data.then(content => {
        console.log(content);
    })
}

function isAuthenticated() {
    // return bool
    return fetch("http://localhost:5000/api/v1/isauth", {
        method: "GET", 
        credentials: 'include',
        headers: {
            "Access-Control-Allow-Credentials": true
          },
    }).then(x => {
        if (x.status == 200) {
            return true
        }
        return false
    });
}