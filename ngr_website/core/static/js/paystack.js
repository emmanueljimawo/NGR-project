//Paystack button

$('.paystack-btn').click(function (event){
    event.preventDefault();
    var this_ = $(this)

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
        label: this_.attr("data-label"),
        currency: this_.attr("data-currency").toUpperCase(),
        ref: this_.attr("data-ref"),
        callback: function (response) {
            window.location.href = this_.attr("data-url");

        },
    };

    var handler = PaystackPop.setup(obj);
    handler.openIframe();

});