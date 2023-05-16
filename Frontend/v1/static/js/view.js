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

/**
* Builds the breadcrumb path for item being displayed
* @param {object} data - Object data used to build breadcrumb trail
*/
async function setBreadcrumbPaths(data){
    var cat = document.getElementById("category")
    cat.innerHTML = pretifyThis[data.Platform];
    cat.href= `browse?platform=${data.Platform}`;
    
    var sub = document.getElementById("subcategory")
    sub.innerHTML = pretifyThis[data.__class__];
    sub.href= `browse?sub=${data.__class__}`;

    document.getElementById("category-list").innerHTML += `<li class="breadcrumb-item active" aria-current="page" id="PRODUCT">${data.ProductName}</li>`;
}

/**
* creates a formated HTML string used to display the item on the page
* @param {object} data - Object holding data to be displayed
*/
function createElementView(data) {
    return `<div class="item-image"><img src="${data.ProductImage}" width="60%" height="100%" /></div>
            <div class="item-title">${data.ProductName}</div>
            <div class="item-description">${data.ProductDescription}</div>
            <div class="item-details" id="item-details">
                <div class="item-detials-price">$${data.Price}</div></br>
            </div>`
}