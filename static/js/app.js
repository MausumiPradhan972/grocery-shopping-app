 console.log("hii")
 document.addEventListener("DOMContentLoaded",function(e){
    let form = document.getElementById("submitForm");
           form.addEventListener("submit",function(e){
            let personName= document.getElementById("name").value.trim();
           let email= document.getElementById("email").value.trim();
           let password= document.getElementById("password").value.trim();
           let p=document.getElementById("para");
           console.log(personName)
          
            console.log("hiii");
            if (personName===""||email===""||password==="" ){
                e.preventDefault();
                console.log("empty");
                p.textContent="all fields are required";
            }
            else{
                document.location.href="home/";
            }
           })
 })

   console.log("js loaded");
 console.log(addToCartURL);
document.addEventListener("DOMContentLoaded",function(){
    let p=document.getElementById("p");
let cartbtn=document.querySelectorAll(".cart");
    cartbtn.forEach(button=>{
        button.addEventListener("click",function(e){
        e.preventDefault();
        alert("added");
         console.log(this.dataset.id);
         console.log(this.dataset.name)
        // alert("added");    
        // pname=document.getElementsByClassName("productName").innerText;
        
        
    });
    });
     
});
console.log("js loaded")
  window.addToCart=function(id){
    console.log("clicked",id);
    if(!id){
        console.error("invalid id",id);
        return;
    }
    let cart=JSON.parse(localStorage.getItem('cart'))||[];
    cart=cart.filter(item=>item!=null);
    let existingItem=cart.find(item=>item.id===id);
    if(existingItem){
        alert("already in cart");
    }else{
        cart.push({
            id:Number(id),
            quantity:1
        });
    }
     console.log(JSON.parse(localStorage.getItem('cart')))
    console.log("adding",id);
    localStorage.setItem("cart",JSON.stringify(cart));
    console.log("hiii")
   
    console.log("cart : ",cart)
     console.log("added");
    
  }
   window.addToWishlist=function(id){
    console.log("clicked wishlist",id);
     if(!id){
        console.error("invalid id",id);
        return; 
    }
    let wishlist=JSON.parse(localStorage.getItem('wishlist'))||[];
    console.log("addingw",id);
    wishlist.push(id);
     localStorage.setItem("wishlist",JSON.stringify(wishlist));
    console.log("wishlist : ",wishlist)
     console.log("addedw");
  } 


    