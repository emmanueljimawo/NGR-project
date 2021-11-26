// Close message
$("#alert-message").delay(3000).slideUp(400, function() {
    $(this).alert('close');
  });


// Scroll To Top

function scrollToTop() {

  window.scrollTo({top: 0, behavior: 'smooth'});
  
  }


  function socialWindow(url) {
    var left = (screen.width - 570) / 2;
    var top = (screen.height - 570) / 2;
    var params = "menubar=no,toolbar=no,status=no,width=570,height=570,top=" + top + ",left=" + left;
    window.open(url, "NewWindow", params);
  }
  
    var tweet = encodeURIComponent($("meta[property='og:description']").attr("content"));
    
    $(".twitter").click(function(e) {
      e.preventDefault();
  
      var this_ = $(this)
      var path = this_.attr("data-url");
      var pageUrl = `${origin}${path}`
      url = `https://twitter.com/intent/tweet?url=${pageUrl}&text=${tweet}?utm_source=Naijagracerace`
        socialWindow(url);
    });
    $(".facebook").click(function(e) {
      e.preventDefault();
  
      var this_ = $(this)
      var path = this_.attr("data-url");
      var pageUrl = `${origin}${path}`
      url = `https://www.facebook.com/sharer.php?u=${pageUrl}?utm_source=Naijagracerace`
      socialWindow(url);
  });
      $(".linkedin").click(function(e) {
        e.preventDefault();
  
        var this_ = $(this)
        var path = this_.attr("data-url");
        var pageUrl = `${origin}${path}`
        url =  `http://www.linkedin.com/shareArticle?mini=true&url=${pageUrl}?utm_source=Naijagracerace` 
        socialWindow(url);
    });
    $(".whatsapp").click(function(e) {
      e.preventDefault();
  
      var this_ = $(this)
      var path = this_.attr("data-url");
      var pageUrl = `${origin}${path}`
      url =  `whatsapp://send?text=${pageUrl}?utm_source=Naijagracerace` 
      socialWindow(url);
  });
  $(".copy-link").click(function(e) {
    e.preventDefault();
  
    var this_ = $(this)
    var path = this_.attr("data-url");
    var pageUrl = `${origin}${path}?utm_source=Naijagracerace`
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(pageUrl).select();
    document.execCommand("copy");
    $temp.remove();
    
  });
  