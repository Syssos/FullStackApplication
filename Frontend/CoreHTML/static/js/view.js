const urlParams = new URLSearchParams(window.location.search);
const product = urlParams.get('item');

if ('caches' in window){    
    caches.open(HOCUS_CACHE).then(cache => {
        cache.match(HOCUS_API).then(settings => {
            if (settings && product) {
                settings.json().then(data => {
                    for (const thing of data) {
                        if (thing.SKU == product) {                            
                            var cat = document.getElementById("category")
                            cat.innerHTML = pretifyThis[thing.Platform];
                            cat.href= `browse?platform=${thing.Platform}`;
                            
                            var sub = document.getElementById("subcategory")
                            sub.innerHTML = pretifyThis[thing.__class__];
                            sub.href= `browse?sub=${thing.__class__}`;
                            
                            document.getElementById("category-list").innerHTML += `<li class="breadcrumb-item active" aria-current="page" id="product">${thing.ProductName}</li>`;
                            
                            console.log(thing);
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