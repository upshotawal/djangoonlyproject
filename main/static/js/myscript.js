// window.addEventListener("load", function() {
//     (function($) {

//         $('.plus-cart').click(function() {
//             console.log("hello")
//                 // var id = $(this).attr("pid").toString();
//                 // var eml = this.parentNode.children[2]
//                 // console.log("hello")
//                 // console.log(id)

//             // $.ajax({
//             //     type: "GET",
//             //     url: "/pluscart",
//             //     data: {
//             //         prod_id: id
//             //     },
//             //     sucess: function(data) {
//             //         eml.innerText = data.quantity
//             //     }
//             // })
//         })

//     })(django.jQuery);
// });
function fontbig() {

    console.log("fontbig clicked");
    var id = this.attr("pid").toString();
    // var eml = this.parentNode.children[2]

    console.log(id)

    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        sucess: function(data) {
            console.log(data)
        }
    })
}