// Close message
$("#alert-message").delay(3000).slideUp(400, function() {
    $(this).alert('close');
  });


  // Contestant search
  const searchOutput = $('.search-output');
  searchOutput.css('display', 'none');
  const djangoOutput = $('.django-output');
  const media_path   = `${window.location.origin}/media/`; 
  const profile_path   = `${window.location.href}profile/`; 

  $('#searchField').keyup(function(e){
      const searchValue = e.target.value;
      if (searchValue.trim().length > 0){
          fetch("/contest/contestants/search/",{
              body: JSON.stringify({searchText: searchValue}),
              method: "POST",
          }).then((res) => res.json()).then((data) => {
              console.log('data', data);
              djangoOutput.css('display', 'none');
              searchOutput.css('display', 'block');
              if (data.length === 0){
                  $('.search-output .people').html('<h3 class="text-muted display-6">Contestants unavailable...</h3>');
              }else{
                  data.forEach((object) => {
                      $('.search-output .people').html(
                         `
                         <div class="col-md-4 col-lg-3 item" data-aos="fade-up">
                          <div class="box" style="background-image: url(${media_path}${object.photograph});">
                              <div class="cover">
                      <h3 class="name">${object.last_name} ${object.other_names}</h3>
                      <p class="title">${object.profession}</p>
                      <div class="social">
                         ${object.facebook ? `<a href="${object.facebook}"><i class="fa fa-facebook-official"></i></a>` : ''} 
                         ${object.instagram ? `<a href="${object.instagram}"><i class="fa fa-instagram"></i></a>` : ''} 
                      </div>
                      <div class="d-flex justify-content-around mt-4"><a class="btn btn-warning" role="button" href="${profile_path}${object.slug}">Profile</a>
                      <span class="btn btn-success paystack-btn"
                      >
                      Vote<i class="fa fa-star ms-1"></i></span>
                </div>

                  </div>
              </div>
              <div class="ribbon"><span> ${object.count_votes ? object.count_votes|intcomma : 0 } votes</span></div>
          </div>
                          `
                      );
                  });
              }
              
          });
      }
      else{
                  djangoOutput.css('display', 'block');
                  searchOutput.css('display', 'none');
              }

  });
