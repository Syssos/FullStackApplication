const HOCUS_CACHE = 'hocus-pocus';
const HOCUS_API = 'http://localhost:5000/api/v1/items';

if ('caches' in window){
    checkCache();
    // DeleteCache();
}

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

async function checkCache() {
    // Checks if cache is present for site, if not it makes a get/options request to source for json data
    caches.open(HOCUS_CACHE).then((cache) => { 
        cache.keys().then( (arrayOfRequest) => { 
            if (arrayOfRequest.length == 0) {
                CollectCacheData();
            }
        });
    });
}

async function CollectCacheData() {
    const newCache = await caches.open(HOCUS_CACHE);
    const options = {
        method: "GET",
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
    }
    newCache.add(new Request(HOCUS_API, options));
}

async function DeleteCache() {
    // Deletes cache
    caches.delete(HOCUS_CACHE).then(() => {
        console.log('Cache successfully deleted!');
    })
}

// async function DeleteAllCaches() {

// }

async function pocusSearch(url, term) {
    // Checks if cache is present for site, if not it makes a get/options request to source for json data
    return caches.open(term).then((cache) => { 
        return cache.match(url).then(settings => {
            if (!settings) {
                return doSearch(url, term);
            } else if (settings) {
                return settings.json().then(data => {return data})
            }
            return []
        });
    });
}

async function doSearch(url, term) {
    const searchCache = await caches.open(term);
    const options = {
        method: "GET",
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
    }
    return searchCache.add(new Request(url, options)).then(() => {
        return caches.open(term).then(cache => {
            return cache.match(url).then(settings => {
                if (settings) {
                    return settings.json().then(data => {
                        return data
                    })
                } else {
                    console.log("cache not found")
                    // cache not found clause
                }
            })
        })
    });    
}

async function Search(form) {
    var inputValue = form.inputBox.value;
    location.assign(`http://localhost:5001/browse?search=${inputValue}`)
}

// function doSearch(event) {
//     console.log(event);
//     if (event.code == "Enter") {
//         // Search(form)
//     }
// }