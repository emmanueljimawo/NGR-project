// Close message
$("#alert-message").delay(3000).slideUp(400, function() {
    $(this).alert('close');
  });


// Scroll To Top

function scrollToTop() {

  window.scrollTo({top: 0, behavior: 'smooth'});
  
  }