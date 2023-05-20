// // canvas control for login menu needed on all pages
var loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", SignIn)

var myOffcanvas = document.getElementById('offcanvasLogin')
myOffcanvas.addEventListener('hide.bs.offcanvas', function () {
    document.getElementById('login-canvas').style.opacity=0;
})

myOffcanvas.addEventListener('show.bs.offcanvas', function () {
    document.getElementById('login-canvas').style.opacity=1;
})

var myCartOffcanvas = document.getElementById('pocusCart')
myCartOffcanvas.addEventListener('show.bs.offcanvas', function () {
    document.getElementById('account-notification').classList.add("visually-hidden");
    document.getElementById('cart-notification').classList.add("visually-hidden");
})
/**
* checks if user is athenticated, then sets controls in header, and retreives cart items
*/
isAuthenticated().then(status => {
    if (status) {
        fetchCart();
        document.getElementById('signin-menu').style.display = "none";
        document.getElementById('user-control-menu').style.display = "block";
    } else {
        document.getElementById('signin-menu').style.display = "block";
        document.getElementById('user-control-menu').style.display = "none";
    }
});

/**
* Sets breadcrumb path for "browse" page, responsible for sorting data that gets displayed to user
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
* Creates an HTML element for each item being displayed on "browse" page
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

/**
* Builds the breadcrumb path for item being displayed on the "view" page
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
* creates a formated HTML string used to display a single item on the "view" page
* @param {object} data - Object holding data to be displayed, expected to a standard product object
* @return {string} - a string of HTML formated with product information
*/
function createElementView(data) {
    var status = `<div class="add-to-cart-btn btn btn-outline-secondary" onclick=addToCart("${data.SKU}")>add to cart</div>`;
    if (data.Amount == 0) {
        status = "Out of Stock"
    }
    // console.log(data.Amount)
    return `<div class="item-image"><img src="${data.ProductImage}" width="60%" height="100%" /></div>
            <div class="item-title">${data.ProductName}</div>
            <div class="item-description">${data.ProductDescription}</div>
            <div class="item-details" id="item-details">
                <div class="item-detials-price">$${data.Price} - ${status}</div></br>
            </div>`
}

/**
* Gathers and positions cart data into canvas
*/
async function fetchCart() {
    var data = fetch("http://localhost:5000/api/v1/cart", {
        method: "GET", 
        credentials: 'include',
        headers: {
            "Access-Control-Allow-Credentials": true
          },
    }).then(x => {return x.json()});
    
    setCart(data)
}

/**
* adds item to cart, updates screen with new cart
*/
async function addToCart(sku_id) {
    var data = fetch("http://localhost:5000/api/v1/cart/add", {
        method: "POST", 
        credentials: 'include',
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Credentials": true
          },
          body: JSON.stringify({item: sku_id})
    }).then(x => {return x.json()});    
    
    document.getElementById('account-notification').classList.remove("visually-hidden");
    document.getElementById('cart-notification').classList.remove("visually-hidden");
    setCart(data)
}

async function setCart(data) {
    data.then(cartData => {
        if (cartData.Items) {
            var container = document.getElementById('cart-item-container')
            container.innerHTML = ""
            for (const cartItem of cartData.Items) {
                var ele = `<div class="cart-item"><a href="http://localhost:5001/view?item=${cartItem.SKU}">${cartItem.ProductName}</a> - $${cartItem.Price} - <div class="remove-from-cart" onclick=removeFromCart("${cartItem.SKU}")>Remove</div></div>`
                container.innerHTML += ele;
            }
        }
    })
}

async function removeFromCart(sku_id) {
    var data = fetch("http://localhost:5000/api/v1/cart/remove", {
        method: "POST", 
        credentials: 'include',
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Credentials": true
          },
          body: JSON.stringify({item: sku_id})
    }).then(x => {return x.json()});
    
    setCart(data)
}

/**
* Validates user authentication with backend
*/
async function isAuthenticated() {
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

/**
* Uses Login form data to authenticate user credentials.
* @param {object} form - The HTML form element that calls the function
*/
async function SignIn(e) {
    // var user = form.usernameInput.value;
    // var pwd = form.passwordInput.value;
    e.preventDefault();
    let user = document.getElementById("usernameInput");
    let pwd = document.getElementById("passwordInput");

    try {
        const response = await fetch("http://localhost:5000/api/v1/autherize", {
          method: "POST", // or 'PUT'
          credentials: 'include',
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Credentials": true
          },
          body: JSON.stringify({"username": user.value, "password": pwd.value}),
        });
    
        const result = await response.json();
        if (result.login == "failure") {
            console.log("error occured, update alerts here")
        } else if (result.login == "success") {
            location.assign("http://localhost:5001")
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

async function logout() {
    var data = fetch("http://localhost:5000/api/v1/logout", {
        method: "GET", 
        credentials: 'include',
        headers: {
            "Access-Control-Allow-Credentials": true
          },
    }).then(x => {return x.json()});
    data.then(logoutcode => {
        location.assign("http://localhost:5001")
    })
}