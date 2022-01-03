//Paystack button

$('.paystack-btn').click(function (event){
    event.preventDefault();
    var this_ = $(this)
    var url = window.location.origin+this_.attr("data-url");  
    ref = ''+Math.floor((Math.random() * 1000000000) + 1);

    if ($('#no-of-votes option:selected').val() > 0){
        var vote_no = $('#no-of-votes option:selected').val();
    }
    else{
        var vote_no = 1
    }

    var obj = {
        key: this_.attr("data-key"),
        email: this_.attr("data-email"),
        amount: this_.attr("data-amount") * 100 * vote_no,
        label: this_.attr("data-slug"),
        currency: this_.attr("data-currency").toUpperCase(),
        ref: ref,
        callback: function (response) {
            window.location.href = `${url}${ref}`;

        },
        metadata:{
            custom_fields:[
                {
            slug: this_.attr("data-slug"),
            payment_type: this_.attr("data-payment_type")
                }
            ]
        },
    };

    var handler = PaystackPop.setup(obj);
    handler.openIframe();

});